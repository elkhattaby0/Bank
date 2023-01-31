import tkinter as main
from tkinter import ttk
import sqlite3
# from main import User as snn
#5160f9 blue    ---   2c2d31 dark   ---   7efa88  green   ---  b39377  brown

class User(main.Tk):
    solde = 0
    def __init__(self) :
        super().__init__()
        self.minsize(1000, 600)
        self.maxsize(1000, 600)
        self.title('Banka Liiiik - Dashboard')

    def dash(self, the_id=0):
        db = sqlite3.connect('data.db')
        c = db.cursor()
        c.execute(f"select fname from signUp where Id='{the_id}'")
        ff = c.fetchall()

        canvas = main.Canvas(self, background='white', width=1000, height=601)
        canvas.pack()

        logo = main.Label(self, text='BANKA LIIIIK', bg='white', fg='#5160f9', font=('Arial 42 bold')) #logo
        logo.place(x=540, y=40)

        balanceL = main.Label(self, text='Total Balance', font=('Arial 20 bold'), bg='white', fg='#2c2d31') # balance
        balanceL.place(x=480, y=200)

        c.execute(f"select balance from signUp where Id='{the_id}'")

        bbbbb = c.fetchone()
        cur1 = bbbbb, 'MAD'
        mnL = main.Label(self, text=cur1, font=('Arial 15 bold'), bg='white', fg='#2c2d31') # 0
        mnL.place(x=520, y=250)

        bkFrame = main.Frame(self, background="#2c2d31", height=131, width=191) # back right
        bkFrame.place(x=771 ,y=180)

        tranL = main.Label(self, text='Transactions', font=('Arial 18 bold'), bg='#2c2d31', fg='white') # Transactions
        tranL.place(x=789, y=200)

        c.execute(f"select transactions from signUp where Id='{the_id}'")
        cvcvcv = c.fetchall()
        cur100 = cvcvcv, 'MAD'
        mnlL = main.Label(self, text= cur100, font=('Arial 15 bold'), bg='#2c2d31', fg='white') # -3
        mnlL.place(x=810, y=250)

        transfersL = main.Label(self, text='Transfers', font=('Arial 15 bold'), bg='white', fg='#2c2d31') # transfersL
        transfersL.place(x=480, y=380)

        bkFrame = main.Frame(self, background="#2c2d31", height=181, width=501) # back right2
        bkFrame.place(x=460 ,y=410)

        fnL = main.Label(self, text='Fullname', font=('Arial 10 bold'), bg='#2c2d31', fg='white') # fullname
        fnL.place(x=490, y=420)

        reasonL = main.Label(self, text='Reason', font=('Arial 10 bold'), bg='#2c2d31', fg='white') # Reason
        reasonL.place(x=620, y=420)

        ribL = main.Label(self, text='RIB', font=('Arial 10 bold'), bg='#2c2d31', fg='white') # rib
        ribL.place(x=750, y=420)

        amountL = main.Label(self, text='Amount', font=('Arial 10 bold'), bg='#2c2d31', fg='white') # amount
        amountL.place(x=880, y=420)

        recebtn = main.Button(self, text='Receive', bg='#7efa88', fg='white', width=6, height=2, relief='flat', command=lambda: balance00()) # Receive
        recebtn.place(x=820, y=540)

        sendbtn = main.Button(self, text='Send', bg='#b39377', fg='white', width=6, height=2, relief='flat', command=lambda: [balance01(), balance02()]) # Send
        sendbtn.place(x=880, y=540)
        #-----------------------------------------------------------------------------------
        bkFrameL = main.Frame(self, background="#2c2d31", height=581, width=411) #left bk
        bkFrameL.place(x=10, y=10)

        imgL = main.Frame(self, background="white", height=151, width=151) #left bk
        imgL.place(x=140, y=50)

        c.execute(f"select lname from signUp where Id='{the_id}'")
        ll = c.fetchall()
        
        ccc = ff + ll
        fnL = main.Label(self, text=ccc, font=('Arial 14 bold'), bg='#2c2d31', fg='white') # fullname
        fnL.place(x=110, y=210)
        
        c.execute(f"select Id from signUp where Id='{the_id}'")
        z = c.fetchall()

        cnL = main.Label(self, text='Compte number :', font=('Arial 11 bold'), bg='#2c2d31', fg='white') # Compte number
        cnL.place(x=50, y=280)
        cnL0 = main.Label(self, text=z, font=('Arial 11 bold'), bg='#2c2d31', fg='white') # Compte number
        cnL0.place(x=250, y=280)

        cardL = main.Label(self, text='Card :', font=('Arial 11 bold'), bg='#2c2d31', fg='white') # card
        cardL.place(x=50, y=340)
        cardL0 = main.Label(self, text='---', font=('Arial 11 bold'), bg='#2c2d31', fg='white') # card
        cardL0.place(x=250, y=340)

        c.execute(f"select age from signUp where Id='{the_id}'")
        d = c.fetchall()

        yrL = main.Label(self, text='Year of birth :', font=('Arial 11 bold'), bg='#2c2d31', fg='white') # Year of birth
        yrL.place(x=50, y=400)
        yrL0 = main.Label(self, text=d, font=('Arial 11 bold'), bg='#2c2d31', fg='white') # Year of birth
        yrL0.place(x=250, y=400)

        c.execute(f"select gender from signUp where Id='{the_id}'")
        dd = c.fetchall()

        numberL = main.Label(self, text='Gender :', font=('Arial 11 bold'), bg='#2c2d31', fg='white') #  gender
        numberL.place(x=50, y=460)
        numberL0 = main.Label(self, text=dd, font=('Arial 11 bold'), bg='#2c2d31', fg='white') #  gender
        numberL0.place(x=250, y=460)

        addressL = main.Label(self, text='Address :', font=('Arial 11 bold'), bg='#2c2d31', fg='white') # address
        addressL.place(x=50, y=520)
        addressL0 = main.Label(self, text='---', font=('Arial 11 bold'), bg='#2c2d31', fg='white') # address
        addressL0.place(x=250, y=520)

        #-----------------------------------------------------------------------------------

        fnE = main.Entry(self, width=6, font=('Arial 20')) #fullname 
        fnE.place(x=470, y=470)

        rsE = main.Entry(self, width=6, font=('Arial 20')) #reason 
        rsE.place(x=600, y=470)

        rbE = main.Entry(self, width=6, font=('Arial 20')) #rib
        rbE.place(x=730, y=470)

        amE = main.Entry(self, width=6, font=('Arial 20')) #amount
        amE.place(x=860, y=470)

        def balance00():
            global nbr2 
            c.execute(f"select balance from signUp where Id='{the_id}'")
            bbbbb = c.fetchone()
            nbr1 = float(amE.get())
            nbr2 = bbbbb[0]
            print(nbr1)
            print(nbr2)
            nbr2 += nbr1
            print(nbr2)
            c.execute(f"UPDATE  signUp SET  balance='{nbr2}' where Id='{the_id}'")
            db.commit()

        def balance01():
            c.execute(f"select balance from signUp where Id='{the_id}'")
            bbbbb = c.fetchone()
            nbr1 = float(amE.get())
            nbr2 = bbbbb[0]
            print(nbr1)
            print(nbr2)
            nbr2 -= nbr1
            print(nbr2)
            c.execute(f"UPDATE  signUp SET  balance='{nbr2}' where Id='{the_id}'")
            db.commit()

        def balance02():
            c.execute(f"select transactions from signUp where Id='{the_id}'")
            cvcvcv = c.fetchone()
            nbr1 = float(amE.get())
            nbr2 = cvcvcv[0]
            print(nbr1)
            print(nbr2)
            nbr2 -= nbr1
            print(nbr2)
            c.execute(f"UPDATE  signUp SET  transactions='{nbr2}' where Id='{the_id}'")
            db.commit()
        
            


if __name__ == '__main__':
    app = User()
    app.dash()
    app.mainloop()