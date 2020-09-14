# -*- coding utf-8 -*-
from func import sum8, dif8, decimalconv
from tkinter import Label, Entry, Tk, Button, END, Radiobutton, IntVar

window = Tk()
window.title("calc8")
window.geometry('200x250')

Label(window, text="Число 1:").pack()
e1 = Entry(window)
e1.pack()
e1.focus()

Label(window, text="Число 2:").pack()
e2 = Entry(window)
e2.pack()
# e2 = Entry(window,state='disabled')
# e2.pack()

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

    if var.get() == 0:
        result = sum8(a, b)
    elif var.get() == 1:
        result = dif8(a, b)
    elif var.get() == 2:
        result = decimalconv(a)

    if var.get() == 2:
        e2.delete(0, END)

    e3.delete(0, END)
    e3.insert(0, result)
    e1.focus()

Button(window, text="Выполнить", command=clicked).pack()

window.mainloop()

###
##  Проверки:
### 1. Если одино из чисел пусто при сложении\вычитании - рез-т= наличиествующее число
### 2. Если не цифра или не восьмеричное число - выкидываем ошибку и очищаем поля ввода и рез-та(?)
###

###