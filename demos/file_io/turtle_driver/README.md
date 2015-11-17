# What you will need to know

* functions
* turtle basics
* reading text files
* converting strings to integers
* loops
* lists

# Challenge

Write a program that draws regular polygons (triangle, square, pentagon, hexagon
etc) defined in a text file.

## Read a text file

Start with [reading one line from a file](../basics/README.md), then extend it to read many lines.

The text file format could be defined like this:

    x,y,sides,size

So an example line from the file might be:

    100,100,4,100

Which would draw a 100px wide square centered at the 100,100 pixel co-ordinate.

## Parse the data

You will need to [parse the lines](../csv/README.md) in the file to break them into the co-ordinates, shapes and sizes.

## Use a function to draw

Once you have the shape type, co-ordinate and size you can write a function that
accepts the data and does the drawing:

    def draw(x, y, sides, size):
        # do the drawing here

# Improvements

Things you can try if you feel confident:

* add a colour and line thickness to the file format
* add another option to the file format that will fill the shape with a colour

# More fun stuff

Check the [waveform necklace workshop out](https://github.com/mattvenn/waveform) for something similar but results in a physical laser cut necklace.
