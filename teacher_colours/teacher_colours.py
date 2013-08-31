import cv2
import numpy as np
import pickle
import show_hist

db_file = "stored"
cap = cv2.VideoCapture(0)
w = 640
h = 480
x_cent = w/2
y_cent = h/2
box_size = 50

regions = [
    {
    "box_x" : w/2,
    "box_y" : h/4,
    },
    {
    "box_x" : w/2,
    "box_y" : 3*h/4,
    },
    ]

while(1):
    #grab a frame from the webcam
    success, img = cap.read()
    #create a region of interest - just the middle square

    color = [ (255,0,0),(0,255,0),(0,0,255) ]
    for roi_num, region in enumerate(regions):
        #get the region of interest
        roi = img[region["box_y"]-box_size/2:region["box_y"]+box_size/2,region["box_x"]-box_size/2:region["box_x"]+box_size/2]

        #make an array for the histogram bins
        bins = np.arange(256).reshape(256,1)
        #store the most predominant colour
        region["predominant_color" ] = np.zeros(3)

        for ch, col in enumerate(color):
            #calcHist args: images, channel, mask, size, ranges
            hist_item = cv2.calcHist([roi],[ch],None,[256],[0,256])
            #round the results to integers
            hist=np.int32(np.around(hist_item))
            #stack the 2 arrays
            pts = np.column_stack((bins,hist))
            #store the most dominant colour
            max_colour = np.argmax(pts,axis=0)
            region["predominant_color"][ch] = int(max_colour[1])

        #convert the rgb values to hsv
        region["hsv"] = cv2.cvtColor(np.asarray([[region["predominant_color"]]],dtype=np.uint8),cv2.COLOR_BGR2HSV)[0][0]
        #print to the image the rgb and hsv values
        cv2.putText(img,str(region["hsv"]), (region["box_x"]+box_size,region["box_y"]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255))

        #draw rectangle after doing histogram
        cv2.rectangle(img, (region["box_x"]-box_size/2, region["box_y"]-box_size/2), (region["box_x"]+box_size/2,region["box_y"]+box_size/2), region["predominant_color"], -1)
     
        cv2.putText(img,"press space to capture", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255))
    #the main window
    cv2.imshow('image',img)

    #key handling
    k = cv2.waitKey(5) & 0xFF
    if k == 27: #esc key
        break
    if k == 32: #space bar
        #load the array
        try:
            db = open(db_file,'r')
            stored = pickle.load(db)
            print "loaded pickled"
            db.close()
        except (EOFError,IOError):
            print "initialising new array"
            stored = []
        stored.append([regions[0]["hsv"],regions[1]["hsv"]])

        for store in stored:
            print store[0][0],store[1][0]

        #save the array
        db = open(db_file,'w')
        pickle.dump(stored,db)
        db.close()
        
        show_hist.draw_graph(stored)

cv2.destroyAllWindows()
