from tkinter import *
from typing import Any, Union, Generator

import mysql.connector
import tkinter.messagebox
import datetime
import os
import random
import  math
from mysql.connector.cursor import MySQLCursor
from mysql.connector.cursor_cext import CMySQLCursor

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="kumbharnr",
    database="myproject")

mycursor = mydb.cursor()

date = datetime.datetime.now().date()

products_list = []
products_price = []
products_quantity = []
products_id = []

labels_list = []
class Applictaion:
    def __init__(self,master,*args,**kwargs):

        self.master = master
        self.left = Frame(master,width=700,height=768,bg='white')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=650, height=768, bg='lightblue')
        self.right.pack(side=RIGHT)

        self.heading = Label(self.left,text="KJEI STORE",font=('arial 33 bold'))
        self.heading.place(x=0,y=0)

        self.date_1 = Label(self.right, text="Todays Date :" + str(date), font=('arial 12 bold'), bg='lightblue',
                            fg='white')
        self.date_1.place(x=0, y=0)

        self.tproduct = Label(self.right, text="Products", font=('arial 18 bold'), bg='lightblue', fg='white')
        self.tproduct.place(x=0, y=50)
        self.tquantity = Label(self.right, text="Quantity", font=('arial 18 bold'), bg='lightblue', fg='white')
        self.tquantity.place(x=300, y=50)

        self.tamount = Label(self.right, text="Amount", font=('arial 18 bold'), bg='lightblue', fg='white')
        self.tamount.place(x=500, y=50)

        self.enterid = Label(self.left, text='Enter Product : ', width=25, font=('arial 18 bold'), bg='white')
        self.enterid.place(x=0, y=80)

        self.enteride = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
        self.enteride.place(x=260, y=80)
        self.enteride.focus()

        self.search_btn = Button(self.left, text='Search', width=20, height=2, bg='orange', command=self.ajax)
        self.search_btn.place(x=400, y=120)

        # fill it later by function ajax
        self.productname = Label(self.left, text="", font=('arial 27 bold'), bg='white', fg='blue')
        self.productname.place(x=0, y=250)

        self.pprice = Label(self.left, text="", font=('arial 27 bold'), bg='white', fg='blue')
        self.pprice.place(x=0, y=290)

        self.quantity_1 = Label(self.left, text="Enter Quantity", font=('arial 18 bold'), bg='white')
        self.quantity_1.place(x=0, y=370)

        self.quantity_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
        self.quantity_e.place(x=190, y=370)
        self.quantity_e.focus()

        # discount
        self.discount_1 = Label(self.left, text="Enter discount", font=('arial 18 bold'), bg='white')
        self.discount_1.place(x=0, y=410)

        self.discount_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
        self.discount_e.place(x=190, y=410)
        self.discount_e.insert(END, 00)

        # add to cart button
        self.add_to_cart_btn = Button(self.left, text="Add To Cart", width=22, height=2, bg='orange',
                                      command=self.add_to_cart)
        self.add_to_cart_btn.place(x=350, y=450)

        # generate bill and change
        self.change_1 = Label(self.left, text="Given Amount", font=('arial 18 bold'), bg='white')
        self.change_1.place(x=0, y=550)

        self.change_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
        self.change_e.place(x=190, y=550)

        # button change
        self.change_btn = Button(self.left, text="Calculate Change", width=22, height=2, bg='orange',
                                 command=self.change)
        self.change_btn.place(x=350, y=590)

        # generate bill button
        self.bill_btn = Button(self.left, text="Generate Bill", width=100, height=2, bg='blue', fg='white',command=self.generate_bill)
        self.bill_btn.place(x=0, y=650)

        self.total_1 = Label(self.right,text="",font=('arial 40 bold'),bg='lightblue',fg='white')
        self.total_1.place(x=0,y=600)

    def ajax(self, *args, **kwargs):
        self.get_id = self.enteride.get()


        # get the product info with that id and fill it in the labels above
        #ID = self.self.enteride.get()
        mycursor.execute("SELECT * FROM ss where id = '%s'" % (self.get_id))
        FETCH = mycursor.fetchall()
        print(FETCH)

        for self.r in FETCH :
            self.get_id = self.r[0]
            self.get_name = self.r[1]
            self.get_price = self.r[4]
            self.get_stock = self.r[2]
            self.productname.configure(text="Product's Name:" + str(self.get_name))
            self.pprice.configure(text="Price:Rs. " + str(self.get_price))


    def add_to_cart(self,*args,**kwargs):
        self.quantity_value = int(self.quantity_e.get())
        if self.quantity_value > int(self.get_stock):
            tkinter.messagebox.showinfo("Error","Not In Stock")
        else:
            self.final_price = float(self.quantity_value)*float(self.get_price)
            products_list.append(self.get_name)
            products_price.append(self.final_price)
            products_quantity.append(self.quantity_value)
            products_id.append(self.get_id)

            self.x_index = 0
            self.y_index = 90
            self.counter = 0
            for self.p in products_list:
                self.tempname = Label(self.right,text=str(products_list[self.counter]),font=('arial 18 bold'),bg='lightblue',fg='white')
                self.tempname.place(x=0,y=self.y_index)
                labels_list.append(self.tempname)

                self.tempqt = Label(self.right, text=str(products_quantity[self.counter]), font=('arial 18 bold'), bg='lightblue',fg='white')
                self.tempqt.place(x=300, y=self.y_index)
                labels_list.append(self.tempqt)


                self.tempprice = Label(self.right, text=str(products_price[self.counter]), font=('arial 18 bold'), bg='lightblue',fg='white')
                self.tempprice.place(x=500, y=self.y_index)
                labels_list.append(self.tempprice)

                self.y_index += 40
                self.counter +=1

                self.total_1.configure(text="Total Rs :" + str(sum(products_price)))

                #self.quantity_1.place_forget()
                #self.quantity_e.place_forget()
                #self.discount_1.place_forget()
                #self.discount_e.place_forget()
                #self.change_1.place_forget()
                #self.change_e.place_forget()
    def change(self,*args,**kwargs):
        self.amount_given = float(self.change_e.get())
        self.our_total = float(sum(products_price))

        self.to_give = self.amount_given - self.our_total


        self.c_amount = Label(self.left,text='Change : Rs ' + str(self.to_give),font=('arial 18 bold'),fg='red')
        self.c_amount.place(x=0,y=590)
    def generate_bill(self,*args,**kwargs):

        directory = "/home/owner/PycharmProjects/store/invoice/" + str(date)
        if not os.path.exists(directory):
            os.makedirs(directory)

        company = "\t\t\t\tKJEI STORE \n"
        address = "\t\t\t\tADDRESS : YEWLEWADI, PUNE 411048 MAHARASHTRA,INDIA\n"
        phone= "\t\t\t\tphone no : 7218973712/9763111462\n"
        dt = "\t\t\t\t" + str(date)
        sample = "\t\t\t\t**invoice**\n"


        table_header = "\n\n\t\t\t\t------------------------------------------\n\t\t\t\tSN.\tproducts\tQty\tAmount\n\t\t\t\t-------------------------------------------"
        final =company +address+phone+sample+dt+ "\n"+table_header

        file_name= str(directory) + str(random.randrange(5000,10000)) + ".docs"
        f= open(file_name,'w')
        f.write(final)

        r=1
        i=0
        for t in products_list:
            f.write("\n\t\t\t"+str(r)+"\t" +str(products_list[i] +".....")[:20] +"\t\t"+str(products_quantity[i]) + "\t\t" +str(products_price[i]))
            i +=1
            r +=1
        f.write("\n\n\t\t\tTotal:Rs."+str(sum(products_price)))
        f.write("\n\n\t\t\tThanks for visiting")
        #os.starfile(file_name,"print")
        f.close()

        self.x = 0


        sql = "INSERT INTO transactions(product_name,quantity,amount,dates) VALUES (%s,%s,%s,%s)"
        mycursor.execute(sql, (products_list[self.x],products_quantity[self.x],products_price[self.x],date))
        mydb.commit()
        self.x +=1

        for a in labels_list:
            a.destroy()
        del(products_list[:])
        del(products_id[:])
        del(products_quantity[:])
        del(products_price[:])

        self.total_1.configure(text="")
        #self.c_amount.configure(text="")
        self.change_e.delete(0,END)



        tkinter.messagebox.showinfo("success","DONE")
    #def generate_bill(self, *args, **kwargs):
root=Tk()
b=Applictaion(root)

root.geometry("1300x768+0+0")
root.mainloop()


