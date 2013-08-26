
#http://effbot.org/imagingbook/

"""
windows - install pillow (PIL for windows) from
http://www.lfd.uci.edu/~gohlke/pythonlibs/

then a different import line:
"""
from PIL import Image, ImageDraw

width = 500
height = 500
num_squares = 10

im = Image.new("RGB", (width,height), "white")
draw = ImageDraw.Draw(im)
squares = zip(
    range(0,width/2,width/2/num_squares),
    range(0,height/2,height/2/num_squares),
    range(1,100,100/num_squares))

for x,y,colour in squares:
        coords=[x,y,width-x,width-y]
        colour = (colour+50,255-colour,100+colour)
        print coords, colour
        draw.rectangle(coords,fill=colour,outline=255)
# write to stdout
im.save("test.jpg", "JPEG")

