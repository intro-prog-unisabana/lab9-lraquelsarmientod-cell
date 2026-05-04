# utils.py
from person import Person
from bank_account import BankAccount
def person_data():
    name = input("Enter the person's name: ")
    person = Person(name)

    while True:
        acc_number = input("Enter a 4-digit account number: ")
        balance = float(input("Enter the initial balance: "))

        account = BankAccount(acc_number, balance)
        person.add_account(account)

        done = input("Are you done adding accounts? (yes/no): ")

        if done == "yes":
            break
    return person