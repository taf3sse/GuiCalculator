from tkinter import * 
import tkinter.messagebox as tmsg
import math 

root = Tk()

root.minsize(520,340)
root.maxsize(520,340)

root.title("Scientific Calculator")
root.wm_iconbitmap("calculator.ico")


sc = StringVar()
sc = Entry(root,width=31,textvariable=sc,relief=SUNKEN,font="cosmicsansms 20")
sc.grid(row=0,column=0,columnspan=10,padx=11,pady=12) 

def helper():
    help = '''1. For the following functions please enter the number first and then press the required function:
sin, cos, tan, log, ln 

2. For multiplication with float numbers, say 5*0.4 multiply like 5*4/10'''
    tmsg.showinfo("Help",help)

f


mainmenu = Menu(root)

submenu = Menu(mainmenu,tearoff=0)
submenu.add_command(label="General",command=helper)
mainmenu.add_cascade(label="Help",menu=submenu)
mainmenu.add_command(label="Exit",command=quit)

root.config(menu=mainmenu)

def sciCal(event):
    key = event.widget
    text = key['text']
    val = sc.get()
    sc.delete(0,END)
    if text=="sin":
        sc.insert(val,math.sin(float(val)))
    elif text=="cos":
        sc.insert(0,math.cos(float(val)))  
    elif text=="tan":
        sc.insert(0,math.tan(float(val)))
    elif text=="log":
        if(float(val)<=0.00):
            tmsg.showerror( 'Error','Error, DNE' )
        else:
            sc.insert(0,math.log10(float(val)))
    elif text=="ln":
        if(float(val)<=0.00):
            tmsg.showerror( 'Error','Error, DNE' )
        else:
            sc.insert(0,math.log(float(val)))

    

def click(event):
    key = event.widget
    text = key['text']
    oldValue = sc.get()
    sc.delete(0,END)
    newValue = oldValue + text
    sc.insert(0,newValue)
              

def clr(event):
    sc.delete(0,END)
    

def backspace(event):
    entered = sc.get()
    length = len(entered)-1
    sc.delete(length,END)
    

def calculate(event):
    answer = sc.get()
    if "^" in answer:
        answer = answer.replace("^","**")
    answer = eval(answer)
    sc.delete(0,END)
    sc.insert(0,answer)
    
    


class Calculator:
    def __init__(self,txt,r,c,funcName,color="blue"):
        self.var = Button(root,text=txt,padx=3,pady=5,fg="black",bg=color,width=10,font="cosmicsansms 12")
        self.var.bind("<Button-1>",funcName)
        self.var.grid(row=r,column=c)


btnSin = Calculator("sin",1,0,sciCal,"black")

btnCos = Calculator("cos",1,1,sciCal,"grey")

btnTan = Calculator("tan",1,2,sciCal,"grey")

btnLog = Calculator("log",2,0,sciCal)

btnLn = Calculator("ln",2,1,sciCal)

btnOB = Calculator("(",2,2,click)

btnCB = Calculator(")",2,3,click)

btnDiv = Calculator("/",2,4,click,"#DBA800")

btnMul = Calculator("*",4,4,click,"#DBA800")

btnSub = Calculator("-",3,4,click,"#DBA800")

btnAdd = Calculator("+",5,4,click,"#DBA800")

btn19 = Calculator("%",3,0,click,"#DBA800")

btn20 = Calculator("9",3,3,click)

btn21 = Calculator("8",3,2,click)

btn22 = Calculator("7",3,1,click)

btn23 = Calculator("6",4,3,click)

btn24 = Calculator("5",4,2,click)

btn25 = Calculator("4",4,1,click)

btn26 = Calculator("1",5,1,click)

btn27 = Calculator("2",5,2,click)

btn28 = Calculator("3",5,3,click)


btn30 = Calculator("C",1,4,clr,"red")

btn31 = Calculator("⌦",1,3,backspace,"red")

btn32 = Calculator("0",6,2,click)

btn33 = Calculator(".",6,3,click)

btn34 = Calculator("=",6,4,calculate)

root.mainloop()
