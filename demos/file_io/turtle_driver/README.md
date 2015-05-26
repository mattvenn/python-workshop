# What you will need to know

* functions
* turtle basics
* reading text files
* converting strings to integers
* conditionals

# Challenge

write a program that does:

* reads a text file
* uses the data from the file to draw simple geometric shapes with the turtle library
* make a function to do the drawing, and start just with squares
* the text file can be any length long

The text file format is defined like this:

    x,y,shape_type,shape_size

So an example line from the file might be:

    100,100,square,100

Which would draw a 100px wide square centered at the 100,100 pixel co-ordinate.

# Improvements

Things you can try if you feel confident:

* add a colour and line thickness to the file
* add a function to draw shapes that the turtle library doesn't have already - eg an octogon, hexagon
* have an error message if the shape isn't supported
* hack the [image processing program](brightness.py) to generate a list of shapes that you can then draw with your program

# More fun stuff

Check the [waveform necklace workshop out](https://github.com/mattvenn/waveform) for something similar but results in a physical laser cut necklace.
