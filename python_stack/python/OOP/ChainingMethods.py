class User:
    def __init__(self, username, email_add, account_balance):
        self.name=username
        self.email=(email_add)
        self.balance=account_balance
        self.withdrawal=0
        # return self
    def make_deposit(self, amountdep):
        self.balance+=amountdep
        return self
    def make_withdrawal(self, amountwithdr):
        self.balance-=amountwithdr
        return self
    def display_result(self):
        print(f"User Name is: {self.name}, Account balance$ {self.balance}")
        return self
    def transfer_money(self, other_user, amounttransfered):
        other_user.make_deposit(amounttransfered) 
        self.make_withdrawal(amounttransfered)
        return self 

rex=User("Gilrex Cervantes", "gilrex@mail.com",3000)
rei=User("Rei Ayanami", "rei@mail.com",5000)
vio=User("Violeta Pineda", "vio@mail.com",3000)

rex.make_deposit(8000).make_deposit(100).make_deposit(70).make_withdrawal(90).transfer_money(rei,250).display_result()
rei.make_deposit(3000).make_deposit(1000).make_deposit(900).make_withdrawal(120).transfer_money(vio,150).display_result()
vio.make_deposit(200).make_deposit(800).make_deposit(1000).make_withdrawal(300).display_result()
