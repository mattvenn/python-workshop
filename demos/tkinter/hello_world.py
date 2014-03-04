import Tkinter
from Tkconstants import *
tk = Tkinter.Tk()

label = Tkinter.Label(tk, text="Hello, World")
label.pack()

button = Tkinter.Button(tk,text="Exit",command=tk.destroy)
button.pack()

tk.mainloop()

