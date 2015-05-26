# the data
names = ['Matt', 'Sue', 'James']
scores = [25, 100, 105]

# how many records we have
records = len(names)

# open the file for write
fh = open('csv.txt', 'w')

# loop through the records
record = 0
while record < records:
    # get the name and score from the lists
    name = names[record]
    score = scores[record]
    # write them to the file
    fh.write(name + ',' + str(score) + '\n')
    record = record + 1

fh.close()
# now we'll read the data back in

