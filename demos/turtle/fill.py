#import all from turtle library
from turtle import *
color('red', 'yellow')

#start a fill
begin_fill()
while True:
    forward(200)
    left(160)
    #break out of the loop when we're back at 0
    if abs(pos()) < 1:
        break
    
#end the fill
end_fill()
done()
