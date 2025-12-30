num = int(input("Enter a number to generate its multiplication table: "))

while True:
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    choice = input("Do you want to generate another table? (yes/no): ").strip().lower()
    if choice == 'yes':
        num = int(input("Enter a number to generate its multiplication table: "))
    else:
        print("Thank you for using the multiplication table generator!")
        break