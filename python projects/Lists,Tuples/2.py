print("Enter marks of 6 students: ")
marks = [] #Making an Empty List
marks.append(input("Enter marks of student 1: ")) #Adding marks to the List
marks.append(input("Enter marks of student 2: "))
marks.append(input("Enter marks of student 3: "))
marks.append(input("Enter marks of student 4: "))
marks.append(input("Enter marks of student 5: "))
marks.append(input("Enter marks of student 6: "))
marks.sort() #Sorting the List in ascending order
print("Your list of marks is:", marks)