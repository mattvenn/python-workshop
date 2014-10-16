"""
Dare Devil Dennis?
"""
 
import pygame
 
"""
Global constants
"""
 
# Colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
GREEN     = (  0, 255,   0)
 
# Screen dimensions
SCREEN_WIDTH  = 800
level_height = 150
levels = 3
SCREEN_HEIGHT = level_height * levels
gravity = 2.5
jump_acc = gravity * 2.5
 
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
 
    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y
        if self.change_y < -jump_acc * gravity:
            self.change_y = -jump_acc * gravity

        if self.change_y > gravity:
            self.change_y = gravity
        print( self.change_y )


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
        if self.rect.x > SCREEN_WIDTH:
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
 
class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
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
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
# Set the title of the window
pygame.display.set_caption('Test')
 
# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
 
# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()
 
ground_th = 10
for level in range(0,levels):
    wall = Wall(0, level_height + level_height * level - ground_th, SCREEN_WIDTH, ground_th)
    wall_list.add(wall)
    all_sprite_list.add(wall)
 
 
# Create the player paddle object
player = Player(50, 50)
player.walls = wall_list
 
all_sprite_list.add(player)
 
clock = pygame.time.Clock()
 
done = False
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #keys
    kp = pygame.key.get_pressed()
    if kp[pygame.K_q]:
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
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()

