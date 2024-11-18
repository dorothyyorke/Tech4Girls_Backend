
class BankAccount:
    bank_name = "Tech4Girls Bank"  # Class variable
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Error: Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Error: Insufficient funds or withdrawal amount invalid.")
    @staticmethod
    def bank_policy():  # Static method
        print("Tech4Girls Bank policy: All transactions are subject to our terms.")
    @classmethod
    def get_bank_name(cls):  # Class method
        return cls.bank_name
my_account = BankAccount("Alice")
my_account.deposit(1000)
my_account.withdraw(500)
BankAccount.bank_policy()
print(BankAccount.get_bank_name()) # Output: Tech4Girls Bank