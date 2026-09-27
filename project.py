# Mini Bank Management System

balance = 5000
transactions = []

def show_balance():
    print("\n💰 Current Balance:", balance)

def deposit():
    global balance

    amount = float(input("Enter deposit amount: ₹"))

    if amount > 0:
        balance += amount
        transactions.append(f"Deposited ₹{amount}")
        print("✅ Money deposited successfully!")
    else:
        print("❌ Invalid amount.")

def withdraw():
    global balance

    amount = float(input("Enter withdrawal amount: ₹"))

    if amount <= 0:
        print("❌ Invalid amount.")
    elif amount > balance:
        print("❌ Insufficient balance.")
    else:
        balance -= amount
        transactions.append(f"Withdrawn ₹{amount}")
        print("✅ Money withdrawn successfully!")

def show_transactions():
    print("\n📜 Transaction History")

    if len(transactions) == 0:
        print("No transactions yet.")
    else:
        for transaction in transactions:
            print("-", transaction)


while True:
    print("\n==========================")
    print("       MINI BANK")
    print("==========================")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        show_transactions()

    elif choice == "5":
        print("Thank you for using Mini Bank! 👋")
        break

    else:
        print("❌ Invalid choice. Try again.")