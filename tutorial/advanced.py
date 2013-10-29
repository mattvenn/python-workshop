#Break and Continue commands
#breaks out of smallest enclosing: http://docs.python.org/release/1.5/tut/node23.html
#continue with next iteration: http://stackoverflow.com/questions/8420705/example-use-of-continue-statement-in-python
for i in range(10):
    if i < 5:
        continue
    if i % 2 == 0:
        continue
    if i >= 9:
        continue
    #avoid deeply nested code
    print i

#Keyword Arguments
def hello(number,string1="hello",string2="matt"):
    print number,string1,string2
hello(10)
hello(10,"goodbye")
hello(10,string2="laura")

#Lambda Expressions
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print filter(lambda x: x % 3 == 0, foo)
print map(lambda x: x * 2 + 10, foo)
print reduce(lambda x, y: x + y, foo)
print sorted(foo,key=lambda x: x % 2 == 1)


#Tuples and tuples vs sequences: http://stackoverflow.com/questions/1708510/python-list-vs-tuple-when-to-use-each
t = 1,2,3
print t
print t[1]
#t[1]=2 won't work

#Sequences
a = "12345"
print a[2], a[2:4]
b = [10,20,30,40]
print b[2]
print map(lambda x: x * 2, b)

#Modules
#any python file

#Packages
#a directory of python files, each dir containing a __init__.py file

#Class and Objects
class my_object:
    def __init__(self,name="matt"):
        self.name = name

    def say_hello(self):
        print "hi", self.name


obj = my_object("laura")
obj.say_hello()

class derived(my_object):
    def say_goodbye(self):
        print "bye", self.name

obj = derived()
obj.say_hello()
obj.say_goodbye()

#package
from myp.pack import *
p = pack()
p.print_name()

"""
#exceptions
while True:
    try:
        a = raw_input("type a float more than 0: ")
        a = float(a)
        if a > 0:
            break
    except ValueError:
        print "not a float"
"""
