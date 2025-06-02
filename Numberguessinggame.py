import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Set the range for the number
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 10  # Number of allowed attempts
    
    print(f"Guess the number between {lower_bound} and {upper_bound}. You have {attempts} attempts.")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))

            if guess < lower_bound or guess > upper_bound:
                print(f"Please enter a number between {lower_bound} and {upper_bound}.")
                continue

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly in {attempt} attempts!")
                return
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    print(f"Sorry, you've used all {attempts} attempts. The correct number was {secret_number}. Better luck next time!")

# Run the game
number_guessing_game()