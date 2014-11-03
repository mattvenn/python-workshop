"""
Snake
"""
 
import pygame
import time
import random

#sound prep
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()
 
"""
Global constants
"""
 
# Colors
BLACK    = (0,   0,   0  )
WHITE    = (255, 255, 255)
BLUE     = (0,   0,   255)
GREEN    = (0,   255, 0  )
YELLOW   = (255, 255, 0  )
RED      = (255, 0,   0  )
 
# Screen dimensions
tile_size = 32 #size of the sprites
tiles = 20
screen_width  = tile_size * tiles
score_height = tile_size
screen_height = tile_size * tiles + score_height
start_speed = 10

#points stuff
chomp_points = 1 # this also gets added to the speed of the game
food_timer = 3 # how long food last before disappearing

# The snake object
class Player(pygame.sprite.Sprite):
 
    # Constructor function
    def __init__(self):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        self.eat_sound = pygame.mixer.Sound('eat.wav') 
        self.eat_sound.set_volume(0.7)

        # Set height, width
        self.image = pygame.image.load("head.png").convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.y = (tiles / 2) * tile_size
        self.rect.x = (tiles / 2) * tile_size

        self.points = 0        
        self.direction = 'left'
        self.done = False

    def get_xy(self):
        return (self.rect.x,self.rect.y)

    #add a new body part
    def add_body(self,number):
        new_body = Body((self.rect.x,self.rect.y))
        snake_list.add(new_body)
        all_sprite_list.add(new_body)

    def update(self):
    
        old_xy = (self.rect.x,self.rect.y)
        """ Update the player position. """
        # Move left/right
        if self.direction == 'left':
            self.rect.x -= tile_size
        elif self.direction == 'right':
            self.rect.x += tile_size
        elif self.direction == 'up':
            self.rect.y -= tile_size
        elif self.direction == 'down':
            self.rect.y += tile_size

        #update the body, pass down the new co-ordinates to all body sections
        for body in snake_list:
            next_xy = body.get_xy()
            body.set_xy(old_xy)
            old_xy = next_xy

        #what to do if gone off the screen
        if self.rect.x >= screen_width:
            self.rect.x = 0
        elif self.rect.x < 0:
            self.rect.x = screen_width - tile_size
        elif self.rect.y >= screen_height:
            self.rect.y = score_height 
        elif self.rect.y < score_height:
            self.rect.y = screen_height - tile_size
 
        #did we hit ourself?
        body_hit_list = pygame.sprite.spritecollide(self, snake_list, False)
        if len(body_hit_list):
            print("finished")
            self.done = True

        #did we hit some food?
        food_hit_list = pygame.sprite.spritecollide(self, food_list, False)
        for food in food_hit_list:
            food.kill()
            self.add_body(1)
            self.eat_sound.play()
            self.points += chomp_points

 
# The snake's body class
class Body(pygame.sprite.Sprite):
 
    # Constructor function
    def __init__(self,(x,y)):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        #load sprite
        self.image = pygame.image.load("tail.png").convert_alpha()

        self.rect = self.image.get_rect()
        (self.rect.x,self.rect.y) = (x,y)
        #self.rect.y = y

    def get_xy(self):
        return (self.rect.x,self.rect.y)

    def set_xy(self,(x,y)):
        self.rect.x = x
        self.rect.y = y
        
class Food(pygame.sprite.Sprite):
    def __init__(self):

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        #load sprite
        self.image = pygame.image.load("fruit.png").convert_alpha()
 
        # Make our bottom-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(0,tiles) * tile_size
        self.rect.x = random.randint(0,tiles) * tile_size

        self.time = time.time()

    def get_xy(self):
        return (self.rect.x,self.rect.y)

    def update(self):
        if time.time() - self.time > food_timer:
            #disappear
            self.kill()
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create sized screen
screen = pygame.display.set_mode([screen_width, screen_height])
 
# Set the title of the window
pygame.display.set_caption('Snake')

#all_sprite_list = pygame.sprite.Group()
snake_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
food_list = pygame.sprite.Group()

#show the score
def show_score():

    #font from http://fontstruct.com/fontstructions/show/beeb
    font = pygame.font.Font('Beeb.ttf', tile_size - 5)
    background = pygame.Surface((screen_width,score_height))
    background = background.convert()
    background.fill(BLUE)
    text = font.render("Points = %d" % player.points, 1, BLACK)
    textpos = text.get_rect(centerx=screen_width/2,centery=score_height / 2)
    background.blit(text, textpos)
    screen.blit(background, (0,0))

 
# Create the player 
player = Player()
all_sprite_list.add(player)

clock = pygame.time.Clock()
 
done = False

print("starting")
start_time = time.time()

food_sound = pygame.mixer.Sound('appear.wav') 
food_sound.set_volume(0.7)

end_sound = pygame.mixer.Sound('game-over.wav') 
end_sound.set_volume(0.7)

while not done:
    #we could get multiple events here. So that's why we break if a key is pressed.
    #it stops the player from being able to change directions multiple times in one update
    for event in pygame.event.get():
        #allow click on window close button
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player.direction != 'right':
                player.direction = 'left'
                break
            elif event.key == pygame.K_RIGHT and player.direction != 'left':
                player.direction = 'right'
                break
            elif event.key == pygame.K_UP and player.direction != 'down':
                player.direction = 'up'
                break
            elif event.key == pygame.K_DOWN and player.direction != 'up':
                player.direction = 'down'
                break
    
    #make some food randomly
    if random.randint(0,20) == 0:
        food = Food()
        crash = False
        #if the sprite happens to be on something already, don't add it
        for sprite in all_sprite_list:
            if food.get_xy() == sprite.get_xy():
                crash = True
        #otherwise add it to the lists
        if not crash:
            food_sound.play()
            all_sprite_list.add(food)
            food_list.add(food)

    #update all sprites
    all_sprite_list.update()
 
    screen.fill(WHITE)
 
    all_sprite_list.draw(screen)

    #show scores
    show_score()

    #crashed?
    if player.done:
        #let player see the crash
        end_sound.play()
        time.sleep(2)
        done = True

    pygame.display.flip()
 
    #slow update, but increases with points
    clock.tick(5 + player.points)

print("you got %d points" % player.points)

pygame.quit()
