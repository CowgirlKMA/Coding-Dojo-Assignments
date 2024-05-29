class BankAccount:
    #conctructor method for ths class, it is the method that actually creates (instantiates) your object aka instance, think of this as a blueprint
    def __init__(self, int_rate, balance):#paramaters aka properties that define how an object gets created
        self.int_rate = 0.05
        self.balance = 0

    def deposit(self, amount):
        # self.deposit = amount
        self.balance += amount
        print(f"You have deposited: ${amount}, your balance is now: ${self.balance}")
        return self

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"You have withdrawn: ${amount}, your balance is now ${self.balance}")
        else: 
            self.balance <= amount
            self.balance -= 5
            print(f"Insufficient funds: you will be charged a $5 fee, your balance is now ${self.balance}")
        return self    

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            print(f"Your balance including interest is : ${self.balance}")
        else:    
            print("You have not accrued any interest since your balance is negative.")
        return self

    def display_account_info(self):
        print(f"Your balance is: ${self.balance}")

account1 = BankAccount(0.05, 0)
account1.deposit(1000).deposit(500).deposit(225).withdrawal(300).yield_interest().display_account_info()

account2 = BankAccount(0.05, 0)
account2.deposit(300).deposit(5000).withdrawal(300).withdrawal(300).withdrawal(300).withdrawal(300).yield_interest().display_account_info()
