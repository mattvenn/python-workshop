"""
Snake
"""
 
import pygame
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
tiles = 15 #how big the board should be
score_height = tile_size #how big the score header should be

#then work out the screen height and width
screen_width  = tile_size * tiles
screen_height = tile_size * tiles + score_height

#points stuff
chomp_points = 1 # this also gets added to the speed of the game
food_timer = 3000 # how long food last before disappearing (ms)

# The snake object
class Snake(pygame.sprite.Sprite):
 
    # Constructor function
    def __init__(self):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        #load the eating sound
        self.eat_sound = pygame.mixer.Sound('eat.wav') 
        self.eat_sound.set_volume(0.7)

        #load the image
        self.imageMaster = pygame.image.load("head.png").convert_alpha()
        self.image = self.imageMaster

        #set the starting position
        self.rect = self.image.get_rect()
        self.rect.y = (tiles / 2) * tile_size
        self.rect.x = (tiles / 2) * tile_size

        #initial starting setup
        self.points = 0        
        self.direction = 'left'
        self.done = False

    #add a new body part
    def add_body(self,number):
        new_body = Body((self.rect.x,self.rect.y))
        snake_list.add(new_body)
        all_sprite_list.add(new_body)

    #this is called every frame
    def update(self):
    
        old_xy = (self.rect.x,self.rect.y)
        """ Update the snake position. """
        # Move left/right
        if self.direction == 'left':
            self.image = pygame.transform.rotate(self.imageMaster, 90)
            self.rect.x -= tile_size
        elif self.direction == 'right':
            self.image = pygame.transform.rotate(self.imageMaster, -90)
            self.rect.x += tile_size
        elif self.direction == 'up':
            self.image = pygame.transform.rotate(self.imageMaster, 0)
            self.rect.y -= tile_size
        elif self.direction == 'down':
            self.image = pygame.transform.rotate(self.imageMaster, 180)
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

        #starting position
        self.rect = self.image.get_rect()
        (self.rect.x,self.rect.y) = (x,y)

    #return the position of the body
    def get_xy(self):
        return (self.rect.x,self.rect.y)

    #update the position
    def set_xy(self,(x,y)):
        self.rect.x = x
        self.rect.y = y
        
#food objects
class Food(pygame.sprite.Sprite):
    def __init__(self):

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        #load sprite's image
        self.image = pygame.image.load("fruit.png").convert_alpha()
 
        # put it somewhere random
        self.rect = self.image.get_rect()
        #but avoid the top score snakeer
        self.rect.y = random.randint(0,tiles-1) * tile_size + score_height
        self.rect.x = random.randint(0,tiles-1) * tile_size

        #make a note of the time
        self.time = pygame.time.get_ticks()

    #called every frame
    def update(self):
        if pygame.time.get_ticks() - self.time > food_timer:
            #disappear
            self.kill()

#function to show the score
def show_score():

    font = pygame.font.SysFont('Arial', tile_size - 5)
    background = pygame.Surface((screen_width,score_height))
    background = background.convert()
    background.fill(BLUE)
    text = font.render("Points = %d" % snake.points, 1, BLACK)
    textpos = text.get_rect(centerx=screen_width/2,centery=score_height / 2)
    background.blit(text, textpos)
    screen.blit(background, (0,0))

"""
Now all the objects have been defined, we can start up the game
"""

# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create screen
screen = pygame.display.set_mode([screen_width, screen_height])
 
# Set the title of the window
pygame.display.set_caption('Snake')

#we keep a track of the sprites in these groups:
#the head and the body of the snake in here
snake_list = pygame.sprite.Group()
#food in here
food_list = pygame.sprite.Group()
#everything in here
all_sprite_list = pygame.sprite.Group()

#load the food appear sound
food_sound = pygame.mixer.Sound('appear.wav') 
food_sound.set_volume(0.7)

end_sound = pygame.mixer.Sound('game-over.wav') 
end_sound.set_volume(0.7)

# Create the snake object, and add to group
snake = Snake()
all_sprite_list.add(snake)

#start clock
clock = pygame.time.Clock()
 
print("starting")

#when this changes to true, the game is over
done = False

while not done:
    #we could get multiple events here. So that's why we break if a key is pressed.
    #it stops the snake from being able to change directions multiple times in one update
    for event in pygame.event.get():
        #allow click on window close button
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.direction != 'right':
                snake.direction = 'left'
                break
            elif event.key == pygame.K_RIGHT and snake.direction != 'left':
                snake.direction = 'right'
                break
            elif event.key == pygame.K_UP and snake.direction != 'down':
                snake.direction = 'up'
                break
            elif event.key == pygame.K_DOWN and snake.direction != 'up':
                snake.direction = 'down'
                break
    
    #make some food randomly
    if random.randint(0,20) == 0:
        food = Food()
        #the food appears in a random place, but we don't want it to appear on the 
        #snake itself. So check if it collides with anything and if so, don't add 
        #it to the food list.
        food_hit_list = pygame.sprite.spritecollide(food, all_sprite_list, False)
        if len(food_hit_list) == 0:
            food_sound.play()
            all_sprite_list.add(food)
            food_list.add(food)

    #update all sprites
    all_sprite_list.update()
 
    #blank the screen
    screen.fill(WHITE)
 
    #draw all sprites
    all_sprite_list.draw(screen)

    #show scores
    show_score()

    #crashed?
    if snake.done:
        #let snake see the crash
        end_sound.play()
        pygame.time.wait(2000)
        done = True

    #flip the screen, this prevents flickering (look up double buffering)
    pygame.display.flip()
 
    #slow update, but increases with points
    #argument to tick is the framerate
    clock.tick(5 + snake.points)

#after crashed, show points and quit
print("you got %d points" % snake.points)
pygame.quit()
