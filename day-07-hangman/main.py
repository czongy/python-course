import hangman_art
import hangman_words
import random

def game():
    word = random.choice(hangman_words.word_list)
    user_guess = ["_" for x in word]
    guessed_words = []
    wrong_count = 6

    print(hangman_art.logo)
    print(hangman_art.stages[wrong_count])
    print(' '.join(user_guess))

    while "_" in user_guess and wrong_count != 0:
        user_letter = input("Guess a letter: ").lower()

        if user_letter not in word:
            guessed_words.append(user_letter)
            wrong_count -= 1
        elif user_letter in guessed_words or user_letter in user_guess:
            print("\nYou have already guessed this letter. Please try again.")
        else: 
            for i in range(len(word)):
                if user_letter == word[i]:
                    user_guess[i] = user_letter

        print(hangman_art.stages[wrong_count])    
        print(f"Guessed words: {','.join(guessed_words)}")
        print(' '.join(user_guess))

    if "_" not in user_guess:
        print("\nYou got the answer~!")
    else:
        print(f"\nGame Over~! The answer is {word}")
    
    next_game = input("\nNext game? (y/n)\n")
    if next_game.lower() == "y":
        game()

game()

