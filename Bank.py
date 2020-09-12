from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
import pymysql

root = Tk()
UserID = StringVar()
Password = StringVar()


def main():
    global root
    global UserID
    global Password
    root.configure(bg = "purple")
    root.geometry('1350x750+0+0')
    root.title("BANKING SYSTEM")
    titleLabel = Label(root,text = "PBI",font = ('arial',50,'bold'),bd = 20,bg = "purple")
    titleLabel.grid(row = 0,column =0)
    lblUsername = Label(root, text= "UserID",font = ('arial',30,'bold'),bd = 22,bg = 'purple')
    lblUsername.grid(row = 1,column = 3)
    txtUsername = Entry(root,font = ('arial',25,'bold'),textvariable = UserID,bd = 22,bg="grey")
    txtUsername.grid(row = 1,column = 4,pady = 10)
    txtUsername.focus()
    lblpassword = Label(root,text = "Password",font = ('arial',30,'bold'),bd = 22,bg = 'purple')
    lblpassword.grid(row = 2,column =3 )
    txtpassword = Entry(root,font = ('arial',25,'bold'),textvariable = Password,show = ".",bd = 22,bg="grey")
    txtpassword.grid(row = 2,column = 4,padx = 85)
    btnLogin = Button(root,text = "Login",width = 17,font = ('arial',20,'bold'),bg = "grey",command = lambda:login())
    btnLogin.grid(row = 7, column = 4)

    lblcontact = Label(root,text = "Facing Any problem contact pbi@gmail.com!!",font = ('arial',20),bd = 20,bg = "purple")
    lblcontact.place(x = 400,y = 650)

def remove_all_widgets():
    global root
    for widget in root.winfo_children():
        widget.destroy()
def backbtn():
    remove_all_widgets()
    secWindow()

def transacWin():
    global UserID
    global root
    root.configure(bg = "purple")
    root.geometry('1350x750+0+0')
    root.title("TRANSACTIONS")
    titleLabel = Label(root,text = "TRANSACTIONS",font = ('arial',30,'bold'),bd = 20,bg = "purple")
    titleLabel.grid(row = 0,column =0)

    
    framepr = Frame(root,bg = 'purple')
    framepr.place(x = 50, y= 100,width = 1000,height = 500)
    transactionTV = ttk.Treeview(framepr,height=25, columns=('USERID','TIME'))
    transactionTV.grid(row = 5, column = 0, columnspan=5,padx = 5)
    transactionTV.column("#0", width=270, minwidth=270)
    transactionTV.column("USERID", width=150, minwidth=150)
    transactionTV.column("TIME", width=400, minwidth=200)

    scrollBar = Scrollbar(framepr, orient="vertical")
    scrollBar.grid(row=5, column=4, sticky="NSE")
    transactionTV.configure(yscrollcommand=scrollBar.set)
    ttk.Style().configure("transactionTV", background="black", foreground="white", fieldbackground="black")

    transactionTV.heading('#0',text="TO_USER_ID")
    transactionTV.heading('#1',text="AMOUNT")
    transactionTV.heading('#2',text="DATE")

    btnback = Button(root,text="BACK",font = ('arial',15,'bold'),width = 20,bg = "grey",command = lambda:backbtn())
    btnback.place(x = 950,y=500)
    
    ide = UserID.get()
    query = "select to_userid,tranfer_amount,date_of_t from Transactions where userid ='{}'".format(ide)
    try :
        conn = pymysql.connect(host = "localhost",user = "root",passwd = "deepak@123",database = "bank")
        with conn:
            with conn.cursor() as cur:
                cur.execute(query)
                vals = cur.fetchall()
            for i in vals:
                transactionTV.insert("", 'end',text = i[0] , values =( i[1],i[2]))

    except Exception as e:
        print(e)

def sendMoney(idt,amo,dt):
    global UserID
    query = "insert into Transactions value('{}','{}','{}','{}')".format(UserID,idt,amo,dt)
    try:
        conn = pymysql.connect(host="localhost",user="root",passwd="deepak@123",database="bank")
        with conn:
            with conn.cursor() as cur:
                cur.execute(query)

    except Exception as e:
        print(e)

def moneyWin():
    global root
    root.configure(bg = "purple")
    root.geometry('1350x750+0+0')
    root.title("MONEY TRANSFER")
    transferID = StringVar()
    amount = StringVar()
    now = datetime.datetime.now()
    date = now.strftime("%Y/%m/%d %H:%M:%S")
    titleLabel = Label(root,text = "MONEY TRANSFER",font = ('arial',30,'bold'),bd = 20,bg = "purple")
    titleLabel.place(x = 0,y =0)
    framepr = LabelFrame(root,text = 'ACCOUNT DETAILS',bg = 'purple',font = ('arial',15,'bold'))
    framepr.place(x = 5, y= 100,width = 890,height = 500)

    lblTransferid = Label(framepr,text = "TransferID:",font = ('arial',25,'bold'),bd = 20,bg = 'purple')
    lblTransferid.place(x=0,y=0)
    txtTransferId = Entry(framepr,font = ('arial',25,'bold'),textvariable = transferID,bd = 15,bg="grey")
    txtTransferId.place(x= 400,y=0)

    lblAmount = Label(framepr,text = "Amount:",font = ('arial',25,'bold'),bd = 20,bg = 'purple')
    lblAmount.place(x=0,y=100)
    txtAmount = Entry(framepr,font = ('arial',25,'bold'),textvariable = amount,bd = 15,bg="grey")
    txtAmount.place(x= 400,y=100)

    lblAmount = Label(framepr,text = "Date:",font = ('arial',25,'bold'),bd = 20,bg = 'purple')
    lblAmount.place(x=0,y=200)
    txtAmount = Label(framepr,font = ('arial',25,'bold'),text = date,bd = 15,bg="grey")
    txtAmount.place(x= 400,y=200)
   
    btntransfer = Button(root,text = "TRANSFER",font = ('arial',15,'bold'),width = 20,bg = "grey",command = lambda:sendMoney(transferID,amount,date))
    btntransfer.place(x = 900,y = 500)

    btnback = Button(root,text="BACK",font = ('arial',15,'bold'),width = 20,bg = "grey",command = lambda:backbtn())
    btnback.place(x = 900,y=550)






def moneytansfer():
    remove_all_widgets()
    moneyWin()
def checktransactions():
    remove_all_widgets()
    transacWin()
def logout():
    remove_all_widgets()
    main()
    global UserID
    global Password
    UserID.set("")
    Password.set("")
    
def checkbalance():
    global UserID
    ide = UserID.get()
    query = "SELECT balance FROM Accounts WHERE userid = '{}' ".format(ide)
    try:
        conn = pymysql.connect(host = "localhost",user = "root",passwd = "deepak@123",database = "bank")
        with conn:
            with conn.cursor() as cur:
                cur.execute(query)
                val = cur.fetchone()
    except Exception as e:
        print(e)
    
    tkinter.messagebox.showinfo("BALANCE","YOUR BALANCE IS: %s"%(val))


#=============================== MENU WINDOW =====================================================================================================


def secWindow():
    global root
    global UserID
    root.configure(bg = "purple")
    root.geometry('1350x750+0+0')
    root.title("BANKING OPTIONS")
    toplabel = Label(root,text = "PBI APP",font = ('arial',30,'bold'),bd = 20,bg = "purple")
    toplabel.grid(row = 0,column = 0)
    ide = UserID.get()
    query = "SELECT Nam FROM Accounts WHERE userid = '{}'".format(ide)
    try:
        conn = pymysql.connect(host = "localhost",user = "root",passwd = "deepak@123",database = "bank")
        with conn:
            with conn.cursor() as cur:
                cur.execute(query)
                name = cur.fetchone()
    except Exception as e:
        print(e)
    lblwelcom = Label(root,text = "Hello %s"%(name),font = ('arial',15,'bold'),bd =10,bg = "purple")
    lblwelcom.grid(row = 3,column = 0)
    btntransac = Button(root,text = "SHOW TRANSACTIONS",width = 20,font = ('arial',15,'bold'),bg = "grey",command = lambda:checktransactions())
    btntransac.place(x = 100, y = 150)

    btnmoney = Button(root,text = "MONEY TRANSFER ",width = 20,font = ('arial',15,'bold'),bg = "grey",command = lambda:moneytansfer())
    btnmoney.place(x = 500, y = 150)

    btnbalance = Button(root,text = "BALANCE",width =20,font = ('arial',15,'bold'),bg = "grey",command = lambda:checkbalance())
    btnbalance.place(x = 900,y = 150)

    instruct1lbl = Label(root,text = "INSTRUCTIONS",font = ('arial',25,'bold'),bd = 20,bg = "purple")
    instruct1lbl.place(x = 100,y = 300) 
    instruct2lbl = Label(root,text = "1. MAKE SURE YOU HAVE A GOOD INTERNET CONNECTION",font = ('arial',15,'bold'),bd = 20,bg = "purple")
    instruct2lbl.place(x = 100,y = 360)
    instruct3lbl = Label(root,text = "2. APPLICATION UNDER CONSTRUCTION ",font = ('arial',15,'bold'),bd = 20,bg = "purple")
    instruct3lbl.place(x = 100,y = 420)
    instruct4lbl = Label(root,text = "3. TRANSACTIONS ONLY TAKES PLACE IF THE ACCOUNT IS OF THE SAME BANK",font = ('arial',15,'bold'),bd = 20,bg = "purple")
    instruct4lbl.place(x = 100,y = 480)

    btnbalance = Button(root,text = "Logout",width =20,font = ('arial',15,'bold'),bg = "grey",command = lambda:logout())
    btnbalance.place(x = 950,y = 500)




#=====================================================================================================================================================     

#===================CHECKING IF THE USER EXISTS OR NOT================================================================================================


def login():
    global UserID
    global Password
    usID = UserID.get()
    passs = Password.get()
    uid,pas = [],[]

    query = "SELECT userid FROM Users"
    query1 = "SELECT pass FROM Users"
    try:
        conn = pymysql.connect(host="localhost",user = "root",passwd = "deepak@123",database="bank")
        with conn:
            with conn.cursor() as cur:
                cur.execute(query)
                user = cur.fetchall()
                for i in user:
                    for j in i:
                        uid.append(j)
                cur.execute(query1)
                pase = cur.fetchall()
                for i in pase:
                    for j in i:
                        pas.append(j)
    except Exception as e:
        print(e)
    if usID == "" and passs == "":
        tkinter.messagebox.showerror("Banking login","PASSWORD OR USERNAME NOT ENTERED")

    elif usID in uid and passs in pas:
        remove_all_widgets()
        secWindow()
    else:
        tkinter.messagebox.showerror("Banking login","NO SUCH USER FOUND")



#============================================================================================================================================



main()
root.mainloop()


