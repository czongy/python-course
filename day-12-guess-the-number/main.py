import art
import random

def diff(difficulty):
    if difficulty == "easy":
        return 10
    else:
        return 5
    
def check(guess, answer):
    if guess == answer:
        print(f"You got it! The answer was {answer}")
        return True
    elif guess < answer:
        print("Too low.")
    elif guess > answer:
        print("Too high.")
    return False

def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    attempt = diff(difficulty)
    answer = random.randint(1, 100)

    while attempt != 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        isCorrect = check(user_guess, answer)
        if not isCorrect:
            attempt -= 1
            print("Guess Again.")
        elif isCorrect:
            break

    if attempt == 0:
        print("You've run out of guesses, you lose.")

game()