from tkinter import *

window = Tk()

window.title("+-/x") # title bar
window.configure(background='gray')

window.geometry('200x250') # resized window

lbl = Label(window, text="Calculator", font=("Arial Bold", 30)) # text in program
lbl.configure(background="black") # Making the text colour fit

lbl.grid(column=0, row=0) # where calculator shows
lbl.configure(background="gray")
lbl.grid(column=0, row=1) # where the text will be
x = Entry(window,width=30) # adding a text entry box, width 30
x.grid(column=0, row=3) # setting to column 
        
def zero():
    x.insert("end",0) # number buttons all just enter a number

def one():
    x.insert("end",1)

def two():
    x.insert("end",2)

def three():
    x.insert("end",3)

def four():
    x.insert("end",4)

def five():
    x.insert("end",5)

def six():
    x.insert("end",6)

def seven():
    x.insert("end",7)

def eight():
    x.insert("end",8)

def nine():
    x.insert("end",9)

def plus():
    x.insert("end"," + ") # plus

def minus():
    x.insert("end"," - ") # minus

def divide():
    x.insert("end"," / ") # divide

def times():
    x.insert("end"," * ") # multiply

def equal():
    try:
        p = x.get()
        p = str(p)
        x.delete(0, "end") # delete text for result
        p = eval(p)
        p = str(p)
        x.insert(0,p) # inster result
    except: # error handling, anything that would usually cause an error should get picked up
        x.delete(0,"end")
        x.insert(0,"Does Not Compute")
    
def clear():
    x.delete(0, "end") # clear all
    
def dot():
    x.insert("end",".") # decimal place
    
def pi():
    x.insert("end","3.14159265359") # call pi


btn0 = Button(window, text="  0  ", bg="white", fg="black",command=zero) # all buttons with relevant assignment
btn1 = Button(window, text="  1  ", bg="white", fg="black",command=one)
btn2 = Button(window, text="  2  ", bg="white", fg="black",command=two)
btn3 = Button(window, text="  3  ", bg="white", fg="black",command=three)
btn4 = Button(window, text="  4  ", bg="white", fg="black",command=four)
btn5 = Button(window, text="  5  ", bg="white", fg="black",command=five)
btn6 = Button(window, text="  6  ", bg="white", fg="black",command=six)
btn7 = Button(window, text="  7  ", bg="white", fg="black",command=seven)
btn8 = Button(window, text="  8  ", bg="white", fg="black",command=eight)
btn9 = Button(window, text="  9  ", bg="white", fg="black",command=nine)
btn10 = Button(window, text="  +  ", bg="white", fg="black",command=plus)
btn11 = Button(window, text="  -  ", bg="white", fg="black",command=minus)
btn12 = Button(window, text="  x  ", bg="white", fg="black",command=times)
btn13 = Button(window, text="  /  ", bg="white", fg="black",command=divide)
btn14 = Button(window, text="  =  ", bg="green", fg="black",command=equal)
btn15 = Button(window, text=" C ", bg="red", fg="black",command=clear)
btn16 = Button(window, text="  .  ", bg="white", fg="black",command=dot)
btn17 = Button(window, text=" π ", bg="white", fg="black",command=pi)

btn0.place(x=40, y=190) # placing buttons in a nice grid
btn1.place(x=10, y=100)
btn2.place(x=40, y=100)
btn3.place(x=70, y=100)
btn4.place(x=10, y=130)
btn5.place(x=40, y=130)
btn6.place(x=70, y=130)
btn7.place(x=10, y=160)
btn8.place(x=40, y=160)
btn9.place(x=70, y=160)
btn10.place(x=120,y=100)
btn11.place(x=152,y=100)
btn12.place(x=120,y=130)
btn13.place(x=152,y=130)
btn14.place(x=150,y=160)
btn15.place(x=10,y=190)
btn16.place(x=73,y=190)
btn17.place(x=120,y=160)

window.mainloop()
