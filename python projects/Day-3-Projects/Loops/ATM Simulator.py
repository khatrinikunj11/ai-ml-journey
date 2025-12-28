# ATM Simulator

class ATM:
    def __init__(self, initial_balance=1000):
        self.balance = initial_balance
        self.transactions = []
        self.transactions.append(f"Initial Balance: ${initial_balance}")
    
    def check_balance(self):
        print(f"\n--- Current Balance ---")
        print(f"Your balance: ${self.balance:.2f}\n")
    
    def deposit(self):
        while True:
            try:
                amount = float(input("Enter amount to deposit: $"))
                if amount <= 0:
                    print("Amount must be greater than 0. Try again.")
                    continue
                self.balance += amount
                self.transactions.append(f"Deposit: +${amount:.2f}")
                print(f"Successfully deposited ${amount:.2f}")
                print(f"New balance: ${self.balance:.2f}\n")
                break
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
    
    def withdraw(self):
        while True:
            try:
                amount = float(input("Enter amount to withdraw: $"))
                if amount <= 0:
                    print("Amount must be greater than 0. Try again.")
                    continue
                if amount > self.balance:
                    print(f"Insufficient balance. Your balance: ${self.balance:.2f}")
                    continue
                self.balance -= amount
                self.transactions.append(f"Withdrawal: -${amount:.2f}")
                print(f"Successfully withdrew ${amount:.2f}")
                print(f"New balance: ${self.balance:.2f}\n")
                break
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
    
    def view_history(self):
        print("\n--- Transaction History ---")
        for transaction in self.transactions:
            print(transaction)
        print()
    
    def run(self):
        print("Welcome to ATM Simulator\n")
        
        while True:
            print("--- Main Menu ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transaction History")
            print("5. Exit")
            
            while True:
                try:
                    choice = input("Select an option (1-5): ")
                    if choice in ['1', '2', '3', '4', '5']:
                        break
                    else:
                        print("Invalid choice. Please select 1-5.")
                except ValueError:
                    print("Invalid input. Please try again.")
            
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                self.view_history()
            elif choice == '5':
                print("Thank you for using ATM Simulator. Goodbye!\n")
                break

# Run the ATM
if __name__ == "__main__":
    atm = ATM()
    atm.run()