import datetime

print("Hello Sir, Welcome to the Personal Expense Tracker")
expenses = []
categories = {}
a = True
while a:
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        expense = input("Enter the expense: ")
        category = input("Enter the category: ")
        expenses.append((datetime.date.today(), expense, category))
        categories[category] = categories.get(category, 0)
        print("Expense added successfully")
    elif choice == 2:
        for expense in expenses:
            print(expense)
        for category in categories.items():
            print(category)
    elif choice == 3:
        break
    else:
        print("Invalid choice")
        break