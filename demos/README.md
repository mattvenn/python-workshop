# Demos

Here are some demos I've written that try to demonstrate various libraries as
simply as possible. Each directory has a demo file and a readme like this. The
readme contains the information you'll need to install a library.

# Library installation

## Mac or Linux (Raspberry Pi)

In general if a library is called LIB, you'd do this:

    sudo pip install LIB

## Windows

You need to go to this website
[http://www.lfd.uci.edu/~gohlke/pythonlibs/](http://www.lfd.uci.edu/~gohlke/pythonlibs/)
and search for the name of the library. There will be a few different versions
and you need to match the version of windows and python you're using. Then
download the whl file.

If you are using Python version > 2.7.9 you will already have pip installed.
Otherwise [follow these
instructions](https://pip.pypa.io/en/latest/installing.html) to install it.

Then run pip from the command line to install the downloaded package:

    pip install yourpackage.whl

* [More information on using pip to install whl files](https://pip.pypa.io/en/latest/user_guide.html#installing-from-wheels
* [Useful video guide to installing packages on windows](https://www.youtube.com/watch?v=jnpC_Ib_lbc)

