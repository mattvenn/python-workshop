import pygame.camera
from PIL import Image
import time

num_photos = 10
delay = 1

def take_image(img_name):
    img = cam.get_image()
    img_size = img.get_size()

    pygame_string_image = pygame.image.tostring(img, "RGBA",False)
    pil_image = Image.fromstring("RGBA",img_size,pygame_string_image)
    print "saving to", img_name
    pil_image.save(img_name, "JPEG")


#setup camera
pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()

#take photos
for i in range(num_photos):
    photo_name = str(i) + ".jpg"
    take_image(photo_name)
    time.sleep(delay)


#cleanup
pygame.camera.quit()
