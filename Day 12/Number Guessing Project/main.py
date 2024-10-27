from art2 import logo
import random
def game():
    print(logo)
    number_to_guess = random.randint(0,100)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty_level=="easy":
        attempts_remaining = 10
    elif difficulty_level=="hard":
        attempts_remaining = 5

    while attempts_remaining>0:
        print(f"You have {attempts_remaining} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number_to_guess:
            print(f"You got it! The answer was {number_to_guess}.")
            break
        elif guess>number_to_guess:
            print("Too high.")
        elif guess<number_to_guess:
            print("Too low.")
        attempts_remaining-=1
        if attempts_remaining ==0:
            print("You've run out of guesses, you lose.")
            break
        print("Guess again.")
game()