'''Добавление библиотеки'''
from tkinter import *
'''Создание окна'''
win = Tk()
'''
Создание строки и текстовой метки,
в которых будут отображаться
действия и результат работы
'''
string = ''
result = Label(text = string)
result.grid(row = 0, column = 0,
            columnspan = 4)
'''
Настройка растяжения кнопок на экране
'''
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
'''
Создание кнопок
'''
btn1 = Button(text = '1')
btn1.grid(row = 3, column = 0, sticky='NSEW')
btn2 = Button(text = '2')
btn2.grid(row = 3, column = 1, sticky='NSEW')
btn3 = Button(text = '3')
btn3.grid(row = 3, column = 2, sticky='NSEW')
btn4 = Button(text = '4')
btn4.grid(row = 2, column = 0, sticky='NSEW')
btn5 = Button(text = '5')
btn5.grid(row = 2, column = 1, sticky='NSEW')
btn6 = Button(text = '6')
btn6.grid(row = 2, column = 2, sticky='NSEW')
btn7 = Button(text = '7')
btn7.grid(row = 1, column = 0, sticky='NSEW')
btn8 = Button(text = '8')
btn8.grid(row = 1, column = 1, sticky='NSEW')
btn9 = Button(text = '9')
btn9.grid(row = 1, column = 2, sticky='NSEW')
btn0 = Button(text = '0')
btn0.grid(row = 4, column = 0, sticky='NSEW')
btnPlus = Button(text = '0')
btnPlus.grid(row = 4, column = 0, sticky='NSEW')
btnMinus = Button(text = '0')
btn.grid(row = 4, column = 0, sticky='NSEW')
btn0 = Button(text = '0')
btn0.grid(row = 4, column = 0, sticky='NSEW')
btn0 = Button(text = '0')
btn0.grid(row = 4, column = 0, sticky='NSEW')
win.mainloop()