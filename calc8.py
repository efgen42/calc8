# -*- coding utf-8 -*-
from func import sum8, dif8, decimalconv
from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.title("calc8")
window.geometry('200x250')

Label(window, text="Число 1:").pack()
e1 = Entry(window)
e1.pack()
Label(window, text="Число 2:").pack()
e2 = Entry(window)
e2.pack()




var=IntVar()
var.set(0)
rad0 = Radiobutton(window, text="+", variable=var, value=0)
rad1 = Radiobutton(window, text="-", variable=var, value=1)
rad2 = Radiobutton(window, text="->10", variable=var, value=2)

rad0.pack()
rad1.pack()
rad2.pack()

e3 = Entry(window)
e3.pack()

def clicked():
    a = e1.get()
    b = e2.get()
    result = a + b

    e3.delete(0,END)
    e3.insert(0, result)

    # Label(window, text=result, font=("Arial Bold", 20)).pack()

Button(window, text="Выполнить", command=clicked).pack()


window.mainloop()
