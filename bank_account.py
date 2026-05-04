# bank_account.py
class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return -1
        else:
            self.balance -= amount
            return 0

    def __str__(self):
        acc_str = str(self.account_number)
        last_digits = acc_str[-2:]
        return f"Account Number: **{last_digits}\nCurrent Balance: {self.balance:.2f}"
    
    def balance_summary(people):
    for person in people:
        total = 0
        for acc in person.accounts:
            total += acc.balance
        print(f"{person.name} : {total:.2f}")