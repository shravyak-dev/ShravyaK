def credit(balance):
    amount = float(input("Enter amount to credit: "))
    if amount <= 0:
            print("Please enter a positive amount:")
    else:
            balance += amount
            print(f"${amount} credited to your account.")
def debit(balance):
        amount = float(input("Enter amount to debit: "))
        if amount <= 0:
            print("Please enter a positive amount.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"${amount} debited from your account.")
def current_balance(balance):
      print(f"current bank balance is:$ {balance}")
def main():
      balance=0
      while True:
            
        print("\nATM Menu:")
        print("1. Credit")
        print("2. Debit")
        print("3. Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            balance = credit(balance)
        elif choice == '2':
            balance = debit(balance)
        elif choice == '3':
            current_balance(balance)
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()


              