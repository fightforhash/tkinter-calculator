import math
from tkinter import *
from tkmacosx import Button

express = " "


def press(num):
    global express
    express = express + str(num)

    equation.set(express)

def equalpress():
    try:
        global express
        total = str(eval(express))
        equation.set(total)
        express = ""
    except ZeroDivisionError:
        equation.set("Math Error")
    except:
        equation.set("Error")
        express = ""

def clear():
    global express
    express = ""
    equation.set("")


def log():
    global express
    result = math.log(eval(express))
    equation.set(result)
    express = ""

def sin():
    global express
    result = math.sin(eval(express))
    equation.set(result)
    express = ""

def cos():
    global express
    result = math.cos(eval(express))
    equation.set(result)
    express = ""

def tan():
    global express
    result = math.tan(eval(express))
    equation.set(result)
    express = ""

def asin():
    global express
    result = math.asin(eval(express))
    equation.set(result)
    express = ""

def acos():
    global express
    result = math.acos(eval(express))
    equation.set(result)
    express = ""

def atan():
    global express
    result = math.atan(eval(express))
    equation.set(result)
    express = ""

if __name__ == "__main__":

    gui = Tk()
    
    gui.title("Practice calculator")
    gui.geometry("840x840")
    equation = StringVar()
    gui.configure(background='blue')
    expressfield = Entry(gui, textvariable=equation)
    expressfield.grid(columnspan=4, ipadx=70)



    button1 = Button(gui, text = "1", fg = 'white', bg = 'green', command = lambda: press(1), height=100, width=100, padx=100, pady=100)
    button1.grid(row = 2, column = 0)

    button2 = Button(gui, text = "2", fg = 'white', bg = 'green', command = lambda: press(2), height=100, width=100, padx=100, pady=100)
    button2.grid(row = 2, column = 1)

    button3 = Button(gui, text = "3", fg = 'white', bg = 'green', command = lambda: press(3), height=100, width=100, padx=100, pady=100)
    button3.grid(row = 2, column = 2)

    button4 = Button(gui, text = "4", fg = 'white', bg = 'green', command = lambda: press(4), height=100, width=100, padx=100, pady=100)
    button4.grid(row = 3, column = 0)

    button5 = Button(gui, text = "5", fg = 'white', bg = 'green', command = lambda: press(5), height=100, width=100, padx=100, pady=100)
    button5.grid(row = 3, column = 1)

    button6 = Button(gui, text = "6", fg = 'white', bg = 'green', command = lambda: press(6), height=100, width=100, padx=100, pady=100)
    button6.grid(row = 3, column = 2)
    
    button7 = Button(gui, text = "7", fg = 'white', bg = 'green', command = lambda: press(7), height=100, width=100, padx=100, pady=100)
    button7.grid(row = 4, column = 0)

    button8 = Button(gui, text = "8", fg = 'white', bg = 'green', command = lambda: press(8), height=100, width=100, padx=100, pady=100)
    button8.grid(row = 4, column = 1)
    
    button9 = Button(gui, text = "9", fg = 'white', bg = 'green', command = lambda: press(9), height=100, width=100, padx=100, pady=100)
    button9.grid(row = 4, column = 2)

    button0 = Button(gui, text = "0", fg = 'white', bg = 'green', command = lambda: press(0), height=100, width=100, padx=100, pady=100)
    button0.grid(row = 5, column = 0)
    
    sin1 = Button(gui, text = "sin", fg = 'white', bg = 'green', command = sin, height=100, width=100, padx=100, pady=100)
    sin1.grid(row = 2, column = 3)

    plus = Button(gui, text = "+", fg = 'white', bg = 'green', command = lambda: press("+"), height=100, width=100, padx=100, pady=100)
    plus.grid(row = 2, column = 4)

    cos1 = Button(gui, text = "cos", fg = 'white', bg = 'green', command = cos, height=100, width=100, padx=100, pady=100)
    cos1.grid(row = 3, column = 3)

    minus = Button(gui, text = "-", fg = 'white', bg = 'green', command = lambda: press("-"), height=100, width=100, padx=100, pady=100)
    minus.grid(row = 3, column = 4)

    tan1 = Button(gui, text = "tan", fg = 'white', bg = 'green', command = tan, height=100, width=100, padx=100, pady=100)
    tan1.grid(row = 4, column = 3)

    multiply = Button(gui, text = "x", fg = 'white', bg = 'green', command = lambda: press("*"), height=100, width=100, padx=100, pady=100)
    multiply.grid(row = 4, column =4)

    power = Button(gui, text = "Power", fg = 'white', bg = 'green', command = lambda:press("**"), height=100, width=100, padx=100, pady=100)
    power.grid(row =5, column = 3)

    divide = Button(gui, text = "/", fg = 'white', bg = 'green', command = lambda: press("/"), height=100, width=100, padx=100, pady=100)
    divide.grid(row =5, column = 4)

    equal = Button(gui, text = "=", fg = 'white', bg = 'green', command = equalpress, height=100, width=100, padx=100, pady=100)
    equal.grid(row= 5, column = 2)
    
    clear1 = Button(gui, text = "Clear", fg = 'white', bg = 'green', command = clear, height=100, width=100, padx=100, pady=100)
    clear1.grid(row =5, column = 1)

    decim = Button(gui, text = ".", fg = 'white', bg = 'green', command = lambda: press("."), height=100, width=100, padx=100, pady=100)
    decim.grid(row = 6, column = 0)


    log = Button(gui, text = "ln", fg = 'white', bg = 'green', command = log, height=100, width=100, padx=100, pady=100)
    log.grid(row = 6, column = 1)
    
    arcsin = Button(gui, text = "arcsin", fg = 'white', bg = 'green', command = asin, height=100, width=100, padx=100, pady=100)
    arcsin.grid(row = 6, column = 2)

    arccos = Button(gui, text = "arccos", fg = 'white', bg = 'green', command = acos, height=100, width=100, padx=100, pady=100)
    arccos.grid(row = 6, column = 3)

    arctan = Button(gui, text = "arctan", fg = 'white', bg = 'green', command = atan, height=100, width=100, padx=100, pady=100)
    arctan.grid(row = 6, column = 4)

    gui.mainloop()