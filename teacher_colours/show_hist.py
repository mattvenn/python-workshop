# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pickle

N = 180 #number of different hues

def load_history():
    #load the file
    db_file = "stored"
    db = open(db_file,'r')
    stored = pickle.load(db)
    print "loaded pickled"
    db.close()
    return stored

def draw_graph(stored):
    hues = np.zeros(N)
    for store in stored:
        hues[store[0][0]]+=1
        hues[store[1][0]]+=1

    ind = np.arange(N)  # the x locations for the groups

    fig, ax = plt.subplots()

    #generate the colour array
    colours = []
    for i in np.arange(0,1,1.0/N):
        HSV = np.dstack((i,1,1))
        colours.append( matplotlib.colors.hsv_to_rgb(HSV)[0][0])

    width = 1 # the width of the bars
    rects1 = ax.bar(ind, hues, width, color=colours)

    # add some
    ax.set_title('Hue of teacher clothing')
    #ax.set_xticks(ind+width)

    plt.show()

if __name__ == '__main__':
    stored = load_history()
    draw_graph(stored)

