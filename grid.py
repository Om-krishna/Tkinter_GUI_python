# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 20:20:04 2020

@author: Om krishna
"""


from tkinter import*
root = Tk()

Label_1 = Label(root, text="Name")
Label_2 = Label(root, text="Password")

entry_1=Entry(root)
entry_2=Entry(root)


Label_1.grid(row=0, sticky=E)
Label_2.grid(row=1, sticky=E)

entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

c= Checkbutton(root, text="Keep me in logged in")
c.grid(columnspan=2)

root.mainloop()
