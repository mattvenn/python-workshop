from PIL import Image
#open our first test image
im = Image.open("test.png")
#rotate it
im = im.rotate(40)
#resize it
im = im.resize((100,200))
#save it
im.save("test.png")
