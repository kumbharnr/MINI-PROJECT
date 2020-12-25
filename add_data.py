from tkinter import *
import mysql.connector
import tkinter.messagebox

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="kumbharnr",
    database="myproject")

mycursor = mydb.cursor()


# mycursor.execute("CREATE DATABASE myproject")
# mycursor.execute("CREATE TABLE ss(id INT,name VARCHAR(255),stock INT,cp INT,sp INT,totalcp INT,totalsp INT,assumed_profit INT,vendor VARCHAR(225),vendor_phoneno INT)")

class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="ADD YOUR STORE PRODUCT", font=('arial 35 bold'), fg='red')
        self.heading.place(x=500, y=0)

        self.id_1 = Label(master, text="Enter ID :", font=('arial 18 bold'))
        self.id_1.place(x=0, y=40)

        self.name_1 = Label(master, text="Enter Product Name :", font=('arial 18 bold'))
        self.name_1.place(x=0, y=70)

        self.stock_1 = Label(master, text="Enter Stock :", font=('arial 18 bold'))
        self.stock_1.place(x=0, y=110)

        self.cp_1 = Label(master, text="Enter Cost Price:", font=('arial 18 bold'))
        self.cp_1.place(x=0, y=150)

        self.sp_1 = Label(master, text="Enter Selling Price :", font=('arial 18 bold'))
        self.sp_1.place(x=0, y=190)

        self.vendor_1 = Label(master, text="Enter Vendor Name :", font=('arial 18 bold'))
        self.vendor_1.place(x=0, y=230)

        self.vendor_phoneno_1 = Label(master, text="Enter Vendor Phone No :", font=('arial 18 bold'))
        self.vendor_phoneno_1.place(x=0, y=270)

        self.id_e = Entry(master, width=7, font=('arial 18 bold'), bg="steelblue")
        self.id_e.place(x=300, y=30)

        self.name_e = Entry(master, width=25, font=('arial 18 bold'), bg="steelblue")
        self.name_e.place(x=300, y=70)

        self.stock_e = Entry(master, width=25, font=('arial 18 bold'), bg="steelblue")
        self.stock_e.place(x=300, y=110)

        self.cp_e = Entry(master, width=25, font=('arial 18 bold'), bg="steelblue")
        self.cp_e.place(x=300, y=150)

        self.sp_e = Entry(master, width=25, font=('arial 18 bold'), bg="steelblue")
        self.sp_e.place(x=300, y=190)

        self.vendor_e = Entry(master, width=25, font=('arial 18 bold'), bg="steelblue")
        self.vendor_e.place(x=300, y=230)

        self.vendor_phoneno_e = Entry(master, width=25, font=('arial 18 bold'), bg="steelblue")
        self.vendor_phoneno_e.place(x=300, y=270)

        self.btn_add = Button(master, text="ADD DATA", width=25, height=2, bg='darkgreen', fg='black',
                              command=self.get_items)
        self.btn_add.place(x=550, y=340)

        self.btn_clr = Button(master, text="CLEAR DETAILS", width=25, height=2, bg="red", fg="black",
                              command=self.clear_all)
        self.btn_clr.place(x=300, y=340)

        self.tBox = Text(master, width=80, height=16.5, bg="steelblue")
        self.tBox.place(x=650, y=70)
        self.tBox.insert(END, "ID has reached upto :" + str(id))

    def get_items(self, *args, **kwargs):
        self.id = self.id_e.get()
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vendor = self.vendor_e.get()
        self.vendor_phoneno = self.vendor_phoneno_e.get()

        self.totalcp = float(self.cp) * float(self.stock)
        self.totalsp = float(self.sp) * float(self.stock)
        self.assumed_profit = float(self.totalsp - self.totalcp)
        if self.id == '' or self.name == '' or self.stock == '' or self.cp == '' or self.sp == '':
            tkinter.messagebox.showinfo("ERROR", "PLEASE INSERT DATA")

        else:
            sql = "INSERT INTO ss(id,name,stock,cp,sp,totalcp,totalsp,assumed_profit,vendor,vendor_phoneno) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(sql, (
            self.id, self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit,
            self.vendor, self.vendor_phoneno))
            mydb.commit()

            # self.tBox.insert(END,"Inserted" +str(self.name) + "into the products")
            tkinter.messagebox.showinfo("success", "ADDED SUCCESSFULLY")

    def clear_all(self, *args, **kwargs):
        self.id_e.delete(0, END)
        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.vendor_phoneno_e.delete(0, END)


root = Tk()
b = Database(root)

root.geometry("1300x800+0+0")
root.title("Add Your Product")
root.mainloop()