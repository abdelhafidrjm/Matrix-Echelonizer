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
    else:
        n = int(n) if n == round(n) else n
    
    textbox.config(text = n)
    
def clear(n):
    global Number, op, Numbers, ops, insertNumber
    Numbers.clear()
    Number = n
    ops.clear()
    insertNumber = iN
    op = ""


def backspace():
    global Number
    if insertNumber == iN:
        if Number < 0:
            Number *= -1 
            Number = (Number - Number % 10) / 10
            Number *= -1
        else:
            Number = (Number - Number % 10) / 10
    else:
        count = 0
        while Number != round(Number):
            count += 1
            Number *= 10
        Number = (Number - Number % 10) / 10
        Number /= 10 ** (count-1)
    refresh(Number)

def delete():
    global Number, Numbers, op, ops
    clear(0)
    refresh(Number)
    
    
# Calculator functions
def iN(num):
    global Number, Numbers
    if Number == pi or num == pi:
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
    global ops, op, Numbers, Number, insertNumber, countD
    if ope == ".":
        countD = 0
        Number = float(Number)
        insertNumber = iDe
        refresh(ope)
    elif ope != "=" : 
        insertNumber = iN
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
                    # if len(Numbers) != len(ops):
                    result -= Numbers[i+1]
                    # else:
                    #     result *= - Numbers[i+1]
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
k = 0
for i in [0,1,2,3]:
    for j in [0, 1, 2]:
        k += 1
        if   k < 10  : Button(theGrid, height = 2, text = k,   font = ("Ink Free", 15, "bold"), command = lambda k = k: insertNumber(k),    bg = "#9A3131", width = 8, borderwidth=5, relief= RAISED).grid(row = i, column = j,  padx = 1, pady = 1)
        elif k == 10 : Button(theGrid, height = 2, text = ".", font = ("Ink Free", 15, "bold"), command = lambda : operationSaver("."),     bg = "#9A3131", width = 8, borderwidth=5, relief= RAISED).grid(row = i, column = j,  padx = 1, pady = 1)
        elif k == 11 : Button(theGrid, height = 2, text = 0,   font = ("Ink Free", 15, "bold"), command = lambda : insertNumber(0),         bg = "#9A3131", width = 8, borderwidth=5, relief= RAISED).grid(row = i, column = j,  padx = 1, pady = 1)
        elif k == 12 : Button(theGrid, height = 2, text = "π", font = ("Ink Free", 15, "bold"), command = lambda : insertNumber(pi),        bg = "#9A3131", width = 8, borderwidth=5, relief= RAISED).grid(row = i, column = j,  padx = 1, pady = 1)

# Arethmetic Operations
for i, j, l in zip(["+", "-", "x", "/", "="], [1, 1, 2, 2, 3], [3, 4, 3, 4, 3]):
    Button(theGrid, height = 2, bg = "#2427df", fg = "#fff",borderwidth = 5, relief = RAISED, text = i, font = ("Ink Free", 15, "bold"), command = lambda k = i: operationSaver(k), width = 10).grid(row = j, column = l,  padx = 1, pady = 1)

# Functionalities
buttonbackspace = Button(theGrid,   height = 2, width = 11,bg = "#2427df", fg = "#fff",borderwidth = 5, relief = RAISED, text = "Backspace", font = ("Ink Free", 15), command = backspace)
buttondelete = Button(theGrid,      height = 2, width = 11,bg = "#2427df", fg = "#fff",borderwidth = 5, relief = RAISED, text = "Delete", font = ("Ink Free", 15), command = delete)
buttonclose = Button(theGrid,text="Quit", font = ("Ink Free", 15), command=root.destroy)

buttonbackspace.grid(row = 0, column = 3,  padx = 1, pady = 1, sticky="e")
buttondelete.grid(row = 0, column = 4,  padx = 1, pady = 1, sticky = "w")
buttonclose.grid(row = 4, column = 4, sticky = "es")

theGrid.config(relief = SOLID, borderwidth = 10, padx = 10, pady = 10, bg = "#000")
theGrid.pack(fill = "x")


root.mainloop()
