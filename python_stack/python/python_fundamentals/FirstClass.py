class User:
    def __init__(self, username, email_add):
        self.name=username
        self.email=email_add
        self.account_balance=0
        self.passwr="123"
    def make_deposit(self, amount):
        self.account_balance+=amount
    def def_pws(self,newpws):
        self.passwr=newpws

guido=User("Guido van Rossum", "guido@mail.com")
monty=User("Monty burns", "monty@mail.com")
guido.make_deposit(200)
guido.make_deposit(80)
monty.make_deposit(300)
guido.def_pws("Newp@ss.2020")
print("This is Guido Email: ",guido.email)
print(monty.email)
print(guido.account_balance)
print(guido.passwr)
print(monty.account_balance)