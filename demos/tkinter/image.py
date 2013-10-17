#requires python-imaging-tk
from PIL import Image, ImageTk
import Tkinter

tk = Tkinter.Tk()

image = Image.open("polar.jpg")
photo = ImageTk.PhotoImage(image)
label = Tkinter.Label(image=photo)

label.pack()
tk.mainloop()
