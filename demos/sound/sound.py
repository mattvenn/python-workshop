#!usr/bin/python

import pygame.mixer

#initialise the mixer to 44.1khz, 16bit, 2channel with 4096 buffer
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()

#load the sound
bell = pygame.mixer.Sound('bell.wav') 
bell.set_volume(0.4)

#play it
bell.play()

while pygame.mixer.get_busy():
    #wait till the sound has finished
    pass
