class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    def example_method(self):
        self.account.deposit(100)		# we can call the BankAccount instance's methods
    	print(self.account.balance)		# or access its attributes