"""
Dare Devil Denis?
"""
 
import pygame
import time
import random
import pygame.mixer
from levels import levels

#change this to start at a higher level
level_num = 0

#sound prep
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()
 
"""
Global constants
"""
 
# Colors
BLACK    = (   0,   0,   0)
BLUE     = (   0,   0, 255)
GREEN     = (  0, 255,   0)
 
# Screen dimensions
screen_width  = 800
score_height = 60
floor_height = 160
floors = 3
screen_height = floor_height * floors + score_height

#game dynamics
gravity = 2.3 # can't fall faster than this
fall_speed = 0.1 # our downward speed increases by this amount
max_speed = 10 # max horizontal speed
jump_acc = gravity * 2.4 # jump accelaration

#points stuff
money_points = 100
level_points = 100
speed_points = 200 # if you do the whole level in 5 seconds

#queue length to make sure we don't run out of motor sounds
motor_sound_queue_length = 5
 
# This class is for Denis
class Denis(pygame.sprite.Sprite):
 
    # Set speed vector
    change_x = 0
    change_y = 0
    floors = None
 
    # Constructor function
    def __init__(self):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Set height, width
        self.denis_image = pygame.image.load("sprites/denis.png").convert()
        self.crash_image = pygame.image.load("sprites/crash.png").convert()
        self.image = self.denis_image

        # sounds
        # crash sounds is straight forward
        self.crash_sound = pygame.mixer.Sound('sounds/crash.wav') 
        self.crash_sound.set_volume(0.7)
        self.coin_sound = pygame.mixer.Sound('sounds/coin.wav') 
        self.coin_sound.set_volume(0.7)

        # motor sound is made of a lot of samples we store in a list
        # as speed changes we play different samples
        self.motor_sounds = []
        files = []
        for i in range(1,7):
            files.append('sounds/motor%d.wav' % i)
        for file in files:
            self.motor_sounds.append(pygame.mixer.Sound(file)) 

        #get a free channel
        self.motor_ch = pygame.mixer.find_channel()
        self.motor_ch.set_volume(0.6)
 
        # Set our transparent color
        self.image.set_colorkey(BLACK)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.lives = 3
        self.points = 0

    #call this at the start of a new level or lose a life
    def start(self):
        self.change_x = 0
        self.change_y = 0.1
        self.rect.y = score_height + floor_height / 2 
        self.rect.x = floor_height / 2
        self.on_ground = False
        self.crash = False
        self.finish = False
        self.image = self.denis_image
        
    #Change the speed of the denis.
    def changespeed(self, x, y):
        self.change_x += x

        #can't go faster than max, or slower than 0
        if self.change_x > max_speed:
            self.change_x = max_speed
        if self.change_x < 0:
            self.change_x = 0

        self.change_y += y

        #can't go up faster than our jump acc
        if self.change_y < -jump_acc * gravity:
            self.change_y = -jump_acc * gravity

        #can't go down faster than gravity
        if self.change_y > gravity:
            self.change_y = gravity


    #update the denis position, check for crashes etc
    def update(self):
        #don't do any updates if we've crashed
        if self.crash:
            return

        #motor sounds
        #work out motor sound speed
        self.motor_sound_speed = int((len(self.motor_sounds)-1) * (self.change_x / max_speed ))
        #then queue up a bunch of sounds so that the sound plays continuously
        while self.motor_ch.get_queue() <= motor_sound_queue_length:
            self.motor_ch.queue(self.motor_sounds[self.motor_sound_speed])

        # Update the denis position.
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit floor - like hitting the side of a hole
        block_hit_list = pygame.sprite.spritecollide(self, self.floors, False)
        for block in block_hit_list:
            self.rect.right = block.rect.left

        #what to do if gone off the screen
        if self.rect.x > screen_width:
            self.rect.x = 0
            if self.rect.y > score_height + floor_height * 2:
                self.finish = True
            self.rect.y += floor_height

        # jump or fall
        self.rect.y += self.change_y
 
        # Check and see if we landed on the floor?
        block_hit_list = pygame.sprite.spritecollide(self, self.floors, False)
        self.on_ground = False
        for block in block_hit_list:
            self.on_ground = True 
            self.rect.bottom = block.rect.top
        
        #collide with obstacles?
        block_hit_list = pygame.sprite.spritecollide(self, self.obs, False)
        for block in block_hit_list:
            if block.type == 'money':
                #remove sprite from all groups
                block.kill()
                print("ker-ching!") 
                #play a sound
                self.coin_sound.play()
                #increase points
                self.points += money_points
            else:
                print("crash!")
                self.crash = True
                self.crash_time = time.time()
                self.crash_sound.play()
                self.image = self.crash_image
 
#stuff like trees, houses, graves
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y,type):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        self.type = type
 
        sprite = type + '.png'
        self.image = pygame.image.load("sprites/" + sprite).convert()
 
        # Set our transparent color
        self.image.set_colorkey(BLACK)
 
        # Make our bottom-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.x = x

#a policeman
class MovingObstacle(pygame.sprite.Sprite):
    def __init__(self,x,y,speed):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        self.type = 'police'
 
        sprite = 'police.png'
        self.image = pygame.image.load("sprites/" + sprite).convert()
 
        # Set our transparent color
        self.image.set_colorkey(BLACK)
 
        # Make our bottom-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.start_y = y
        self.rect.x = x

        #rects have to be defined as ints, so make a separate y that can be higher res
        self.y = 0
        self.speed = speed
        self.up = True
        self.max_move = - floor_height / 2

    def update(self):
        #alternatively move up and down
        if self.y <= self.max_move:
            self.up = False
        elif self.y >= 0:
            self.up = True

        #update the high res y
        if self.up:
            self.y -= self.speed
        else:
            self.y += self.speed

        #then update the sprite's position with the int(y)
        self.rect.bottom = self.start_y + int(self.y)
        

#the floors
class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Make a green floor, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create sized screen
screen = pygame.display.set_mode([screen_width, screen_height])
 
# Set the title of the window
pygame.display.set_caption('Denis')

#music for start and end
pygame.mixer.music.load("sounds/begin.wav")
pygame.mixer.music.set_volume(0.5)

all_sprite_list = pygame.sprite.Group()
floor_list = pygame.sprite.Group()

#show the score at the top of the screen
def show_score():
    #font from http://fontstruct.com/fontstructions/show/beeb
    font = pygame.font.Font('Beeb.ttf', 30)
    background = pygame.Surface((screen_width,score_height))
    background = background.convert()
    background.fill(BLUE)
    text = font.render("Wages %05d   Lives %d" % (denis.points, denis.lives), 1, BLACK)
    textpos = text.get_rect(centerx=screen_width/2,centery=score_height / 2)
    background.blit(text, textpos)
    screen.blit(background, (0,0))

#title for beginning
def show_title():
    pygame.mixer.music.play(1)

    #font from http://fontstruct.com/fontstructions/show/beeb
    font = pygame.font.Font('Beeb.ttf', 30)
    background = pygame.Surface((screen_width,screen_height))
    background = background.convert()
    background.fill(BLUE)

    x = screen_width / 2
    y = screen_height / 4

    text = font.render("Dare Devil Denis!" , 1, GREEN)
    textpos = text.get_rect(centerx=x,centery=y)
    background.blit(text, textpos)

    y += 80

    text = font.render("Left Shift - Accelerate" , 1, BLACK)
    textpos = text.get_rect(centerx=x,centery=y)
    background.blit(text, textpos)

    y += 40

    text = font.render("Space - Jump" , 1, BLACK)
    textpos = text.get_rect(centerx=x,centery=y)
    background.blit(text, textpos)

    y += 40

    text = font.render("Enter - Brake" , 1, BLACK)
    textpos = text.get_rect(centerx=x,centery=y)
    background.blit(text, textpos)

    screen.blit(background, (0,0))
    pygame.display.flip()

    #wait till music finishes
    while pygame.mixer.music.get_busy():
        pass

#end screen showing score
def show_end():
    pygame.mixer.music.play(1)

    #font from http://fontstruct.com/fontstructions/show/beeb
    font = pygame.font.Font('Beeb.ttf', 30)
    background = pygame.Surface((screen_width,screen_height))
    background = background.convert()
    background.fill(BLUE)

    x = screen_width / 2
    y = screen_height / 2

    text = font.render("Game Over!" , 1, GREEN)
    textpos = text.get_rect(centerx=x,centery=y)
    background.blit(text, textpos)

    y += 80

    text = font.render("You wages were %05d" % denis.points , 1, BLACK)
    textpos = text.get_rect(centerx=x,centery=y)
    background.blit(text, textpos)

    screen.blit(background, (0,0))
    pygame.display.flip()

    #wait till music finishes
    while pygame.mixer.music.get_busy():
        pass

#function to load a level defined in the levels.py file 
#check the levels.py file for how to create new levels.
def load_level(level_num,all_sprite_list,denis):
    print("%d of %d levels" % (level_num, num_levels))
    # empty the list
    all_sprite_list.empty()
    # Make the floors. (x_pos, y_pos, width, height)
    floor_list = pygame.sprite.Group()

    #create the level!
    #start with floors. Get the gaps:
    ground_th = 10
    for floor in range(0,floors):
        for seg in levels[level_num]['floors'][floor]:
            floor_obj = Floor(seg[0] * screen_width, score_height + floor_height + floor_height * floor - ground_th, seg[1]*screen_width, ground_th)
            floor_list.add(floor_obj)
            all_sprite_list.add(floor_obj)

    # create obstacles
    obs_list = pygame.sprite.Group()
    for o in levels[level_num]['obs']:
        if o['type'] == 'police':
            obs = MovingObstacle(o['x']*screen_width,score_height + floor_height + floor_height * o['floor'] - ground_th, o['speed'])
        else:
            obs = Obstacle(o['x']*screen_width,score_height + floor_height + floor_height * o['floor'] - ground_th,o['type'])
        obs_list.add(obs)
        all_sprite_list.add(obs)

    #get the player ready
    denis.start()
    #update the player's floor and obstacle list
    denis.floors = floor_list
    denis.obs = obs_list
    all_sprite_list.add(denis)
 
# Create denis 
denis = Denis()

clock = pygame.time.Clock()
 
#flag for finishing the game
done = False

num_levels = len(levels)
load_level(level_num,all_sprite_list,denis)

#start with the title
show_title()

print("starting")
start_time = time.time()
crash_time = 0

#main loop
while not done:
    #allow click on window close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #keys
    kp = pygame.key.get_pressed()
    if kp[pygame.K_LSHIFT]:
        #can only accelarate when we are on the ground
        if denis.on_ground:
            denis.changespeed(0.1, 0)
    if kp[pygame.K_RETURN]:
        #can only brake when we are on the ground
        if denis.on_ground:
            denis.changespeed(-0.2, 0)
    if kp[pygame.K_q]:
        done = True
    if kp[pygame.K_SPACE]:
        #only jump if on ground
        if denis.on_ground:
            denis.changespeed(0, -jump_acc)

    #always fall down
    denis.changespeed(0, fall_speed)

    #update all sprites
    all_sprite_list.update()
 
    #blank the screen
    screen.fill(BLACK)
 
    #draw new screen
    all_sprite_list.draw(screen)

    #draw score
    show_score()

    #flip display (double buffering)
    pygame.display.flip()
 
    #check if we've finished the level
    if denis.finish:
        level_num += 1
        #increase score
        denis.points += level_points

        #work out how long it took for time score
        level_time = time.time() - start_time
        start_time = time.time()
        speed_bonus = int(speed_points - level_time * 10)
        if speed_bonus > 0:
            print("speed bonus: %d" % speed_bonus)
            denis.points += speed_bonus

        print("denis points total: %d" % denis.points)
        if level_num == num_levels:
            done = True
        else:
            load_level(level_num,all_sprite_list,denis)


    if denis.crash and time.time() - denis.crash_time > 2:
        denis.lives -= 1
        if denis.lives == 0:
            done = True
        denis.start()

    clock.tick(60)
 
#show ending scren
show_end()

#finish!
pygame.quit()
