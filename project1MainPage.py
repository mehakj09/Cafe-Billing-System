import pandas as pd
from tkinter import *
from PIL import ImageTk,Image
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import sys
import os
rs = Tk()
def BSC():
    os.system("python project2BillingSystem.py")
def ABC():
    os.system("python project3Graph.py")
def CBA():
    os.system("python project4view.py")
rs.title('Main Page')
rs.geometry('940x788')
photo1=ImageTk.PhotoImage(file =r'C:\Users\Mehak\Desktop\Python\Cafe Billing Application\pic3.png')
lbl1=Label(rs,image = photo1,)
lbl1.place(x=0,y=0)
BS=Button(rs, text="Billing system",padx=40,pady=7, bd=10 ,fg="white",font=('Copper Black' ,16,'bold italic'),width=10, bg="grey26" ,command=BSC) 
BS.place(x=590, y=500)
CS=Button(rs, text="Graph",padx=40,pady=7, bd=10 ,fg="white",font=('Copper Black' ,16,'bold italic'),width=10, bg="grey26",command=ABC) 
CS.place(x=590, y=580)
DS=Button(rs, text="Billing Summary ",padx=40,pady=7, bd=10 ,fg="white",font=('Copper Black' ,16,'bold italic'),width=10, bg="grey26",command=CBA) 
DS.place(x=590, y=660)
rs.mainloop()
