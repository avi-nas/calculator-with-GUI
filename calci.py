from tkinter import *
import PIL.Image
from PIL import ImageTk

global operator
operator = ""
def opration(number):
    global operator
    operator= operator+str(number)
    txt_Input.set(operator)
def clr():
    global operator
    operator=""
    txt_Input.set("")
def eva():
    global operator
    a=eval(operator)  
    operator = str(a)
    txt_Input.set(str(a))
root = Tk()
root.configure(bg="gray")
pho = PIL.Image.open("number-1.png")
pho = pho.resize((60,60))
#pho.show()
photo=ImageTk.PhotoImage(pho)
root.iconphoto(False,photo)



root.title("MY CALCII")
root.geometry("360x440")
#root.maxsize(360,440)
#root.minsize(360,370)
txt_Input=StringVar()

enrty = Entry(root,font="arial 20 bold",textvariable=txt_Input, bd=30,insertwidth=4,bg="sky blue",justify='right').grid(columnspan=4)

btn7=Button(root,text="7",font="arial 20 bold",padx=16,bg='red',command=lambda:opration(7)).grid(row=2,column=0)
btn8=Button(text="8",font="arial 20 bold",padx=16,borderwidth=0,command=lambda:opration(8)).grid(row=2,column=1)
btn9=Button(text="9",font="arial 20 bold",padx=16,bg='red',command=lambda:opration(9)).grid(row=2,column=2)
btn4=Button(text="4",font="arial 20 bold",padx=16,bg='red',command=lambda:opration(4)).grid(row=3,column=0)
btn5=Button(text="5",font="arial 20 bold",padx=16,bg='red',command=lambda:opration(5)).grid(row=3,column=1)
btn6=Button(text="6",font="arial 20 bold",padx=16,bg='red',command=lambda:opration(6)).grid(row=3,column=2)
btn1=Button(text="1",font="arial 20 bold",padx=16,bg='red',command=lambda:opration(1)).grid(row=4,column=0)
btn2=Button(text="2",font="arial 20 bold",padx=16,bg='red',command=lambda:opration(2)).grid(row=4,column=1)
btn3=Button(text="3",font="arial 20 bold",padx=16,bg='red',command=lambda:opration(3)).grid(row=4,column=2)
btn_clr=Button(text="C",font="arial 20 bold",padx=16,bd=8,command=clr).grid(row=5,column=0)
btn0=Button(text="0",font="arial 20 bold",padx=16,bg='red',command=lambda:opration(0)).grid(row=5,column=1)
btn_dot=Button(text=".",font="arial 20 bold",padx=16,bd=8,command=lambda:opration('.')).grid(row=5,column=2)

btn_mul=Button(text="x",font="arial 20 bold",padx=16,bd=8,command=lambda:opration('*')).grid(row=2,column=3)
btn_sub=Button(text="-",font="arial 20 bold",padx=18,bd=8,command=lambda:opration('-')).grid(row=3,column=3)
btn_add=Button(text="+",font="arial 20 bold",padx=15,bd=8,command=lambda:opration('+')).grid(row=4,column=3)

btn_mul=Button(text="/",font="arial 20 bold",padx=16,bd=8,command=lambda:opration('/')).grid(row=1,column=3)
btn_mul=Button(text="mode",font="arial 20",padx=0,borderwidth=0,command=lambda:opration('%')).grid(row=1,column=2)

btn_eql=Button(text="=",font="arial 20 bold",padx=15,bd=8,command=eva).grid(row=5,column=3)

root.mainloop()