import tkinter as main
from tkinter import ttk
from tkinter import messagebox
import sqlite3
#5160f9 blue    ---   2c2d31 dark   ---   7efa88  green   ---  b39377  brown

class User(main.Tk):
    code = 1110
    def __init__(self) :
        super().__init__()
        self.minsize(1000, 600)
        self.maxsize(1000, 600)
        self.title('Banka Liiiik - Sign Up')
        User.code = User.code + 1
        self.code = User.code
        

    def signUp(self):
        canvas = main.Canvas(self, background='#2c2d31', width=1000, height=601)
        canvas.pack()

        logo = main.Label(self, text='BANKA LIIIIK', bg='#2c2d31', fg='#5160f9', font=('Arial 48 bold')) #logo
        logo.place(x=350, y=30)

        fnameL = main.Label(self, text='First name', bg='#2c2d31', fg='#F7F7F7', font='bold') # first name
        fnameL.place(x=50, y=185)

        fnameE = main.Entry(self, width=20, font=('Arial 20'))
        fnameE.place(x=150, y=180)

        lnameL = main.Label(self, text='Last name', bg='#2c2d31', fg='#F7F7F7', font='bold') # last name
        lnameL.place(x=530, y=185)

        lnameE = main.Entry(self, width=20, font=('Arial 20'))
        lnameE.place(x=630, y=180)

        emailL = main.Label(self, text='Email', bg='#2c2d31', fg='#F7F7F7', font='bold') # email
        emailL.place(x=50, y=285)

        emailE = main.Entry(self, width=20, font=('Arial 20'))
        emailE.place(x=150, y=280)

        genderL = main.Label(self, text='Gender', bg='#2c2d31', fg='#F7F7F7', font='bold') # gender
        genderL.place(x=530, y=285)

        genderList = main.Listbox(self, height=2, width=50)
        genderList.insert(1, 'Male')
        genderList.insert(2, 'Femmle')
        genderList.place(x=630, y=280)

        passL = main.Label(self, text='Password', bg='#2c2d31', fg='#F7F7F7', font='bold') # password
        passL.place(x=50, y=375)

        passE = main.Entry(self, width=20, font=('Arial 20'), show='*')
        passE.place(x=150, y=370)

        repassL = main.Label(self, text='Repassword', bg='#2c2d31', fg='#F7F7F7', font='bold') # repassword
        repassL.place(x=530, y=375)

        repassE = main.Entry(self, width=20, font=('Arial 20'), show='*')
        repassE.place(x=630, y=370)
        
        ageL = main.Label(self, text='Year of birth', bg='#2c2d31', fg='#F7F7F7', font='bold') # age
        ageL.place(x=50, y=475)

        ageE = main.Entry(self, width=20, font=('Arial 20'))
        ageE.place(x=150, y=470)

        btnUp = main.Button(self, text='Sign Up', height=2, width=13, bg='#5160f9', fg='white', font='bold', command=lambda: getToInfo(), relief='flat') #btn sign Up
        btnUp.place(x=630, y=460)
        
        btnIn = main.Button(self, text='Sign In', height=2, width=13, bg='#F2E7D5', fg='black', font='bold', relief='flat') #btn sign In
        btnIn.place(x=807, y=460)
        self.lbotona=btnIn
        
        def getToInfo():
            
            fn = fnameE.get()
            ln = lnameE.get()
            email = emailE.get()
            age = ageE.get()
            curr0 = 0
            curr1 = 0.0
            for i in genderList.curselection():
                 gender = genderList.get(i)
           
            if passE.get() != repassE.get():
                messagebox.showerror("Error", "Password incorrect")
            
            elif (fn == '') or (ln == '') or (email == '') or (age == ''):
                messagebox.showerror("Error", "Erorr")

            else:
                password = passE.get()
                repassword = repassE.get()
                messagebox.showinfo("Valid", "Valid")

            db = sqlite3.connect('data.db')
            c = db.cursor()
            c.execute(f"insert into signUp(Id, fname, lname, email, gender, password, repassword, age, transactions, balance) values('{self.code}', '{fn}', '{ln}', '{email}', '{gender}', '{password}', '{repassword}', '{age}', '{curr1}', '{curr0}')")
            db.commit()

if __name__ == '__main__':
    app = User()
    app.signUp()
    app.mainloop()