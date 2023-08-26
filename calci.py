from tkinter import *

#event handlers

def btn__digit(digit):
    ini_value=result["text"]                    #extract current value of the label
    fin_value=ini_value+str(digit)
    result.config(text=fin_value)

def clear_one():
    ini_value=result["text"]
    fin_val=ini_value[:-1]
    result.config(text=fin_val)

def all_clear():
    result.config(text="")



def oper(ot):
    global first,operator
    first=int(result["text"])
    operator=ot
    result.config(text="")

def eq():
    global first,operator,second
    second=int(result["text"])
    print(first)
    if operator=="+":
        result.config(text=str(first+second))
    elif operator=="-":
        result.config(text=str(first-second))
    elif operator=="/":
        result.config(text=str(first/second))
    elif operator=="x":
        result.config(text=str(first*second))
    elif operator=="%":
        result.config(text=str(first%second))


root=Tk()

#UI
root.title(" Calculator")
root.iconbitmap("./images/calculator.ico")
root.geometry("400x600")
root.maxsize(400,600)
root.configure(background="black")


result=Label(root,text="",width=21,height=2,bg="black",fg="white")
result.grid(row=0,column=0,columnspan=4,pady=(125,0),sticky="w")            #sticky force our text to start from west(w) or east(e)
result.config(font=("verdana",20,"bold"))

btn_c=Button(root,text="C",bg="#d1dbe4",fg="black",width=8,height=3,font=("verdana",14),command=clear_one)
btn_c.grid(row=1,column=0)
btn_c["border"]=0

btn_all_clr=Button(root,text="AC",bg="#d1dbe4",fg="black",width=8,height=3,font=("verdana",14),command=all_clear)
btn_all_clr.grid(row=1,column=1)
btn_all_clr["border"]=0

btn_mod=Button(root,text="%",bg="#d1dbe4",fg="black",width=8,height=3,font=("verdana",14),command=lambda:oper("%"))
btn_mod.grid(row=1,column=2)
btn_mod["border"]=0

btn_div=Button(root,text="/",bg="orange",fg="black",width=8,height=3,font=("verdana",14),command=lambda:oper("/"))
btn_div.grid(row=1,column=3)
btn_div["border"]=0

btn_7=Button(root,text="7",bg="#d1dbe4",fg="black",width=8,height=3,font=("verdana",14),command=lambda:btn__digit(7))       #lambda is used when we write function with() or passing an argument to hold the command until event trigger is not held.
btn_7.grid(row=2,column=0)
btn_7["border"]=0

btn_8=Button(root,text="8",bg="#d1dbe4",fg="black",width=8,height=3,font=("verdana",14),command=lambda:btn__digit(8))
btn_8.grid(row=2,column=1)
btn_8["border"]=0

btn_9=Button(root,text="9",bg="#d1dbe4",fg="black",width=8,height=3,font=("verdana",14),command=lambda:btn__digit(9))
btn_9.grid(row=2,column=2)
btn_9["border"]=0

btn_mul=Button(root,text="x",bg="orange",fg="black",width=8,height=3,font=("verdana",14),command=lambda:oper("x"))
btn_mul.grid(row=2,column=3)
btn_mul["border"]=0



btn_4=Button(root,text="4",bg="#d1dbe4",fg="black",width=8,height=3,font=("verdana",14),command=lambda:btn__digit(4))
btn_4.grid(row=3,column=0)
btn_4["border"]=0

btn_5=Button(root,text="5",bg="#d1dbe4",fg="black",width=8,height=3,font=("verdana",14),command=lambda:btn__digit(5))
btn_5.grid(row=3,column=1)
btn_5["border"]=0

btn_6=Button(root,text="6",bg="#d1dbe4",fg="black",width=8,height=3,font=("verdana",14),command=lambda:btn__digit(6))
btn_6.grid(row=3,column=2)
btn_6["border"]=0

btn_sub=Button(root,text="-",bg="orange",fg="black",width=8,height=3,font=("verdana",14),command=lambda:oper("-"))
btn_sub.grid(row=3,column=3)
btn_sub["border"]=0

btn_1=Button(root,text="1",bg="#d1dbe4",fg="black",width=8,height=3,font=("verdana",14),command=lambda:btn__digit(1))
btn_1.grid(row=4,column=0)
btn_1["border"]=0

btn_2=Button(root,text="2",bg="#d1dbe4",fg="black",width=8,height=3,font=("verdana",14),command=lambda:btn__digit(2))
btn_2.grid(row=4,column=1)
btn_2["border"]=0

btn_3=Button(root,text="3",bg="#d1dbe4",fg="black",width=8,height=3,font=("verdana",14),command=lambda:btn__digit(3))
btn_3.grid(row=4,column=2)
btn_3["border"]=0

btn_add=Button(root,text="+",bg="orange",fg="black",width=8,height=3,font=("verdana",14),command=lambda:oper("+"))
btn_add.grid(row=4,column=3)
btn_add["border"]=0


btn_zero=Button(root,text="0",bg="#d1dbe4",fg="black",width=25,height=3,font=("verdana",14),command=lambda:btn__digit(0))
btn_zero.grid(row=5,column=0,columnspan=3,sticky="w")
btn_zero["border"]=0


btn_equ=Button(root,text="=",bg="orange",fg="black",width=8,height=3,font=("verdana",14),command=eq)
btn_equ.grid(row=5,column=3,sticky="w")
btn_equ["border"]=0


root.mainloop()