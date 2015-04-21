# Basic file I/O

The [read_write.py](read_write.py) demo shows how to open a file for write, then
open it for read. 

The file created is [file.txt](file.txt) which has a 'hello' on each line.

When the file is printed, there is an extra line in between each 'hello'. This
is because the `print()` function adds its own newline character to the string,
which already has its own newline - meaning 2 newlines get printed.

## open()

`open()` takes 2 parameters: the name of the file and the read or write mode.
Some important modes are:

* 'w' : open the file for writing (will delete any contents first)
* 'r' : open the file for reading
* 'a' : open the file for writing, but will append new data to the old

`open()` returns a 'file handle' which is why I shorten it to `fh` in the
examples. The file handle is the bit that lets us read or write.

## write()

`write()` takes one parameter: the data to write. It can be anything. If you
want to write strings on separate lines you'll need to add the newline character
`\n` or all the lines will be joined together.

## read()

`read()` reads the whole file in as one big piece. We mostly will use
`readlines()` because that splits up the file into separate lines for us.

## readlines()

`readlines()` reads the whole file into a list, with each line as a separate
element in a list.

## close()

`close()` closes the file handle, which is good practice but often not
necessary; as Python will close all open files when the program ends.
