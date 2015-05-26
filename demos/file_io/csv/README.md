# CSV

CSV stands for comma separated values. It might look like this:

    name, score
    Matt, 25
    Sue, 100
    James, 105

The first line is called the header. It's often left off to make life easier.

# Writing

Writing a CSV file is pretty easy, we need to add together the values to make a
long string and then write that to a file like in the [basics
demo](../basics/README.md)

    name = "Matt"
    score = 25
    fh.write(name + ',' + str(score) + '\n')

The score is a number, so it has to be converted to a string before we can write
it to the file.

