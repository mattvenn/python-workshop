# Snake example

This is a port of the classic snake game found on Nokia phones. I'm pretty sure
everyone's seen it or played it!

# Game setup

The game starts by defining some constants that choose the size of the sprites
and the size of the board. 

We define some colours so we can use then easily later.

Then we define our objects.

# Objects Overview

In this game we use 3 objects:

* Snake - this is the head of the snake, that we control
* Body - the body grows as we eat food, it follows the head
* Food - randomly appears and after a while disappears

## Snake

The snake object is the most complicated. It can move around, has a sound for
when it eats, and can add extra body sections to itself. 

In the update method, it:

* moves the head, 
* moves all the body sections so they follow the head 
* check to see if we crashes into any of the body sections
* checks to see if it hits any food.

If any food is hit, the `add_body()` method is called. This method adds a new
body sprite to the snake, and also adds the sprite to the snake group and the
all_sprites group. This lets us check if we ever crash into ourselves.

## Body

The body object just loads the image and can then have its position queried and
updated.

## Food

The food object creates a new food sprite, and puts it somewhere randomly on the
screen. It makes a note of the time when it was created, and after a certain
time, the update() method will remove the sprite so it disappears.

# More game setup

After the objects have been defined, we've still got some stuff to do before we
can get started:

* Initialise pygame with the init() method
* Set the screen size
* Create the sprite groups
* Load sounds
* Create the player object
* Start the clock

# The main loop

The loop is the heart of the game. The most important thing here is to regularly
call update() on all the sprites.

We also:

* Check for key presses
* Make food appear randomly
* Wipe the screen and redraw all the sprites
* Show the score
* Check to see if the snake has crashed, and if so, end the game.

# Sprites and sounds

* Sprites were found by searching for 'snake sprite' on google images
* Sounds came from [freesoundlib](https://www.freesound.org/)
