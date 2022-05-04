class BankAccount:
    # class attributes
    bank_name = "Bank of Dojo"
    all_accounts = []

    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    # class method to change the name of the Bank
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    @classmethod
    def all_balance(cls):
        sum = 0
        #we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        print(f"There are {len(cls.all_accounts)} accounts in Bank of Dojo.")
        print(f"There is {sum} in all accounts in Bank of Dojo.")
        return sum
        


    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        self.balance * self.int_rate
        return self

# Instance Accounts
# Account1 = BankAccount(0.01)
# Account2 = BankAccount(0.04)

# Account1.deposit(1000).deposit(2000).deposit(3000).withdraw(4000).yield_interest().display_account_info()
# Account2.deposit(10).deposit(5).withdraw(5).withdraw(4).withdraw(1).withdraw(100).yield_interest().display_account_info()

# BankAccount.all_balance()