# -*- coding utf-8 -*-
from func import sum8, dif8, decimalconv
from tkinter import Label, Entry, Tk, Button, END, Radiobutton, IntVar, messagebox

window = Tk() # основное окно
window.title("calc8")
window.geometry('200x250')

Label(window, text="Число 1:").pack() # метод pack размещает элементы друг под другом
e1 = Entry(window)  # поле ввода
e1.pack()
e1.focus()

Label(window, text="Число 2:").pack()
e2 = Entry(window)
e2.pack()

var = IntVar()  # класс-переменная для хран-я состояния переключателя, в виде целого числа
var.set(0)
rad0 = Radiobutton(window, text="+", variable=var, value=0)
rad1 = Radiobutton(window, text="-", variable=var, value=1)
rad2 = Radiobutton(window, text="->10", variable=var, value=2)
rad0.pack()
rad1.pack()
rad2.pack()

e3 = Entry(window)
e3.pack()


def err1(): # функция, применяемая при обработке исключения
    messagebox.showinfo('Ошибка', 'Необходимо указывать положительное восьмеричное число!')
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e1.focus()


def clicked(): # функция для кнопки "Выполнить"
    a = e1.get() if e1.get() else '0'  # если одно из чисел пусто при сложении\вычитании -  \
    b = e2.get() if e2.get() else '0'  # рез-т= наличиествующее число
    # print(e1.get(),e2.get())
    try:
        if not any([int(x) <= 7 for x in a]):   # число восьмеричное ?
            err1()  # если не удасться выполнить int(x) - сработает исключение ValueError
        else:
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
    except ValueError:
        err1()


Button(window, text="Выполнить", command=clicked).pack()
window.mainloop()