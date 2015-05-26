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

# Reading

Reading is the same but the other way round. We have to read the file in, then
split the lines into their segments. And if we need to get numbers back we'll
have to convert the string (that we read from the file) to a number.

Here's how you can split a line into sections divided by the comma:

    name, score = record.split(',')

And here's how we can conver the score back to an integer:

    score = int(score)

Finally, if you see a `\n` character in your data it's because this is the
character used to separate lines in a file. To get rid of it you can strip it
off the end of the string we read from the file:

    record = record.strip()
