# File IO

A quick demo of using files to store and retreive data.

## create_data.py

[create_data.py](create_data.py) uses a file with the write setting `w` to make a [data file](data.txt) with 100 random numbers in it.

A key part is knowing that we have to convert a floating point number to a
string and add a new line to it.

I'm using the `with` keyword to ensure that the file is closed nicely regardless
of any exceptions raised. Information on the `with` keyword can be [found on the
effbot website](http://effbot.org/zone/python-with-statement.htm).

## barchart.py

[barchart.py](barchart.py) loads the data and uses it to create a simple bar
chart.

When we load the data, we need to convert it back to a float so we can use it to
draw rectangles of specific lengths.

# Requirements 

the pillow module (a better supported version of PIL).

For installation instructions see the [Library Readme](../README.md)

