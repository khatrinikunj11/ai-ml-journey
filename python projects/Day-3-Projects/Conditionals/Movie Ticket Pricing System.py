import datetime
from datetime import date

print("Good morning, sir")
print("Average ticket price is 400 INR though it may vary based on age, time, and day of the week.")
age = int(input("What is your age? "))
day = date.today()
time = input("Which time do you want to watch the movie? (morning or evening) ").lower()
ticket_price = 400
if age < 3:
    ticket_price = 0
    print("Your ticket is free!")
elif age <= 12:
    ticket_price -= 50
    print("Your ticket is decreased by 50 INR due to age less than 12.")
    if time == "morning":
        ticket_price -= 75
        print("Your ticket is decreased by 75 INR due to morning time.")
    elif time == "evening":
        ticket_price += 50
        print("Your ticket is increased by 50 INR due to evening time.")
    else:
        print("Invalid time input. Please enter 'Morning' or 'Evening'.")

elif 13 <= age <= 59:
    if time == "morning":
        ticket_price -= 75
        print("Your ticket is decreased by 75 INR due to morning time.")
    elif time == "evening":
        ticket_price += 50
        print("Your ticket is increased by 50 INR due to evening time.")
    else:
        print("Invalid time input. Please enter 'Morning' or 'Evening'.")
elif age >= 60:
    ticket_price -= 100
    print("Your ticket is decreased by 100 INR due to senior citizen discount.")
    if time == "morning":
        ticket_price -= 75
        print("Your ticket is decreased by 75 INR due to morning time.")
    elif time == "evening":
        ticket_price += 50
        print("Your ticket is increased by 50 INR due to evening time.")
    else:
        print("Invalid time input. Please enter 'Morning' or 'Evening'.")
if day.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
    ticket_price += 50
    print(f"Since it's weekend, an additional charge of 50 INR is applied.")

print(f"Your final ticket price is: {ticket_price} INR")