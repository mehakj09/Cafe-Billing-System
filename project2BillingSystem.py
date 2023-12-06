from tkinter import*
import pandas as pd
import csv

root = Tk()
root.geometry("1080x600")
root.title("Cafe Billing System")

Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

lblinfo = Label(Tops, font=( 'Helvetica' ,50, 'bold italic' ),text="Cafe Billing System",fg="midnight blue",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)


def xRef():

    Cor =int(Croissants.get())
    San = int(Sandwich.get())
    Wra = int(Wrap_Salad.get())
    Sou = int(Soup.get())
    Pan = int(Pancakes.get())
    Cof = int(coffee_tea.get())

    costofcroissants = Cor*50
    costofsandwich = San*40
    costofwrap = Wra*70
    costofsoup = Sou*35
    costofpancakes = Pan*60
    costofcoffee_tea = Cof*45

    #tax rate is 12% ( 12/100 = 0.12)
    #service charge rate is 20% ( 10/100 = 0.2)

    costofmeal = "Rs.",str((costofcroissants +  costofsandwich + costofwrap + costofsoup + costofpancakes + costofcoffee_tea))
    PayTax=((costofcroissants +  costofsandwich + costofwrap + costofsoup + costofpancakes + costofcoffee_tea)*0.12)
    Totalcost=(costofcroissants +  costofsandwich + costofwrap + costofsoup + costofpancakes + costofcoffee_tea)
    Ser_Charge=((costofcroissants +  costofsandwich + costofwrap + costofsoup + costofpancakes + costofcoffee_tea)*0.2)
    Service="Rs.",str(Ser_Charge)
    OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="Rs.",str(PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)

def xexit():
    root.destroy()
    
def xsave():
    #to csv
    Or= str(int(rand.get()))
    Cf = str(int(coffee_tea.get()))
    Ci = str(int(Croissants.get()))
    Sn = str(int(Sandwich.get()))
    Wa = str(int(Wrap_Salad.get()))
    Su = str(int(Soup.get()))
    Pn = str(int(Pancakes.get()))
    lst = [[Or, Cf, Ci, Sn, Wa, Su, Pn]]
    dataframe = pd.DataFrame(lst)
    dataframe.to_csv('Product.csv', index=False, mode='a', header=False)

def xreset():
    rand.set("")
    Croissants.set("")
    Sandwich.set("")
    Wrap_Salad.set("")
    Soup.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    coffee_tea.set("")
    Tax.set("")
    cost.set("")
    Pancakes.set("")


#-------------------------------------------label and entry --------------------------------------------
rand = StringVar()
Croissants = StringVar()
Sandwich = StringVar()
Wrap_Salad = StringVar()
Soup = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
coffee_tea = StringVar()
Tax = StringVar()
cost = StringVar()
Pancakes = StringVar()


LReference = Label(f1, font=( 'Helvetica' ,16, 'bold' ),text="Order No.",fg="SteelBlue4",bd=20,anchor='w')
LReference.grid(row=0,column=0)
EReference = Entry(f1,font=('Helvetica' ,16,'bold'), textvariable=rand , bd=6,insertwidth=6,bg="skyblue4" ,justify='right')
EReference.grid(row=0,column=1)

LCroissants = Label(f1, font=( 'Helvetica' ,16, 'bold' ),text=" Croissants  ",fg="SteelBlue4",bd=10,anchor='w')
LCroissants.grid(row=2,column=0)
ECroissants = Entry(f1,font=('Helvetica' ,16,'bold'), textvariable=Croissants  , bd=6,insertwidth=4,bg="SlateGray1" ,justify='right')
ECroissants.grid(row=2,column=1)

LSandwich = Label(f1, font=( 'Helvetica' ,16, 'bold' ),text="Sandwich ",fg="SteelBlue4",bd=10,anchor='w')
LSandwich.grid(row=3,column=0)
ESandwich = Entry(f1,font=('Helvetica' ,16,'bold'), textvariable=Sandwich , bd=6,insertwidth=4,bg="SlateGray1" ,justify='right')
ESandwich.grid(row=3,column=1)


LWrap = Label(f1, font=( 'Helvetica' ,16, 'bold' ),text="Wrap & Salad ",fg="SteelBlue4",bd=10,anchor='w')
LWrap.grid(row=4,column=0)
EWrap = Entry(f1,font=('Helvetica' ,16,'bold'), textvariable=Wrap_Salad , bd=6,insertwidth=4,bg="SlateGray1" ,justify='right')
EWrap.grid(row=4,column=1)

LSoup = Label(f1, font=( 'Helvetica' ,16, 'bold' ),text="Soup ",fg="SteelBlue4",bd=10,anchor='w')
LSoup.grid(row=5,column=0)
ESoup = Entry(f1,font=('Helvetica' ,16,'bold'), textvariable=Soup , bd=6,insertwidth=4,bg="SlateGray1" ,justify='right')
ESoup.grid(row=5,column=1)

LPancakes = Label(f1, font=( 'Helvetica' ,16, 'bold' ),text="Pancakes",fg="SteelBlue4",bd=10,anchor='w')
LPancakes.grid(row=6,column=0)
EPancakes = Entry(f1,font=('Helvetica' ,16,'bold'), textvariable=Pancakes , bd=6,insertwidth=4,bg="SlateGray1" ,justify='right')
EPancakes.grid(row=6,column=1)

LCoffee = Label(f1, font=( 'Helvetica' ,16, 'bold' ),text="Coffee/Tea",fg="SteelBlue4",bd=10,anchor='w')
LCoffee.grid(row=1,column=0)
ECoffee = Entry(f1,font=('Helvetica' ,16,'bold'), textvariable=coffee_tea , bd=6,insertwidth=4,bg="SlateGray1" ,justify='right')
ECoffee.grid(row=1,column=1)

LCost = Label(f1, font=( 'Helvetica' ,16, 'bold' ),text="Cost",fg="SteelBlue4",bd=10,anchor='w')
LCost.grid(row=2,column=2)
ECost = Entry(f1,font=('Helvetica' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="white" ,justify='right')
ECost.grid(row=2,column=3)

LService_Charge = Label(f1, font=( 'Helvetica' ,16, 'bold' ),text="Service Charge",fg="SteelBlue4",bd=10,anchor='w')
LService_Charge.grid(row=3,column=2)
EService_Charge = Entry(f1,font=('Helvetica' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="white" ,justify='right')
EService_Charge.grid(row=3,column=3)

LTax = Label(f1, font=( 'Helvetica' ,16, 'bold' ),text="Tax",fg="SteelBlue4",bd=10,anchor='w')
LTax.grid(row=4,column=2)
ETax = Entry(f1,font=('Helvetica' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="white" ,justify='right')
ETax.grid(row=4,column=3)

LSubtotal = Label(f1, font=( 'Helvetica' ,16, 'bold' ),text="Subtotal",fg="SteelBlue4",bd=10,anchor='w')
LSubtotal.grid(row=5,column=2)
ESubtotal = Entry(f1,font=('Helvetica' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="white" ,justify='right')
ESubtotal.grid(row=5,column=3)

LTotal = Label(f1, font=( 'Helvetica' ,16, 'bold' ),text="Total",fg="SteelBlue4",bd=10,anchor='w')
LTotal.grid(row=6,column=2)
ETotal = Entry(f1,font=('Helvetica' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="grey" ,justify='right')
ETotal.grid(row=6,column=3)

LTotal = Label(f1,text="---------------------",fg="white")
LTotal.grid(row=7,columnspan=3)

#-----------------------------------------buttons------------------------------------------

xTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('Helvetica' ,16,'bold'),width=10, text="TOTAL", bg="midnight blue",command=xRef)
xTotal.grid(row=8, column=1)

xreset=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('Helvetica' ,16,'bold'),width=10, text="RESET", bg="midnight blue",command=xreset)
xreset.grid(row=8, column=2)

xexit=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('Helvetica' ,16,'bold'),width=10, text="EXIT", bg="midnight blue",command=xexit)
xexit.grid(row=8, column=3)


def xprice():
    price = Tk()
    price.geometry("600x220")
    price.title("Price List")
    label1 = Label(price, font=('Helvetica', 15, 'bold'), text="ITEM", fg="black", bd=5)
    label1.grid(row=0, column=0)
    label1 = Label(price, font=('Helvetica', 15,'bold'), text="_____________", fg="white", anchor=W)
    label1.grid(row=0, column=2)
    label1= Label(price, font=('Helvetica', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    label1.grid(row=0, column=3)
    label1 = Label(price, font=('Helvetica', 15, 'bold'), text="Croissants", fg="steel blue", anchor=W)
    label1.grid(row=1, column=0)
    label1 = Label(price, font=('Helvetica', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    label1.grid(row=1, column=3)
    label1 = Label(price, font=('Helvetica', 15, 'bold'), text="Sandwich ", fg="steel blue", anchor=W)
    label1.grid(row=2, column=0)
    label1 = Label(price, font=('Helvetica', 15, 'bold'), text="40", fg="steel blue", anchor=W)
    label1.grid(row=2, column=3)
    label1 = Label(price, font=('Helvetica', 15, 'bold'), text="Wrap & Salad ", fg="steel blue", anchor=W)
    label1.grid(row=3, column=0)
    label1 = Label(price, font=('Helvetica', 15, 'bold'), text="70", fg="steel blue", anchor=W)
    label1.grid(row=3, column=3)
    label1 = Label(price, font=('Helvetica', 15, 'bold'), text="Soup ", fg="steel blue", anchor=W)
    label1.grid(row=4, column=0)
    label1 = Label(price, font=('Helvetica', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    label1.grid(row=4, column=3)
    label1 = Label(price, font=('Helvetica', 15, 'bold'), text="Pancakes", fg="steel blue", anchor=W)
    label1.grid(row=5, column=0)
    label1 = Label(price, font=('Helvetica', 15, 'bold'), text="60", fg="steel blue", anchor=W)
    label1.grid(row=5, column=3)
    label1 = Label(price, font=('Helvetica', 15, 'bold'), text="Coffee/Tea", fg="steel blue", anchor=W)
    label1.grid(row=6, column=0)
    label1 = Label(price, font=('Helvetica', 15, 'bold'), text="45", fg="steel blue", anchor=W)
    label1.grid(row=6, column=3)

    price.mainloop()

xprice=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="midnight blue",command=xprice)
xprice.grid(row=8, column=0)

xsave=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="SAVE", bg="midnight blue",command=xsave)
xsave.grid(row=8, column=4)


root.mainloop()
