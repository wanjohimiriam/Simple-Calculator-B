from tkinter import *
home = Tk()
home.geometry("380x500")

text_input=StringVar()
operator=""

f1=Frame(home,width=0, height=0, relief=SUNKEN)
f1.pack(side=LEFT)
f2=Frame(home, width=0, height=0, relief=SUNKEN)
f2.pack(side=LEFT)

def btnclick(numbers):
    global operator
    operator+=str(numbers)
    text_input.set(operator)

def btncleardisplay():
    global operator
    operator=""
    text_input.set("")

def btnequals():
    global operator
    sumup=str(eval(operator))
    operator=""
    text_input.set(sumup)

txtDisplay=Entry(f2, font=("arial", 20, "bold"), bd=30, insertwidth=4, bg="powder blue", justify="right",textvariable=text_input)
txtDisplay.grid(columnspan=5)

btn3 = Button(f2, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="3", bg="powder blue", command=lambda:btnclick(3)).grid(row=1, column=3)
btn2 = Button(f2, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="2", bg="powder blue", command=lambda:btnclick(2)).grid(row=1, column=2)
btn1 = Button(f2, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="1", bg="powder blue", command=lambda:btnclick(1)).grid(row=1, column=1)

btn6 = Button(f2, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="6", bg="powder blue", command=lambda:btnclick(6)).grid(row=2, column=3)
btn5 = Button(f2, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="5", bg="powder blue", command=lambda:btnclick(5)).grid(row=2, column=2)
btn4 = Button(f2, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="4", bg="powder blue", command=lambda:btnclick(4)).grid(row=2, column=1)

btn7 = Button(f2, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="7", bg="powder blue", command=lambda:btnclick(7)).grid(row=3, column=1)
btn8 = Button(f2, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="8", bg="powder blue", command=lambda:btnclick(8)).grid(row=3, column=2)
btn9 = Button(f2, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="9", bg="powder blue", command=lambda:btnclick(9)).grid(row=3, column=3)

btnpls = Button(f2, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="+", bg="powder blue", command=lambda:btnclick("+")).grid(row=1, column=4)
btnmns = Button(f2, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="-", bg="powder blue", command=lambda:btnclick("-")).grid(row=2, column=4)
btnmult = Button(f2, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="x", bg="powder blue", command=lambda:btnclick("x")).grid(row=3, column=4)
btdiv = Button(f2, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="/", bg="powder blue", command=lambda:btnclick("/")).grid(row=4, column=4)

btn0 = Button(f2, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="0", bg="powder blue", command=lambda:btnclick(0)).grid(row=4, column=1)
btnclear= Button(f2, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="c", bg="powder blue", command=btncleardisplay).grid(row=4, column=2)
btneqls = Button(f2, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="=", bg="powder blue", command=btnequals).grid(row=4, column=3)


home.mainloop()