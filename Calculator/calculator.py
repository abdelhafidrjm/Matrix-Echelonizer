from tkinter import *
from math import pi

# Window Initialisation
root = Tk()
root.title("Calculator")
root.geometry("650x450")
root.config(bg = "#000")
root.resizable(False, False)

# Initialisation
Numbers = []
Number = 0
ops = []
op = ""
countD = 0

# subFunction
def refresh(n):
    if n == pi : 
        n = "π" 
    elif n == ".":
        n = "."
    elif n == 0:
        n = ""
    else:
        n = int(n) if n == round(n) else n
    
    textbox.config(text = n)
    
def clear(n):
    global Number, op, Numbers, ops
    Number = n
    Numbers.clear()
    op = ""
    ops.clear()


def backspace():
    global Number
    Number = (Number - Number % 10) / 10
    refresh(Number)

def delete():
    global Number, Numbers, op, ops
    clear(0)
    refresh(Number)
    
    
# Calculator functions
def iN(num):
    global Number
    if num == pi:
        Number = num
    else:
        Number = Number * 10 + num
    refresh(Number)
insertNumber = iN
    
def iDe(num):
    global Number, countD
    countD += 1
    if num == pi:
        Number = pi
    else:    
        Number += num / pow(10, countD)
    refresh(Number)


def operationSaver(ope):
    global ops, op, Numbers, Number, insertNumber
    if ope == ".":
        Number = float(Number/1)
        insertNumber = iDe
        refresh(ops[i])
    elif ope != "=" : 
        op = ope
        ops.append(op)
        Numbers.append(Number)
        Number = 0
        refresh(Number)
    else:
        Numbers.append(Number)
        result = Numbers[0]
        for i in range(len(ops)):
            insertNumber = iN
            match ops[i]:
                case "+":
                    result += Numbers[i+1]
                case "-":
                    result -= Numbers[i+1]
                case "x":
                    result *= Numbers[i+1]    
                case "/":
                    try:
                        result /= Numbers[i+1]
                    except ZeroDivisionError:
                        textbox.config(text = "you can't divide by 0")
                        clear(0)
                        return
        refresh(result)
        clear(result)
        refresh(Number)
        
        
# Resault
textbox = Label(fg = "#FCFCFC", bg = "#510c23",width = 350, font = ("Ink Free", 20), relief = SOLID, borderwidth = 10)
textbox.pack()


theGrid = Frame(root)

# Numbers
buttonnumber1 = Button(theGrid, height = 2, text = 1,   font = ("Ink Free", 15, "bold"), command = lambda : insertNumber(1),    bg = "#9A3131", width = 8, borderwidth=5, relief= RAISED)
buttonnumber2 = Button(theGrid, height = 2, text = 2,   font = ("Ink Free", 15, "bold"), command = lambda : insertNumber(2),    bg = "#9A3131", width = 8, borderwidth=5, relief= RAISED)
buttonnumber3 = Button(theGrid, height = 2, text = 3,   font = ("Ink Free", 15, "bold"), command = lambda : insertNumber(3),    bg = "#9A3131", width = 8, borderwidth=5, relief= RAISED)
buttonnumber4 = Button(theGrid, height = 2, text = 4,   font = ("Ink Free", 15, "bold"), command = lambda : insertNumber(4),    bg = "#9A3131", width = 8, borderwidth=5, relief= RAISED)
buttonnumber5 = Button(theGrid, height = 2, text = 5,   font = ("Ink Free", 15, "bold"), command = lambda : insertNumber(5),    bg = "#9A3131", width = 8, borderwidth=5, relief= RAISED)
buttonnumber6 = Button(theGrid, height = 2, text = 6,   font = ("Ink Free", 15, "bold"), command = lambda : insertNumber(6),    bg = "#9A3131", width = 8, borderwidth=5, relief= RAISED)
buttonnumber7 = Button(theGrid, height = 2, text = 7,   font = ("Ink Free", 15, "bold"), command = lambda : insertNumber(7),    bg = "#9A3131", width = 8, borderwidth=5, relief= RAISED)
buttonnumber8 = Button(theGrid, height = 2, text = 8,   font = ("Ink Free", 15, "bold"), command = lambda : insertNumber(8),    bg = "#9A3131", width = 8, borderwidth=5, relief= RAISED)
buttonnumber9 = Button(theGrid, height = 2, text = 9,   font = ("Ink Free", 15, "bold"), command = lambda : insertNumber(9),    bg = "#9A3131", width = 8, borderwidth=5, relief= RAISED)
buttonnumber0 = Button(theGrid, height = 2, text = 0,   font = ("Ink Free", 15, "bold"), command = lambda : insertNumber(0),    bg = "#9A3131", width = 8, borderwidth=5, relief= RAISED)
buttonnumberp = Button(theGrid, height = 2, text = "π", font = ("Ink Free", 15, "bold"), command = lambda : insertNumber(pi),   bg = "#9A3131", width = 8, borderwidth=5, relief= RAISED)
buttonnumberd = Button(theGrid, height = 2, text = ".", font = ("Ink Free", 15, "bold"), command = lambda : operationSaver("."),  bg = "#9A3131", width = 8, borderwidth=5, relief= RAISED)

# Arethmetic Operations
buttonpls = Button(theGrid, height = 2, bg = "#2427df", fg = "#fff",borderwidth = 5, relief = RAISED, text = "+", font = ("Ink Free", 15, "bold"), command = lambda : operationSaver("+"), width = 10)
buttonmin = Button(theGrid, height = 2, bg = "#2427df", fg = "#fff",borderwidth = 5, relief = RAISED, text = "-", font = ("Ink Free", 15, "bold"), command = lambda : operationSaver("-"), width = 10)
buttonmul = Button(theGrid, height = 2, bg = "#2427df", fg = "#fff",borderwidth = 5, relief = RAISED, text = "x", font = ("Ink Free", 15, "bold"), command = lambda : operationSaver("x"), width = 10)
buttondiv = Button(theGrid, height = 2, bg = "#2427df", fg = "#fff",borderwidth = 5, relief = RAISED, text = "/", font = ("Ink Free", 15, "bold"), command = lambda : operationSaver("/"), width = 10)
buttoneql = Button(theGrid, height = 2, bg = "#2427df", fg = "#fff",borderwidth = 5, relief = RAISED, text = "=", font = ("Ink Free", 15, "bold"), command = lambda : operationSaver("="), width = 10)

# Functionalities
buttonbackspace = Button(theGrid,   height = 2, width = 11,bg = "#2427df", fg = "#fff",borderwidth = 5, relief = RAISED, text = "Backspace", font = ("Ink Free", 15), command = backspace)
buttondelete = Button(theGrid,      height = 2, width = 11,bg = "#2427df", fg = "#fff",borderwidth = 5, relief = RAISED, text = "Delete", font = ("Ink Free", 15), command = delete)

buttonclose = Button(theGrid,text="Quit", font = ("Ink Free", 15), command=root.destroy)

# Displaying the buttons
buttonnumber1.grid(row = 0, column = 0,  padx = 1, pady = 1)
buttonnumber2.grid(row = 0, column = 1,  padx = 1, pady = 1)
buttonnumber3.grid(row = 0, column = 2,  padx = 1, pady = 1)
buttonnumber4.grid(row = 1, column = 0,  padx = 1, pady = 1)
buttonnumber5.grid(row = 1, column = 1,  padx = 1, pady = 1)
buttonnumber6.grid(row = 1, column = 2,  padx = 1, pady = 1)
buttonnumber7.grid(row = 2, column = 0,  padx = 1, pady = 1)
buttonnumber8.grid(row = 2, column = 1,  padx = 1, pady = 1)
buttonnumber9.grid(row = 2, column = 2,  padx = 1, pady = 1)
buttonnumber0.grid(row = 3, column = 1,  padx = 1, pady = 1)
buttonnumberp.grid(row = 3, column = 2,  padx = 1, pady = 1)
buttonnumberd.grid(row = 3, column = 0,  padx = 1, pady = 1)

buttonmin.grid(row = 1, column = 4,  padx = 1, pady = 1, sticky = "w")
buttonpls.grid(row = 1, column = 3,  padx = 1, pady = 1, sticky = "e")
buttonmul.grid(row = 2, column = 3,  padx = 1, pady = 1, sticky = "e")
buttondiv.grid(row = 2, column = 4,  padx = 1, pady = 1, sticky = "w")
buttoneql.grid(row = 3, column = 3,  padx = 1, pady = 1, sticky = "e")

buttonbackspace.grid(row = 0, column = 3,  padx = 1, pady = 1, sticky="e")
buttondelete.grid(row = 0, column = 4,  padx = 1, pady = 1, sticky = "w")
buttonclose.grid(row = 4, column = 4, sticky = "es")

theGrid.config(relief = SOLID, borderwidth = 10, padx = 10, pady = 10, bg = "#000", height = 300)
theGrid.pack(fill = "x")


root.mainloop()
