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
        self.heading = Label(master, text="UPDATE YOUR STORE PRODUCT", font=('arial 30 bold'), fg='darkred')
        self.heading.place(x=600, y=0)

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

        self.totalcp_1 = Label(master, text="Enter Total Cost Price:", font=('arial 18 bold'))
        self.totalcp_1.place(x=0, y=230)

        self.totalsp_1 = Label(master, text="Enter Total Selling Price :", font=('arial 18 bold'))
        self.totalsp_1.place(x=0, y=270)

        self.vendor_1 = Label(master, text="Enter Vendor Name :", font=('arial 18 bold'))
        self.vendor_1.place(x=0, y=310)

        self.vendor_phoneno_1 = Label(master, text="Enter Vendor Phone No :", font=('arial 18 bold'))
        self.vendor_phoneno_1.place(x=0, y=350)

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

        self.totalcp_e = Entry(master, width=25, font=('arial 18 bold'), bg="steelblue")
        self.totalcp_e.place(x=300, y=230)

        self.totalsp_e = Entry(master, width=25, font=('arial 18 bold'), bg="steelblue")
        self.totalsp_e.place(x=300, y=270)

        self.vendor_e = Entry(master, width=25, font=('arial 18 bold'), bg="steelblue")
        self.vendor_e.place(x=300, y=310)

        self.vendor_phoneno_e = Entry(master, width=25, font=('arial 18 bold'), bg="steelblue")
        self.vendor_phoneno_e.place(x=300, y=350)

        self.btn_add = Button(master, text="UPDATE DATA", width=25, height=2, bg='darkgreen', fg='black',command=self.update)
        self.btn_add.place(x=550, y=400)

        self.btn_clr = Button(master, text="CLEAR DETAILS", width=25, height=2, bg="red", fg="black",
                              command=self.clear_all)
        self.btn_clr.place(x=300, y=400)

        self.btn_search = Button(master, text='Search', width=10, height=2, bg='orange', command=self.search)
        self.btn_search.place(x=400, y=30)

        self.tBox = Text(master, width=80, height=22, bg="steelblue")
        self.tBox.place(x=650, y=70)
        self.tBox.insert(END, "ID has reached upto :" + str(id))

    def clear_all(self, *args, **kwargs):
        self.id_e.delete(0, END)
        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.vendor_phoneno_e.delete(0, END)

    def search(self, *args, **kwargs):
        ID = self.id_e.get()
        mycursor.execute("SELECT * FROM ss where id = '%s'" % (ID))
        FETCH =mycursor.fetchall()
        print(FETCH)
                                       #self.name_e.get(),self.stock_e.get(),self.cp_e.get(),self.sp_e.get(),self.totalcp_e.get(),self.totalsp_e.get(),self.vendor_e.get(),self.vendor_phoneno_e.get()))
        for r in FETCH:
            self.n1 = r[1]  # name
            self.n2 = r[2]  # stock
            self.n3 = r[3]  # cp
            self.n4 = r[4]  # sp1
            self.n5 = r[5]  # totalcp
            self.n6 = r[6]  # totalsp
            self.n8 = r[8]  # vendor
            self.n9 = r[9]  # vendor_phoneno

        mydb.commit()
        self.name_e.delete(0,END)
        self.name_e.insert(0, str(self.n1))

        self.stock_e.delete(0,END)
        self.stock_e.insert(0, str(self.n2))

        self.cp_e.delete(0,END)
        self.cp_e.insert(0, str(self.n3))

        self.sp_e.delete(0,END)
        self.sp_e.insert(0, str(self.n4))

        self.totalcp_e.delete(0,END)
        self.totalcp_e.insert(0, str(self.n5))

        self.totalsp_e.delete(0,END)
        self.totalsp_e.insert(0, str(self.n6))

        self.vendor_e.delete(0,END)
        self.vendor_e.insert(0, str(self.n8))

        self.vendor_phoneno_e.delete(0,END)
        self.vendor_phoneno_e.insert(0, str(self.n9))
        self.id_e.get()





    def update(self, *args, **kwargs):
        ID = self.id_e.get()

        mycursor.execute("UPDATE ss SET name = '%s',sp='%s',cp='%s',vendor='%s',vendor_phoneno='%s' WHERE id = '%s'" % ((self.name_e.get()),(self.sp_e.get()),(self.cp_e.get()),(self.vendor_e.get()),(self.vendor_phoneno_e.get()),(ID)))
        sql = mycursor.fetchone()
        print(sql)
        mydb.commit()

        tkinter.messagebox.showinfo("Success","Record Updated..!!")

root = Tk()
b = Database(root)

root.geometry("1300x800+0+0")
root.title("Update Your Products")
root.mainloop()