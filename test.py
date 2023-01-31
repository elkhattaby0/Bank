class bank:
    solde = 0
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname
        # self.solde = solde

    def balance(self, prix):
        bank.solde += prix
        print('Fullname : ', self.fname, ' ', self.lname, '\n Solde : ', bank.solde)

x = bank('lahoucine', 'elkhattaby')
x.balance(11)
x.balance(4)
x.balance(5)