from PIL import Image, ImageDraw
from random import randint

width = 500
height = 500
num_squares = 10

#create an image
im = Image.new("RGB", (width,height), "white")
#get the draw object
draw = ImageDraw.Draw(im)

#and use the draw object to draw a lot of randomly placed, sized and coloured rectangles!
for square in range(num_squares):
    #randint generates a random number between the 2 arguments we pass it
    coords=[randint(0,width),randint(0,height),randint(0,width),randint(0,height)]
    colour = (randint(0,255),randint(0,255),randint(0,255))
    print coords, colour
    draw.rectangle(coords,fill=colour)

#save the image
im.save("test.png", "PNG")

