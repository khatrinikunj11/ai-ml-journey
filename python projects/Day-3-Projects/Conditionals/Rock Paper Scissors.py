import random

computer_choices = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0
def get_computer_choice():
    return random.choice(computer_choices)
def get_user_choice():
    choice = input("Enter rock, paper, or scissors : ").lower()
    while choice not in computer_choices :
        choice = input("Invalid choice. Please enter rock, paper, or scissors : ").lower()
    return choice
print("Welcome to Rock, Paper, Scissors!")
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
    print(f"Score - You: {user_score}, Computer: {computer_score}\n")
    if {user_score, computer_score} >= {5, 5}:
        print("Game over!")
        if user_score > computer_score:
            print("Congratulations! You won.")
        else:
            print("Computer won.")
        a = input("Do you want to play again? (yes/no): ").lower()
        if a == "no":
            print("Thanks for playing!")
            break
        if a == "yes":
            user_score = 0
            computer_score = 0
            print("Starting a new game!\n")
            