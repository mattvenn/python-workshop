import cv2
import numpy as np

# create video capture
cap = cv2.VideoCapture(0)

min_area = 50 #avoid noise
h = 480
w = 640

#we draw on a blank background
background = np.zeros((h, w, 3), np.uint8)
ox,oy = 0,0

while(1):
    # read the frames
    success,frame = cap.read()
    # flip the image
    frame = cv2.flip(frame, flipCode=1)

    # smooth it
    frame = cv2.blur(frame,(3,3))

    # convert to hsv and find range of colors
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower = np.array((170,150,150))
    upper = np.array((179,255,255))
    thresh = cv2.inRange(hsv,lower,upper)

    # find contours in the threshold image
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    # finding contour with maximum area and store it as best_cnt
    max_area = 0
    found = False
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > max_area and area > min_area:
            max_area = area
            best_cnt = cnt
            found = True

    #if we find a big enough contour, then use it to draw lines
    if found:
        # finding centroids of best_cnt
        M = cv2.moments(best_cnt)
        cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
        if ox and oy:
            #draw a line
            cv2.line(background,(ox,oy),(cx,cy),255,5)
        ox,oy = cx,cy

    #Show various images: 
    #original frame
    
    #cv2.imshow('frame',frame)
    #the contours
    #cv2.imshow('thresh',thresh2)
    
    #this line is necessary for the pre-packaged opencv in windows
    cv2.namedWindow('background', cv2.CV_WINDOW_AUTOSIZE)
    cv2.imshow('background',background)

    #if key pressed is 'Esc', exit the loop
    if cv2.waitKey(33)== 27:
        break

# Clean up everything before leaving
cv2.destroyAllWindows()
cap.release()
