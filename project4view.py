import pandas as pd
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
df=pd.read_csv("C:\\Users\\Mehak\\Desktop\\Python\\Cafe Billing Application\\Product.csv",index_col=0)
page = Tk()
page. geometry("1500x800")

pic0=ImageTk.PhotoImage(file =r'C:\Users\Mehak\Desktop\Python\Cafe Billing Application\pic5.png')
abel=Label(page ,image = pic0,)
abel.place(x=0,y=0)

tree1 = ttk.Treeview(page)
tree1.place(x=50,y=350)
tree1['columns'] = df.columns.values.tolist()

for i in df.columns.values.tolist():
    tree1.column(i)
    tree1.heading(i, text=i)
for index, row in df.iterrows():
    tree1.insert("", 'end', text=index, values=list(row))
print(df.iterrows())

page.mainloop()
