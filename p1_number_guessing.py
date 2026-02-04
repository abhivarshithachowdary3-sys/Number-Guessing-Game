import random

comps_secret_num = random.randint(1,100)
user_guess = 0
attempts_done = 0

print("Welcome! to the Number guessing Game!")
print("I'm thinking of a number between 1 and 100....")

while user_guess != comps_secret_num:
    user_guess = int(input("Enter your Guess:"))
    attempts_done += 1

    if user_guess > comps_secret_num:
        print("Too high! Try again.")

    elif user_guess < comps_secret_num:
        print("Too low! Try again.")

    else:
        print(f"Correct! You guessed it in {attempts_done} attempts!")