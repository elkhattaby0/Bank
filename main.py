import tkinter as main
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk
import dash as ttt
import signup as sp
import video as vd
#5160f9 blue    ---   2c2d31 dark   ---   7efa88  green   ---  b39377  brown
class User(main.Tk):
    def __init__(self) :
        super().__init__()
        self.minsize(1000, 600)
        self.maxsize(1000, 600)
        self.title('Banka Liiiik - Sign In')
    
    def signIn(self):
        canvas1 = main.Canvas(self, background='#2c2d31', width=1000, height=601) # background color
        canvas1.pack() 

        logoL = main.Label(self, text='BANKA LIIIIK', font=('Arial 42 bold'), fg='#5160f9', bg='#2c2d31') # name logo
        logoL.place(x=580, y=80)

        emailE = main.Entry(self, width=23, font=('Arial 20')) # entry mail
        emailE.place(x=580, y=260)
        
        passwordE = main.Entry(self, width=23, font=('Arial 20'), show='*') # entry password
        passwordE.place(x=580, y=360)

        emailL = main.Label(self, text='Email', font=('Arial 14'), fg='white', bg='#2c2d31') # label mail
        emailL.place(x=585, y=232)

        passwordL = main.Label(self, text='Password', font=('Arial 14'), fg='white', bg='#2c2d31') # label password
        passwordL.place(x=585, y=331)

        btnlogin = main.Button(self, text='Log In', fg='white',bg='#5160f9', width=16, height=2, relief='flat', command=lambda: verfiedIndata()) # btn log in
        btnlogin.place(x=580, y=450)

        btnsignup = main.Button(self, text='Sign Up', fg='black', bg='white', width=16, height=2, relief='flat', command=lambda: snp()) # btn sign up
        btnsignup.place(x=710, y=450)

        btnforgot = main.Button(self, text='Forget password', relief='flat', fg='white', bg='#2c2d31', width=12, height=2, command=lambda: viv()) #btn forgot password
        btnforgot.place(x=580, y=400)

        image1 = Image.open("istockphoto-1031507604-612x612.jpg") # image
        test = ImageTk.PhotoImage(image1)
        label1 = main.Label(image=test, width=511, height=601, bg='#ffffff')
        label1.image = test
        label1.place(x=0, y=0)

        def verfiedIndata():
            mail = emailE.get()
            pass1 = passwordE.get()
            db = sqlite3.connect('data.db')
            c = db.cursor()
            c.execute('select Id, fname, lname, email, gender, password from signUp')
            
            for i in c.fetchall():
                if ((mail in i[3]) and (pass1 in i[5])) and ((mail != '') and (pass1 != '')):
                    messagebox.showinfo("Successfully", "Successfully")
                    c.execute(f"select Id from signUp where email='{mail}'")
                    result = c.fetchone()
                    return ttt.User().dash(result[0])
            else:
                messagebox.showerror("Error", "Email or Password Incorrect")
        
        def snp(): # for sign Up botton
            if btnsignup:
                sp.User().signUp()
        def ex():
            if btnsignup:
                exit()

        def viv():
            if btnforgot:
                vd.Vdeio().video()

    def CreateData():
        db = sqlite3.connect('data.db')
        db.execute("create table if not exists signUp(Id integer, fname text, lname text, email text, gender text, password text, repassword text, age integer, transactions float, balance float )")
        db.close()
    CreateData()

if __name__ == '__main__':
    app = User()
    app.signIn()
    app.mainloop()