print("Welcome to the Calculator!")
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
op = input("Enter an operator (+, -, *, /): ")
if num1.isdigit() and num2.isdigit():
    num1 = float(num1)
    num2 = float(num2)
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Error: Invalid operator"