"""
Dare Devil Dennis?
"""
 
import pygame
import random
 
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
level_height = 150
levels = 3
screen_height = level_height * levels
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
    def __init__(self, x, y):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.on_ground = False
        self.level = 0
        self.crash = False
 
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
            self.level += 1
            self.rect.x = 0
            self.rect.y += level_height
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
 
class Fence(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, height):
        """ Constructor for fences """
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        width = 10
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.x = x

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
pygame.display.set_caption('Test')
 
# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
 
# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()
 
ground_th = 10
for level in range(0,levels):
    wall = Wall(0, level_height + level_height * level - ground_th, screen_width, ground_th)
    wall_list.add(wall)
    all_sprite_list.add(wall)

# create obstacles
obs_list = pygame.sprite.Group()
for level in range(0,levels):
    for f in range(random.randint(0,3)):
        x = random.randint(20,screen_width-20)
        h = random.randint(10,50)
        fence = Fence(x,level_height + level_height * level - ground_th, h)
        obs_list.add(fence)
        all_sprite_list.add(fence)

 
# Create the player paddle object
player = Player(50, level_height / 2)
player.walls = wall_list
player.obs = obs_list
 
all_sprite_list.add(player)
 
clock = pygame.time.Clock()
 
done = False
 
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
    if player.level == levels:
        done = True

    if player.crash:
        done = True
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()

