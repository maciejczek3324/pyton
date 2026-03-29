from tkinter import *

dzialanie = ""

def press(num):
    current = expression_field.get()
    expression_field.delete(0, END)
    expression_field.insert(0, str(current) + str(num))

def button_add():
    firstNumber = expression_field.get()
    global f_num
    global math
    math = "addition"
    f_num = int(firstNumber)
    expression_field.delete(0, END)

def button_subtract():
    firstNumber = expression_field.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(firstNumber)
    expression_field.delete(0, END)

def button_multiply():
    firstNumber = expression_field.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(firstNumber)
    expression_field.delete(0, END)

def button_divide():
    firstNumber = expression_field.get()
    global f_num
    global math
    math = "division"
    f_num = int(firstNumber)
    expression_field.delete(0, END)

def wynik():

    secondNumber = expression_field.get()
    if(secondNumber!="0"):
        expression_field.delete(0, END)

        if math == "addition":
            expression_field.insert(0, f_num + int(secondNumber))

        if math == "subtraction":
            expression_field.insert(0, f_num - int(secondNumber))

        if math == "multiplication":
            expression_field.insert(0, f_num * int(secondNumber))

        if math == "division":
            expression_field.insert(0, f_num / int(secondNumber))

def c():
    global dzialanie
    dzialanie = ""
    wpisane.set("")


window = Tk()

window.configure(background="white")
window.title("Kalkulator")
window.geometry("235x240")

wpisane = StringVar()
expression_field = Entry(window, textvariable=wpisane)
expression_field.grid(columnspan=12, ipadx=45)

jeden = Button(window, text=' 1 ', fg='black', bg='grey', command=lambda: press(1), height=3, width=7)
jeden.grid(row=2, column=0)

dwa = Button(window, text=' 2 ', fg='black', bg='grey', command=lambda: press(2), height=3, width=7)
dwa.grid(row=2, column=1)

trzy = Button(window, text=' 3 ', fg='black', bg='grey', command=lambda: press(3), height=3, width=7)
trzy.grid(row=2, column=2)

cztery = Button(window, text=' 4 ', fg='black', bg='grey', command=lambda: press(4), height=3, width=7)
cztery.grid(row=3, column=0)

piec = Button(window, text=' 5 ', fg='black', bg='grey', command=lambda: press(5), height=3, width=7)
piec.grid(row=3, column=1)

szesc = Button(window, text=' 6 ', fg='black', bg='grey', command=lambda: press(6), height=3, width=7)
szesc.grid(row=3, column=2)

siedem = Button(window, text=' 7 ', fg='black', bg='grey', command=lambda: press(7), height=3, width=7)
siedem.grid(row=4, column=0)

osiem = Button(window, text=' 8 ', fg='black', bg='grey', command=lambda: press(8), height=3, width=7)
osiem.grid(row=4, column=1)

dziewiec = Button(window, text=' 9 ', fg='black', bg='grey', command=lambda: press(9), height=3, width=7)
dziewiec.grid(row=4, column=2)

zero = Button(window, text=' 0 ', fg='black', bg='grey', command=lambda: press(0), height=3, width=7)
zero.grid(row=5, column=0)

plus = Button(window, text=' + ', fg='black', bg='grey', command=lambda: button_add(), height=3, width=7)
plus.grid(row=2, column=3)

minus = Button(window, text=' - ', fg='black', bg='grey', command=lambda: button_subtract(), height=3, width=7)
minus.grid(row=3, column=3)

mnoznik = Button(window, text=' * ', fg='black', bg='grey', command=lambda: button_multiply(), height=3, width=7)
mnoznik.grid(row=4, column=3)

dzielnik = Button(window, text=' / ', fg='black', bg='grey', command=lambda: button_divide(), height=3, width=7)
dzielnik.grid(row=5, column=3)

rownasie = Button(window, text=' = ', fg='black', bg='grey',command=lambda: wynik(),height=3, width=7)
rownasie.grid(row=5, column=2)

C = Button(window, text='C', fg='black', bg='grey', command=c, height=3, width=7)
C.grid(row=5, column=1)

window.mainloop()
