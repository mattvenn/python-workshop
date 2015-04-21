# open the file for write
fh = open("file.txt", 'w')

# in a loop:
loops = 0
while loops < 10:
    # write hello 10 times. The `\n` is to make each line separate
    fh.write("hello\n")
    loops = loops + 1

# close the file
fh.close()


# open the file for read
fh = open("file.txt", 'r')

# read all the lines into a list
lines = fh.readlines()

# using a for loop, print the lines out
for line in lines:
    print(line)
