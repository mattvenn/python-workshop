import cv2
import numpy as np

# create video capture
cap = cv2.VideoCapture(0)

h = 480
w = 640
cap.set(3,w)
cap.set(4,h)

#we draw on a blank background
background = np.zeros((h, w, 3), np.uint8)
slit_num = 0

while(1):
    # read the frames
    success,frame = cap.read()
    frame = cv2.flip(frame, flipCode=1)

    #copy a line from the frame to the background
    for x in range(0,2):
        for y in range(0,h):
            line = frame[0:h,0:2]
            background[y][x+slit_num] = frame[y][x+slit_num]

    #increment the slit position
    slit_num+=2
    if slit_num >= w:
        slit_num = 0

    #draw a line that shows the slit
    cv2.line(frame,(x+slit_num,0),(x+slit_num,h),255,2)

    #show images
    cv2.imshow('background',background)
    cv2.imshow('frame',frame)

    #if key pressed is 'Esc', exit the loop
    if cv2.waitKey(33)== 27:
        break

# Clean up everything before leaving
cv2.destroyAllWindows()
cap.release()
