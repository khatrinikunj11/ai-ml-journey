name = input("Welcome, Please enter your full name - ") #Taking Input from user
print("Hello " + name)
print("""
I will do following manipulations on your name:
1. Print your name in uppercase
2. Print your name in lowercase
3. Print your name with first letter of each word capitalized    
4. Print the number of characters in your name (excluding spaces)
5. Print the Initials (e.g., "J.D.S.")  
""")
print("1. Your name in uppercase is: ",name.upper()) #Uppercasing the name
print("2. Your name in lowercase is: ",name.lower()) #Lowercasing the name
print("3. Your name with first letter of each word capitalized is: ",name.title()) #Title Case(First letter of each word capitalized)
name_excluding_spaces = name.replace(" ", "") #Replacing spaces with nothing(Removing spaces)
print("4. The number of characters in your name (excluding spaces) is: ",len(name_excluding_spaces)) #Finding length of name excluding spaces

words = name.split() #Splitting the name into list of words 
initials = "" #Making an empty string to store initials
for word in words: #Looping each word in the list
    first_letter = word[0] #Getting the first letter of each word      
    uppercase_letter = first_letter.upper()  #Uppercasing the first letter
    initials = initials + uppercase_letter + "." #Adding dot after each initial

print("5. Your initials are: ",initials) #Printing the initials
