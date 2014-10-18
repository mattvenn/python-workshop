"""
Dare Devil Dennis?
"""
 
import pygame
import random
from levels import levels
 
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
 
        # Set our transparent color
        self.image.set_colorkey(BLACK)
        #self.image = pygame.Surface([15, 15])
        #self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.on_ground = False
        self.crash = False

    def start(self):
        self.change_x = 0
        self.change_y = 0
        self.rect.y = 50
        self.rect.x = floor_height / 2
        self.on_ground = False
        self.crash = False
        self.floor = 0
        
    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y
        if self.change_y < -jump_acc * gravity:
            self.change_y = -jump_acc * gravity

        if self.change_y > gravity:
            self.change_y = gravity
        #print( self.change_y )


    def update(self):
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
        if self.rect.x > screen_width:
            self.floor += 1
            self.rect.x = 0
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
    def __init__(self,x,y):
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
        self.speed = random.random()
        if self.speed < 0.5:
            self.speed += 0.5
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
            obs = MovingObstacle(o['x']*screen_width,floor_height + floor_height * o['floor'] - ground_th)
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

level_num = 0
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
    if player.floor == floors:
        level_num += 1
        load_level(level_num,all_sprite_list,player)

    if player.crash:
        done = True
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()

