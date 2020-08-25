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


acc1=BankAccount(0.15, 100)
acc2=BankAccount(0.2, 500)
acc1.deposit(30).deposit(500).deposit(100).withdraw(35).yield_interest().display_account()
acc2.deposit(300).deposit(50).deposit(1000).withdraw(500).yield_interest().display_account()