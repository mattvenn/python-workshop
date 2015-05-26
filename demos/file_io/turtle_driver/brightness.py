# requires the PIL library
from PIL import Image

# open the image to be pixelated
image_file = "face.jpg"
img = Image.open(image_file)
img_width = img.size[0]
img_height = img.size[1]
print("opened %s [%d x %d]" % (image_file,img_width,img_height))

# sums to work out how many and how big the tiles are
x_tiles = 10
tile_width = img_width / x_tiles
# assume square tiles
y_tiles = img_height / tile_width

# function that returns the average value of a region of pixels
def get_brightness(image,box):
    brightness = 0
    region = image.crop(box)
    width, height = region.size
    # iterate through all the pixels
    for x in range(width):
        for y in range(height):
            pixel = region.getpixel((x,y))
            brightness += sum(pixel)/3
    brightness = brightness / (width * height)
    return brightness

# split the image into squares
for x in range(0,img_width,tile_width):
    for y in range(0,img_height,tile_width):
        # and for each of those squares, 
        # find the average colour
        box = (x, y, x+tile_width, y+tile_width)
        brightness = get_brightness(img, box)

        print("x=%4d, y=%4d, bright=%s" % (x, y, brightness))

