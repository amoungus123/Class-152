# -*- coding: utf-8 -*-
"""
Created on Wed May  4 21:09:22 2022

@author: pulle
"""

from tkinter import *
root=Tk()
root.title("Multidimensional Arrays")

root.geometry("500x500")
label= Label(root)


array_1d = ["John", "James", "Thomsan"]
print(array_1d[0])

array_2d = [["John", "A"], ["James", "B"], ["Thomson", "C"]]
print(array_2d[0][1])

array_3d = [[["John", "A+", "Excellent"], ["James", "B", "Very Good"], ["Thomson", "C", "Good"]]]
print(array_3d[0][0][2])

def report():
    label["text"] = array_3d[0][1][0] + " got grade " + array_3d[0][1][1] + " and he is doing " + array_3d[0][1][2]
    
btn = Button(root, text= "Show Report", command = report)
btn.place(relx = 0.5, rely = 0.4, anchor = CENTER)

label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()