from bank_account import BankAccount
class User:
    bank_name = "Bank of Dojo"
    def __init__(self, name, email, account = {"savings":BankAccount(), "checking": BankAccount()}):
        self.name = name
        self.email = email
        self.account = account
# make deposit method
    def make_deposit(self, amount, account_type):
        self.account[account_type].deposit(amount)
        return self
# make withdrawal method
    def make_withdrawal(self, amount, account_type):
        self.account[account_type].withdraw(amount)
        return self
# display user balance method
    def display_user_balance(self, account_type):
        print(f"{self.name}")
        self.account[account_type].display_account_info()
        return self

    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        self.display_user_balance()
        other_user.display_user_balance()

Account1 = BankAccount()
Account2 = BankAccount()
Account3 = BankAccount()

# Instance Users
ana = User("Ana Banana", "ana@python.com", account = {"checking": BankAccount()})
moxi = User("Moxi Bossy", "moxi@python.com")
# monty = User("Monty Python", "monty@python.com")
moxi.make_deposit(1000, 'checking').display_user_balance('checking')
moxi.make_withdrawal(200, 'checking').display_user_balance('checking').make_deposit(200, 'savings').display_user_balance('savings')

# ana.make_deposit(1000)
# ana.make_deposit(300)
# ana.make_deposit(300)
# ana.make_withdrawal(500)
# ana.display_user_balance()

# moxi.make_deposit(9000)
# moxi.make_deposit(3000)
# moxi.make_withdrawal(1000)
# moxi.make_withdrawal(2000)
# moxi.display_user_balance()

# monty.make_deposit(2000)
# monty.make_withdrawal(500)
# monty.make_withdrawal(500)
# monty.make_withdrawal(500)
# monty.display_user_balance()

# # User tranfer funds
# monty.transfer_money(ana, 400)