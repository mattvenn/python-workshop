"""
inspired by demo from
http://python-textbok.readthedocs.org/en/latest/Introduction_to_GUI_Programming.html
"""
from Tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.last_number = 0
        self.total_label_text = IntVar()
        self.number = 0
        self.operation = '+'

        self.result = Label(master, textvariable=self.total_label_text)

        self.add_button = Button(master, text="+", command=self.add)
        self.sub_button = Button(master, text="-", command=self.sub)
        self.clear_button = Button(master, text="c", command=self.clear)
        self.equals_button = Button(master, text="=", command=self.equals)

        #do buttons in a loop
        row = 1
        for number in range(0,10):
            button = Button(master, text=number, command=lambda x=number: self.update_number(x))
            if number == 0:
                button.grid(row=4,column=1)
                print("adding button 0")
            else:
                button.grid(row=row,column=(number-1)%3)
                if number %3 == 0:
                    row += 1

        # LAYOUT
        self.result.grid(row=0,column=0,columnspan=4)
        self.add_button.grid(row=1,column=3)
        self.sub_button.grid(row=2,column=3)
        self.clear_button.grid(row=3,column=3)
        self.equals_button.grid(row=4,column=3)

    def equals(self):
        if self.operation == '+':
            result = self.last_number + self.number
        elif self.operation == '-':
            result = self.last_number - self.number
        self.total_label_text.set(result)
        self.number = result

    def add(self):
        self.operation = '+'
        self.last_number = self.number
        self.number = 0

    def sub(self):
        self.operation = '-'
        self.last_number = self.number
        self.number = 0

    def clear(self):
        self.number = 0
        self.last_number = 0
        self.total_label_text.set(self.number)

    def update_number(self,number):
        self.number *= 10
        self.number += number
        self.total_label_text.set(self.number)

root = Tk()
my_gui = Calculator(root)
root.mainloop()
