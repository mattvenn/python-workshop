#import all from turtle library
from turtle import *
pencolor('red')
fillcolor( 'yellow')
speed(5)

#start a fill
begin_fill()
loops = 0

while loops < 20:
    forward(200)
    left(170)
    loops = loops + 1
    
#end the fill
end_fill()
done()
