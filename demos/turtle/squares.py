from turtle import *

speed(0)
width(2)

def square(size):
    penup()
    setpos(0,0)
#    setpos(size/2,size/2)
    pendown()
    begin_fill()
    for i in range(4):
        right(90)
        forward(size)
    end_fill()


num_squares = 30
for i in range(num_squares):
    size = i * 10
    color(0.5,1-(1.0/num_squares)*i,(1.0/num_squares)*i)
    left(360/num_squares)
    square(size)

print "done"
done()
