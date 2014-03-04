import Tkinter
tk = Tkinter.Tk()

def callback(event):
    print "clicked at", event.x, event.y 

frame = Tkinter.Frame(tk, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()

tk.mainloop()
