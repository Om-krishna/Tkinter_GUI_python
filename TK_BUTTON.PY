# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 19:57:15 2020

@author: Om Krishna
"""

from tkinter import*
root = Tk()

topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)


button1=Button(topFrame, text="Button1", fg="red")
button2=Button(topFrame, text="Button2", fg="blue")
button3=Button(topFrame, text="Button3", fg="green")
button4=Button(topFrame, text="Button4", fg="purple")


button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)


root.mainloop()
