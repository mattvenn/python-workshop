import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
w = 640
h = 480
x_cent = w/2
y_cent = h/2
box_size = 50
while(1):
    _, img = cap.read()
    roi = img[y_cent-box_size/2:y_cent+box_size/2,x_cent-box_size/2:x_cent+box_size/2]
    h = np.zeros((300,256,3))
 
    bins = np.arange(256).reshape(256,1)
    predominant_color = [0,0,0]
    color = [ (255,0,0),(0,255,0),(0,0,255) ]
    for ch, col in enumerate(color):
        hist_item = cv2.calcHist([roi],[ch],None,[256],[0,256])
        #cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX)
        hist=np.int32(np.around(hist_item))
        pts = np.column_stack((bins,hist))
        cv2.polylines(h,[pts],False,col)

        max_hsv = np.argmax(pts,axis=0)
        predominant_color[ch]= int(max_hsv[1])

     

    h=np.flipud(h)
#    import ipdb; ipdb.set_trace()
    hsv = cv2.cvtColor(np.asarray([[predominant_color]],dtype=np.uint8),cv2.COLOR_BGR2HSV)
    cv2.putText(img,"BGR: " + str(predominant_color), (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.putText(img,"HSV: " + str(hsv), (10,80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))

    #draw rectangle after doing histogram
    cv2.rectangle(img, (x_cent-box_size/2, y_cent-box_size/2), (x_cent+box_size/2,y_cent+box_size/2), predominant_color, -1)
     
    cv2.imshow('colorhist',h)
    cv2.imshow('image',img)
#    cv2.imshow('roi',roi)

#    cv2.imshow('frame',frame)
#    cv2.imshow('mask',mask)
#    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
