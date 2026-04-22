##Mini-Project: "AI Number Guessing Game Lite"
print("Mini-Project: AI Number Guessing Game Lite")

import random   # importing random module to generate number

# computer selects a random number between 1 and 50
secret = random.randint(1, 50)
# total attempts allowed
attempts = 7

# counter to track how many tries used
count = 0

print("Welcome to AI Number Guessing Game Lite!")
print("Guess a number between 1 and 50")


# loop runs until attempts finish
while count < attempts:

    # taking input from user
    guess = int(input("Enter your guess: "))

    # checking if input is in valid range
    if guess < 1 or guess > 50:
        print("Please enter a number between 1 and 50\n")
        continue   # skip rest and ask again

    # increasing attempt count
    count += 1

    # checking conditions
    if guess > secret:
        print("Too high!")

    elif guess < secret:
        print("Too low!")

    else:
        # correct guess
        print(f"You win in {count} attempts!")
        print("AI training level: Beginner → Intermediate")
        break   # exit loop when correct

    # showing remaining attempts
    remaining = attempts - count
    print(f"Attempts left: {remaining}")
    
# if user fails after all attempts
if count == attempts and guess != secret:
    print("Game Over!")
    print(f"The correct number was {secret}")