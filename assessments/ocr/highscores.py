"""
Design, code and test a system to store and manage user names and their highest score. 
The system must be able to 
* create a file 
* add data to a file 
* locate data in the file by name and their highest score 
* delete an item and its associated data from the file 
* locate and update a high score for a user 
The system need only cater for 10 items
"""
import csv

csv_file = 'scores.csv'

#write the data
def write_data(data):
    file = open(csv_file,'w')
    writer = csv.writer(file)
    #write the old data
    for row in data:
        writer.writerow(row)
    file.close()

#adding to the file
def add_data(name,score):
    data = read_file()
    data.append([name,score])
    write_data(data)

#reading
def read_file():
    try:
        file = open(csv_file)
        data = []
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
        return data
    except IOError:
        #return empty array if the file doesn't exist
        return []

#delete
def delete(name,score):
    data = read_file()
    #search the array
    if([name,score] in data):
        print("removing record")
        data.remove([name,score])
    else:
        print("couldn't find a matching record")
    #write the new data
    write_data(data)

#go through all the scores and find the highest
def find_highest_score():
    data = read_file()
    score = 0
    name = ''
    for row in data:
        #convert score string to a number
        if int(row[1]) > score:
            score = int(row[1])
            name = row[0]
    print("highest score is", score, "by", name)
        

#print out all scores with this name
def find_name(name):
    data = read_file()
    print("high scores for", name)
    for row in data:
        if row[0] == name:
            print(row[1])

#user interface
while True:
    print( """
    0: quit
    1: add to the file
    2: read file
    3: delete a record
    4: find highest score
    5: find name
    """)
    choice = int(raw_input("choose option: "))
    if choice == 0:
        #quit
        exit(1)
    if choice == 1:
        name = raw_input("name: ")
        score = int(raw_input("score: "))
        add_data(name,score)
    if choice == 2:
        data = read_file()
        print(data)
    if choice == 3:
        name = raw_input("name: ")
        score = raw_input("score: ")
        delete(name,score)
    if choice == 4:
        find_highest_score()
    if choice == 5:
        name = raw_input("name: ")
        find_name(name)
