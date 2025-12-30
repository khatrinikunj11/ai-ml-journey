print("Hello Sir, Welcome to the Student Grade Management System")
dict = {}
list = []
list2 = []
list3 = []
tuple = ()
a = True
while a:
    print("1. Add Student Details")
    print("2. View Students Details")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter the name of the student: ")
        grade = input("Enter the grade of the student: ")
        dict[name] = {grade}
        print("Student added successfully")
        a = int(input("How many subjects are there? "))
        for i in range(a):
            subject = input("Enter the subject name: ")
            grade = input("Enter the grade of the subject: ")
            list.append(grade)
            list2.append(subject)
        print("Subject with grades added successfully")
        list3.append(name)
        list3.append(list)
        list3.append(list2)
        roll_number = input("Enter the roll number of the student: ")
        class_name = input("Enter the class name of the student: ")
        father_name = input("Enter the father's name of the student: ")
        mother_name = input("Enter the mother's name of the student: ")
        address = input("Enter the address of the student: ")
        phone_number = input("Enter the phone number of the student: ")
        email = input("Enter the email of the student: ")
        tuple = (roll_number,class_name,father_name,mother_name,address,phone_number,email)
        list3.append(tuple)
        print("Student details added successfully")
        a = int(input("Do you want to add more students? (1 for yes, 0 for no): "))
        if a == 1:
            continue
        else:
            break

    elif choice == 2:
        print(f"Student Details: {list3}")
    elif choice == 3:
        break
    else:
        print("Invalid choice")
        break