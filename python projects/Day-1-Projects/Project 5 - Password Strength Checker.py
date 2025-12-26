password = input("Enter a password: ") 

# Check 1: Length
if len(password) >= 8: #Check if password length is at least 8 characters
    print("Length is good!")
else:
    print("Too short!")

# Check 2: Has number?
has_number = False
for char in password:
    if char in "0123456789": #Check if any character is a digit by using for loop
        has_number = True
        break

if has_number:
    print("Has a number!")
else:
    print("Add a number!")

# Check 3: Has uppercase?
has_uppercase = False
for char in password:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": #Check if any character is an uppercase letter by using for loop
        has_uppercase = True
        break

if has_uppercase:
    print("Has uppercase!")
else:
    print("Add an uppercase letter!")