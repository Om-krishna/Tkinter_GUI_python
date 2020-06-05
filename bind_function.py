# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 20:28:18 2020

@author: Om Krishna
"""


from tkinter import*
root = Tk()

def printName(event):
    print("Hello my Name is Turners")
    
button_1=Button(root, text="Print my name")    
button_1.bind("<Button-1>",printName)
button_1.pack()

root.mainloop()
