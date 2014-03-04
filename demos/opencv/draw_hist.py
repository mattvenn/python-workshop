import cv2
import numpy as np

cap = cv2.VideoCapture(0)
w = 640
h = 480
x_cent = w/2
y_cent = h/2
box_size = 50

#this line is necessary for the pre-packaged opencv in windows
cv2.namedWindow('colorhist', cv2.CV_WINDOW_AUTOSIZE)
cv2.namedWindow('image', cv2.CV_WINDOW_AUTOSIZE)

while(1):
    #grab a frame from the webcam
    success, img = cap.read()
    #create a region of interest - just the middle square
    roi = img[y_cent-box_size/2:y_cent+box_size/2,x_cent-box_size/2:x_cent+box_size/2]

    #the histogram image
    h = np.zeros((300,256,3))
 
    #make an array for the histogram bins
    bins = np.arange(256).reshape(256,1)
    #store the most predominant colour
    predominant_color = [0,0,0]
    color = [ (255,0,0),(0,255,0),(0,0,255) ]
    for ch, col in enumerate(color):
        #calcHist args: images, channel, mask, size, ranges
        hist_item = cv2.calcHist([roi],[ch],None,[256],[0,256])
        #round the results to integers
        hist=np.int32(np.around(hist_item))
        #stack the 2 arrays
        pts = np.column_stack((bins,hist))
        #draw a graph using the stack as the vertex co-ordinates
        cv2.polylines(h,[pts],False,col)

        #store the most dominant colour
        max_colour = np.argmax(pts,axis=0)
        predominant_color[ch]= int(max_colour[1])

    #flip the pic horizontally
    h=np.flipud(h)
    #convert the rgb values to hsv
    hsv = cv2.cvtColor(np.asarray([[predominant_color]],dtype=np.uint8),cv2.COLOR_BGR2HSV)
    #print to the image the rgb and hsv values
    cv2.putText(img,"BGR: " + str(predominant_color), (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.putText(img,"HSV: " + str(hsv), (10,80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))

    #draw rectangle after doing histogram
    cv2.rectangle(img, (x_cent-box_size/2, y_cent-box_size/2), (x_cent+box_size/2,y_cent+box_size/2), predominant_color, -1)
     
    #Show various images: 
    #just the region of interest
    #cv2.imshow('roi',roi)
    #the histogram window
    cv2.imshow('colorhist',h)
    #the main window
    cv2.imshow('image',img)

    #if key pressed is 'Esc', exit the loop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    if k == 99: #c key
        print("capture")
        print(hsv)
        break

cv2.destroyAllWindows()
