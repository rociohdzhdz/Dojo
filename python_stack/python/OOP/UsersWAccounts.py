class BankAccount:
    def __init__ (self, int_rate,accbalance):
        self.balance=accbalance
        self.interes=int_rate
        self.earnings=0
    def deposit(self,amountdep):
        self.balance+=amountdep
        return self
    def yield_interest(self):
        self.earnings=self.balance*self.interes
        return self
    def withdraw(self,amountwit):
        if amountwit>self.balance:
            print(f"Te required amount {amountwit} exceeds your current balance of {self.balance}, you will be charged with a fee of $5")
            feecharge=self.balance-5
            self.balance=feecharge
        self.balance-=amountwit
        return self
   
    def display_account(self): 
        self.balance+=self.earnings
        print(f"Account balance Today $ {self.balance} you have been earn {self.earnings}")

class User:
    def __init__(self, username, email_add, int_rate,accbalance):
        self.name=username
        self.email=(email_add)
        self.accounts=BankAccount(int_rate,accbalance)
    def create_account(self, int_rate, accbalance):
        self.accounts=BankAccount(int_rate,accbalance)
        self.accounts.deposit(50000)
        self.accounts.withdraw(1000)
        self.accounts.yield_interest()
        return self
    

rex=User("Gilrex Cervantes", "gilrex@mail.com",.15,0)
rex.create_account(.12,300)
rex.accounts.display_account()
