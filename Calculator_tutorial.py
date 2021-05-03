# Simple Calculator
# By Sreekanth
# python 3.8 Using Vscode
# Windows
# Topic : tkinker, grid gemometry manager, eval, try/except, lambda

import tkinter

#Create defination

def add():
    pass

# Create GUI
root = tkinter.Tk()
root.title("Calculator")

label_result = tkinter.Label(root, text="")
label_result.grid(row=0, cloumn=0)

button_1 = tkinter.Button(root,test="1" ,command=add())
button_1.grid(row=1, column=0)

button_2 = tkinter.Button(root,test="2" ,command=add())
button_2.grid(row=1, column=1)

button_3 = tkinter.Button(root,test="3" ,command=add())
button_3.grid(row=1, column=2)

button_Divide = tkinter.Button(root,test="/" ,command=add())
button_Divide.grid(row=1, column=3)



root.mainloop()
