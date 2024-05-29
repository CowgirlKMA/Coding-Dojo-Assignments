from Bank_Account import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.05, balance=0)
    #make all of the methods below call on its bank account's instance methods
    def make_deposit(self, amount):
        self.account.deposit(amount)
        # print(self.account.balance)
        return self

    def make_withdrawal(self, amount):
        self.account.withdrawal(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

user_katie = User("Katie", "katie@gmail.com")
#using chaining method
user_katie.make_deposit(1000).make_deposit(500).make_deposit(225).make_deposit(300).account.yield_interest().display_account_info()

user_katie.make_deposit(500)
user_katie.account.display_account_info()
user_katie.make_withdrawal(200)
user_katie.display_user_balance()
