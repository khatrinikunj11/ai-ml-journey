print("Hello Sir, Welcome to the Contact Book with Duplicate Detection")


user_name = str(input("Enter your name: "))
user_phone_number = int(input("Enter your phone number: "))
user_email = str(input("Enter your email: "))
user_details = (user_name, user_phone_number, user_email)


contacts = {}         
phone_numbers = set()  
emails = set()         


def add_contact():
    contact_name = str(input("Enter the name of the contact: "))
    contact_phone_number = int(input("Enter the phone number of the contact: "))
    contact_email = str(input("Enter the email of the contact: "))
    if contact_phone_number in phone_numbers or contact_email in emails:
        print("Contact already exists")
    else:
        contacts[contact_name] = {contact_phone_number, contact_email}
        phone_numbers.add(contact_phone_number)
        emails.add(contact_email)
        print("Contact added successfully")

def view_contact():
    print(contacts)

def main():
    a = True
    while a:
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contact()
        elif choice == 3:
            print("Thank you for using the Contact Book with Duplicate Detection")
            break
        else:
            print("Invalid choice")
            break
    
main()
