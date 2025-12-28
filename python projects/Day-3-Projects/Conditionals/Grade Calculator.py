grades = int(input("Enter your grades (1-100): "))
if grades >= 100 or grades < 0:
    print("Invalid grade (must be between 0 and 100)")
else:
    if grades >= 90:
        print("Your grade is A")
    elif grades >= 80:
        print("Your grade is B")
    elif grades >= 65:
        print("Your grade is C")
    elif grades >= 50:
        print("Your grade is D")
    elif grades >= 33:
         print("Your grade is E")
    else:
        print("Your grade is F")