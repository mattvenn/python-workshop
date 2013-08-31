import cv2
import time

num_photos = 10
delay = 1

def take_image(img_name):
    #setup camera
    cap = cv2.VideoCapture(0)

    #take some frames of video to allow auto-exposure etc to work.
    for i in range(10):
        success,frame = cap.read()

    #cleanup
    cap.release()
    print "writing image to", img_name
    cv2.imwrite(img_name,frame)

#take photos
for i in range(num_photos):
    photo_name = str(i) + ".jpg"
    take_image(photo_name)
    time.sleep(delay)
