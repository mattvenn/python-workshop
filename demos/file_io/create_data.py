import random
with open("data.txt", 'w') as fh:
    for i in range(100):
        fh.write(str(random.random()) + "\n")
