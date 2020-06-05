# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 20:09:53 2020

@author: Om Krishna
"""


from tkinter import*
root = Tk()




one = Label(root, text="One", bg="red", fg="white")
one.pack()

two = Label(root, text="Two", bg="yellow", fg="black")
two.pack(fill=X)

three = Label(root, text="Three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y)

root.mainloop()

