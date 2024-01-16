import art
import game_data
import random
import os


def get_data(prev):
    if prev is None:
        return random.choice(game_data.data)
    
    new = random.choice(game_data.data)
    while new == prev:
        new = random.choice(game_data.data)
    
    return new

def question(a, b):
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(art.vs)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.")
    return input("Who has more followers? Type 'A' or 'B': ").lower()

def check(user, a, b, score):
    if a['follower_count'] > b['follower_count']:
        answer = "a"
    else:
        answer = "b"

    if user != answer:
        print(f"Sorry, that's wrong. Final score: {score}")
        return True
    else:
        score += 1
        print(art.logo)
        print(f"You're right! Current score: {score}.")
        return False

def game():
    print(art.logo)
    data_b = get_data(None)
    game_over = False
    score = 0

    while not game_over:
        data_a = data_b
        data_b = get_data(data_a)

        user_answer = question(data_a, data_b)
        os.system('cls')
        game_over = check(user_answer, data_a, data_b, score)
        
game()

