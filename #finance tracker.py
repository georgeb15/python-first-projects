#finance tracker

import sys
mode =int(input("Enter 1 to add a transaction, 2 to view transactions, or 3 to exit: "))
if mode == 1:
    transaction = input("Enter the transaction (e.g., 'Groceries'): ")
    with open("transactions.txt", "a") as file:
        file.write(transaction + " ")
    print("Transaction added.")
    amount = input("Enter the amount: ")
    with open("transactions.txt", "a") as file:
        file.write(amount + "\n")
    print("Amount added.")
elif mode == 2:
    with open("transactions.txt") as file:
        transactions = file.readlines()
    for transaction in transactions:
        print(transaction.strip())
elif mode == 3:
    sys.exit("Exiting the finance tracker")