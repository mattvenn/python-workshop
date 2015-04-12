'''
if you want to draw good bar charts you should be using
matplotlib - see the demos in the scipy directory
'''

from PIL import Image, ImageDraw

width = 500
height = 500

# create an image
im = Image.new("RGB", (width,height), "white")
# get the draw object
draw = ImageDraw.Draw(im)

# define a colour
BLUE = (0, 0, 255)

with open("data.txt") as fh:
    data = fh.readlines() 

# work out bar width
num_points = len(data)
bar_w = width / num_points

# counter for which bar
bar_num = 0

# draw the data
for point in data:
    bar_h = float(point)
    # data goes from 0 to 1, so scale to height
    bar_h *= height

    coords=[bar_num*bar_w, 0, bar_num*bar_w + bar_w, bar_h]
    draw.rectangle(coords, fill=BLUE)
    bar_num += 1

#save the image
im.save("random.png", "PNG")
