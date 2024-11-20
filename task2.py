import random

def number_guessing_game():
    # Generate a random secret number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize the number of attempts
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    print("Try to guess the number!")

    # Loop to keep asking the player for guesses
    while True:
        # Get the player's guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Increment the number of attempts
        attempts += 1
        
        # Check the player's guess against the secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            # The player guessed correctly
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break

# Call the game function to start the game
number_guessing_game()
