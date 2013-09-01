# opencv

From http://opencv.org/about.html

OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library.

The library has more than 2500 optimized algorithms, which includes a comprehensive set of both classic and state-of-the-art computer vision and machine learning algorithms. These algorithms can be used to detect and recognize faces, identify objects, etc.

# numpy

The cv2 module is the latest python module for opencv. It depends on another python module called NumPy which is a highly stable and fast array processing library.

Everything in cv2 is returned as NumPy objects like ndarray and native Python objects like lists,tuples,dictionary, etc. So due to this NumPy support, you can do any numpy operation here. 

NumPy is documented here: http://www.numpy.org/

# draw_hist demo

This demo looks at a small region of interest in the center of the video stream. It works out the predominant colour, and converts the RGB value to HSV. These values are printed on the video stream. We also draw a histogram of the RGB values in the region of interest.

You might need something like this to help you identify the hue (the H in HSV) of an object. It's much easier doing image tracking within the HSV colour space than the RGB colour space.

Once you have your hue, we can use it in the colour tracker demo.

The demo was based on http://opencvpython.blogspot.co.uk/2012/04/drawing-histogram-in-opencv-python.html

# colour_tracker demo

This demo identifies the largest area in a video feed that is of a certain hue. We do this by converting each frame from RGB to HSV, then filtering out a range of hues we're interested in. Once we've done that we use the opencv findContours method to find blobs in the frame. The largest blob found is then used to draw a line. In this way we can do a 'virtual graffiti' system. It could be extended to controlling windows in a GUI by sticking bits of coloured tape on your fingers.

The demo was based on http://stackoverflow.com/questions/12943410/opencv-python-single-rather-than-multiple-blob-tracking

# Documentation

Some really good sources of learning and examples:

* http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_tutorials.html
* http://opencvpython.blogspot.co.uk/

And the official docs:

* http://docs.opencv.org/


# Requirements

The opencv module

## Windows

follow these instructions:
    
    http://opencvpython.blogspot.co.uk/2012/05/install-opencv-in-windows-for-python.html

## Linux/Mac

pip install numpy
pip install opencv???

