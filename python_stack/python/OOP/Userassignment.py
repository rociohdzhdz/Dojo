class User:
    def __init__(self, username, email_add, account_balance):
        self.name=username
        self.email=(email_add)
        self.balance=account_balance
        self.withdrawal=0
    def make_deposit(self, amountdep):
        self.balance+=amountdep
        return self
    def make_withdrawal(self, amountwithdr):
        self.balance-=amountwithdr
    def display_result(self):
        print(f"User Name is: {self.name}, Account balance${self.balance}")
    def transfer_money(self, other_user, amount):
        # BONUS
        # let's leverage the fact that we have deposit and withdrawal methods that are available to self and other_user
        # since they're both User objects...You don't have to do it this way though
        other_user.make_deposit(amount) # could also say other_user.account_balance += amount
        self.make_withdrawal(amount) # could also say self.account_balance -= amount

rex=User("Gilrex Cervantes", "gilrex@mail.com",3000)
rei=User("Rei Ayanami", "rei@mail.com",5000)
vio=User("Violeta Pineda", "vio@mail.com",3000)

rex.make_deposit(8000)
rex.make_deposit(200)
rex.make_deposit(100)
rex.make_withdrawal(70)
rex.display_result()

rei.make_deposit(3000)
rei.make_deposit(1000)
rei.make_deposit(900)
rei.make_withdrawal(2000)
rei.display_result()

vio.make_deposit(200)
vio.make_deposit(2000)
vio.make_deposit(200)
vio.make_withdrawal(200)
vio.display_result()

# BONUS
rex.transfer_money(rei,250)
rex.display_result()
rei.display_result()