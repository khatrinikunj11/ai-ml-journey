import random
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess (1-100): "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            play_again()
            break
    else:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")
        play_again()
def play_again():
    while True:
        response = input("Do you want to play again? (yes/no): ").strip().lower()
        if response in ['yes', 'y']:
            number_guessing_game()
            return True
        elif response in ['no', 'n']:
            print("Thank you for playing! Goodbye!")
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
number_guessing_game()
        
