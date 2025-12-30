email = input("Enter your email address: ") #Taking Input from user
if "@" in email: #Checks if @ is present in the email
    print("Yes, it contains '@'.") 
if email.endswith(".com"): #Checks if email ends with .com
    print("Yes, it ends with '.com'.")
a = email.find("@") #Finds the index of @ in the email
print(email[0:a], "is the username.") #Prints the username part of the email
print(email[a+1:], "is the domain name.") #Prints the domain name part of the email