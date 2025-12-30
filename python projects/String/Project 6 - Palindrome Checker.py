str = input("Enter a string: ") #Takes input from the user
string = str.replace(" ", "").lower() #Removes spaces and converts to lowercase
reversed_str = string[::-1] #Reverses the string
if string == reversed_str: #Checks if the original string is equal to the reversed string
    print(f'"{str}" is a palindrome.')
else:
    print(f'"{str}" is not a palindrome.')