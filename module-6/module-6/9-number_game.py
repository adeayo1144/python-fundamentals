#/usr/bin/python3

import random

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)

print("I'm thinking of a number between 1 and 20.")
print("You have 5 attempts to guess it!")

# Allow up to 5 attempts
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        
        if guess < 1 or guess > 20:
            print("Please enter a number between 1 and 20.")
            continue

        attempts += 1

        if guess == secret_number:
            print("Congratulations! You guessed the number correctly!")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
    except ValueError:
        print("Invalid input. Please enter a number.")

if attempts == max_attempts and guess != secret_number:
    print("Game Over! You've used all your attempts.")
    print(f"The number was: {secret_number}")
