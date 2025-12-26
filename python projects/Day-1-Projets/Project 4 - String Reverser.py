str = input("Enter a string: ") #Takes input from the user
print("Reversed string:", str[::-1]) #Reverses the entire string including letters and spaces
print("Reversed words:", ' '.join(reversed(str.split()))) #Reverses the order of words
print("Alternate characters:", str[::2]) #Prints every second character from the string
