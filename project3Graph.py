import pandas as pd
from tkinter import *
from PIL import ImageTk,Image
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
def graph():
    product=pd.read_csv("C:\\Users\\Mehak\\Desktop\\Python\\Cafe Billing Application\\Product.csv")
    product1=product['coffee_tea'].sum()
    product2=product['Croissants'].sum()
    product3=product['Sandwich'].sum()
    product4=product['Wrap_Salad'].sum()
    product5=product['Soup'].sum()
    product6=product['Pancakes '].sum()
    sumlist=[product1,product2,product3,product4,product5,product6]
    itemlist=['Coffee/Tea','Croissants','Sandwich','Wrap & Salad','Soup','Pancakes']
    figure = plt.Figure(figsize = (6.5, 4.5),dpi = 100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, ws)
    chart_type.get_tk_widget().place(x=370, y=320)
    rects1 = ax.bar(itemlist,sumlist)
ws = Tk()
ws.title('Segement analysis')
ws.geometry('1024x768')
photo2=ImageTk.PhotoImage(file =r'C:\Users\Mehak\Desktop\Python\Cafe Billing Application\pic2.png')
lbl=Label(ws,image = photo2,)
lbl.place(x=0,y=0)
Graph1=Button(ws, text="Graph",padx=35,pady=16, bd=10 ,fg="Black",font=('Aria' ,20,'bold italic'),width=10, bg="white",command=graph) 
Graph1.place(x=80, y=440)
ws.mainloop()

