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
        self.clear_button = Button(master, text="clear", command=self.clear)
        self.equals_button = Button(master, text="=", command=self.equals)

        self.num_buttons = []
        for number in range(10):
            button = Button(master, text=number, command=lambda x=number: self.update_number(x))
            button.pack()
            self.num_buttons.append(button)

        # LAYOUT
        self.result.pack()
        self.add_button.pack()
        self.sub_button.pack()
        self.clear_button.pack()
        self.equals_button.pack()

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
