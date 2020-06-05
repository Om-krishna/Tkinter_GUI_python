# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 20:40:13 2020

@author: Om Krishna

"""

from tkinter import*
root = Tk()


def leftClick(event):
    print("Left")
    
def middleClick(event):
    print("Middle")
    
def rightClick(event):
    print("Right")
    
frame = Frame(root, width=300, height= 250)
frame.bind("<Button-1>",leftClick)
frame.bind("<Button-2>",middleClick)
frame.bind("<Button-3>",rightClick)
frame.pack()

root.mainloop()


