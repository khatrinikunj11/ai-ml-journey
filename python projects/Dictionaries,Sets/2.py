print("Enter eight numbers: ")
l = set() #Creating an empty set to store unique numbers
for i in range(8): #Loop to take 8 inputs
    num = int(input())
    l.add(num) #Adding each number to the set
print("The unique number(s) are/is:", l)