import random

# ask the user for a number, and convert to an int
lines = int(input("how many lines of data? "))

# open a file for writing (that's what the 'w' is for)
with open("data.txt", 'w') as fh:
    # generate the data
    for i in range(100):
        # write it to the file
        # it needs to be a string, and we also add a newline
        fh.write(str(random.random()) + "\n")
