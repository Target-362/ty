from tkinter import *
win = Tk()

string = ''
result = Label(text = string)
result.grid(row = 0, column = 0,
            columnspan = 4)

Grid.rowconfigure(win, 0, weight=1)
Grid.columnconfigure(win, 0, weight=1)
Grid.rowconfigure(win, 1, weight=1)
Grid.columnconfigure(win, 1, weight=1)
Grid.rowconfigure(win, 2, weight=1)
Grid.columnconfigure(win, 2, weight=1)
Grid.rowconfigure(win, 3, weight=1)
Grid.columnconfigure(win, 3, weight=1)
Grid.rowconfigure(win, 3, weight=1)
Grid.columnconfigure(win, 4, weight=1)
Grid.rowconfigure(win, 4, weight=1)

def add_1():
    global string
    string += '1'
    result['text'] = string

def add_2():
    global string
    string += '2'
    result['text'] = string

def add_3():
    global string
    string += '3'
    result['text'] = string

def add_4():
    global string
    string += '4'
    result['text'] = string

def add_5():
    global string
    string += '5'
    result['text'] = string


def add_6():
    global string
    string += '6'
    result['text'] = string


def add_7():
    global string
    string += '7'
    result['text'] = string


def add_8():
    global string
    string += '8'
    result['text'] = string


def add_9():
    global string
    string += '9'
    result['text'] = string


def add_10():
    global string
    string += '0'
    result['text'] = string

btn1 = Button(text = '1', command = add_1)
btn1.grid(row = 3, column = 0, sticky='NSEW')
btn2 = Button(text = '2', command = add_2)
btn2.grid(row = 3, column = 1, sticky='NSEW')
btn3 = Button(text = '3', command = add_3)
btn3.grid(row = 3, column = 2, sticky='NSEW')
btn4 = Button(text = '4', command = add_4)
btn4.grid(row = 2, column = 0, sticky='NSEW')
btn5 = Button(text = '5', command = add_5)
btn5.grid(row = 2, column = 1, sticky='NSEW')
btn6 = Button(text = '6', command = add_6)
btn6.grid(row = 2, column = 2, sticky='NSEW')
btn7 = Button(text = '7', command = add_7)
btn7.grid(row = 1, column = 0, sticky='NSEW')
btn8 = Button(text = '8', command = add_8)
btn8.grid(row = 1, column = 1, sticky='NSEW')
btn9 = Button(text = '9', command = add_9)
btn9.grid(row = 1, column = 2, sticky='NSEW')
btn0 = Button(text = '0', command = add_10)
btn0.grid(row = 4, column = 1, sticky='NSEW')
btnPlus = Button(text = '+')
btnPlus.grid(row = 1, column = 3, sticky='NSEW')
btnMinus = Button(text = '-')
btnMinus.grid(row = 2, column = 3, sticky='NSEW')
btnMultiply = Button(text = '×')
btnMultiply.grid(row = 4, column = 3, sticky='NSEW')
btnDivide = Button(text = '÷')
btnDivide.grid(row = 3, column = 3, sticky='NSEW')
btnEqualis = Button(text = '=')
btnEqualis.grid(row = 4, column = 2, sticky='NSEW')
btnDelete = Button(text = '←')
btnDelete.grid(row = 4, column = 0, sticky='NSEW')
win.mainloop()
