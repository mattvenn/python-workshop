"""
Dare Devil Dennis?
"""
 
import pygame
import random
import pygame.mixer
from levels import levels

level_num = 0
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()
 
"""
Global constants
"""
 
# Colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
GREEN     = (  0, 255,   0)
 
# Screen dimensions
screen_width  = 800
floor_height = 150
floors = 3
screen_height = floor_height * floors
gravity = 2.5
max_speed = 10
motor_sound_queue_length = 10
jump_acc = gravity * 2.3
 
# This class represents the bar at the bottom that the player controls
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player controls. """
 
    # Set speed vector
    change_x = 0
    change_y = 0
    walls = None
 
    # Constructor function
    def __init__(self):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Set height, width
        self.image = pygame.image.load("sprites/dennis.png").convert()
        # sounds
        # crash sounds is straight forward
        self.crash_sound = pygame.mixer.Sound('sounds/crash.wav') 
        self.crash_sound.set_volume(0.4)

        # motor sound is made of a lot of samples we store in a list
        self.motor_sounds = []
        import glob
        files = glob.glob('sounds/motor*wav')
        files.sort()
        for sound in files:
            self.motor_sounds.append(pygame.mixer.Sound(sound)) 

        #get a free channel
        self.motor_ch = pygame.mixer.find_channel()
        self.motor_ch.set_volume(0.3)

 
        # Set our transparent color
        self.image.set_colorkey(BLACK)
        #self.image = pygame.Surface([15, 15])
        #self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.on_ground = False
        self.crash = False
        self.lives = 3

    def start(self):
        self.change_x = 0
        self.change_y = 0
        self.rect.y = 50
        self.rect.x = floor_height / 2
        self.on_ground = False
        self.crash = False
        self.finish = False
        
    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x

        if self.change_x > max_speed:
            self.change_x = max_speed

        self.change_y += y
        if self.change_y < -jump_acc * gravity:
            self.change_y = -jump_acc * gravity

        if self.change_y > gravity:
            self.change_y = gravity

        #work out motor sound speed
        self.motor_sound_speed = int((len(self.motor_sounds)-1) * (self.change_x / max_speed ))

        print(self.motor_sound_speed)


    def update(self):
        #motor sounds
        if self.motor_ch.get_queue() <= motor_sound_queue_length:
            self.motor_ch.queue(self.motor_sounds[self.motor_sound_speed])

        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
        #what to do if gone off the screen
        if self.rect.x > screen_width:
            self.rect.x = 0
            if self.rect.y > floor_height * 2:
                self.finish = True
            self.rect.y += floor_height
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        self.on_ground = False
        for block in block_hit_list:
            self.on_ground = True 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
        
        block_hit_list = pygame.sprite.spritecollide(self, self.obs, False)
        for block in block_hit_list:
            self.crash = True
            self.crash_sound.play()
            print("crash!")
 
class Obstacle(pygame.sprite.Sprite):
    """ Things the player can run into. """
    def __init__(self, x, y,type):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        t = random.randint(0,2)
        sprite = type + '.png'
        self.image = pygame.image.load("sprites/" + sprite).convert()
 
        # Set our transparent color
        self.image.set_colorkey(BLACK)
 
        # Make our bottom-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.x = x

class MovingObstacle(pygame.sprite.Sprite):
    def __init__(self,x,y,speed):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        t = random.randint(0,0)
        if t == 0:
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
        self.max_move = - floor_height / 3

    def update(self):

        if self.y <= self.max_move:
            self.up = False
        elif self.y >= 0:
            self.up = True
        #update the high res y
        if self.up:
            self.y -= self.speed
        else:
            self.y += self.speed
        #then copy to rect
        self.rect.bottom = self.start_y + int(self.y)
        

class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the ground """
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Make a blue wall, of the size specified in the parameters
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
pygame.display.set_caption('Dennis')
 

all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

def load_level(level_num,all_sprite_list,player):
    print("%d of %d levels" % (level_num, num_levels))
    # empty the list
    all_sprite_list.empty()
    # Make the walls. (x_pos, y_pos, width, height)
    wall_list = pygame.sprite.Group()

    #create the level!
    #start with floors. Get the gaps:
    ground_th = 10
    for floor in range(0,floors):
        for seg in levels[level_num]['floors'][floor]:
            wall = Wall(seg[0] * screen_width, floor_height + floor_height * floor - ground_th, seg[1]*screen_width, ground_th)
            wall_list.add(wall)
            all_sprite_list.add(wall)

    # create obstacles
    obs_list = pygame.sprite.Group()
    for o in levels[level_num]['obs']:
        if o['type'] == 'police':
            obs = MovingObstacle(o['x']*screen_width,floor_height + floor_height * o['floor'] - ground_th, o['speed'])
        else:
            obs = Obstacle(o['x']*screen_width,floor_height + floor_height * o['floor'] - ground_th,o['type'])
        obs_list.add(obs)
        all_sprite_list.add(obs)

    player.start()
    player.walls = wall_list
    player.obs = obs_list
    all_sprite_list.add(player)
 
# Create the player paddle object
player = Player()

clock = pygame.time.Clock()
 
done = False

num_levels = len(levels)
load_level(level_num,all_sprite_list,player)
print("starting")
while not done:
 
    #allow click on window close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #keys
    kp = pygame.key.get_pressed()
    if kp[pygame.K_q]:
        #can only accelarate when we are on the ground
        if player.on_ground:
            player.changespeed(0.1, 0)
    if kp[pygame.K_w]:
        done = True
    if kp[pygame.K_SPACE]:
        #only jump if on ground
        if player.on_ground:
            player.changespeed(0, -jump_acc)

    player.changespeed(0, 0.1)

    all_sprite_list.update()
 
    screen.fill(BLACK)
 
    all_sprite_list.draw(screen)
    if player.finish:
        level_num += 1
        if level_num == num_levels:
            done = True
        else:
            load_level(level_num,all_sprite_list,player)

    if player.crash:
        player.lives -= 1
        if player.lives == 0:
            done = True
        else:
            player.start()
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()

