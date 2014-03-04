import Tkinter
tk = Tkinter.Tk()

x = 0
y = 0
colour = "red"

def start_draw(event):
    global x,y
    print "clicked at", event.x, event.y 
    x = event.x
    y = event.y

def draw(event):
    global x,y,colour
    new_x = event.x
    new_y = event.y
    canvas.create_line(new_x,new_y,x,y,width=2,fill=colour)
    x = new_x
    y = new_y

def set_colour(c):
    global colour
    print("set colour to " + c)
    colour = c

button = Tkinter.Button(tk,text="Red",command=lambda: set_colour("red"))
button.pack()
button = Tkinter.Button(tk,text="Blue",command=lambda: set_colour("blue"))
button.pack()

canvas = Tkinter.Canvas(tk, width=400, height=400, bg="white")
canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)
canvas.pack()

tk.mainloop()
