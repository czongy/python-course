############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import art
import random
import os

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def cal_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player, npc):
    if player == npc:
        return "Draw 🙃"
    elif player == 0:
        return "Win with a Blackjack 😎"
    elif npc == 0:
        return "Lose, opponent has Blackjack 😱"
    elif player > 21:
        return "You went over. You lose 😭"
    elif npc > 21:
        return "Opponent went over. You win 😁"
    elif player > npc:
        return "You win 😃"
    else:
        return "You lose 😤"

def game():
    print(art.logo)

    player_card = []
    npc_card = []
    is_over = False

    for _ in range(2):
        player_card.append(deal_card())
        npc_card.append(deal_card())

    while not is_over:
        player_score = cal_score(player_card)
        npc_score = cal_score(npc_card)

        print(f"Your cards: {player_card}, current score: {player_score}")
        print(f"Computer's first card: {npc_card[0]}")

        if player_score == 0 or npc_score == 0 or player_score > 21:
            is_over = True
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                player_card.append(deal_card())
            else:
                is_over = True
    
    while npc_score != 0 and npc_score < 17:
        npc_card.append(deal_card())
        npc_score = cal_score(npc_card)
    
    print(f"Your final hand: {player_card}, final score: {player_score}")
    print(f"Computer's final hand: {npc_card}, final score: {npc_score}")
    print(compare(player_score, npc_score))


while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == "y":
    os.system('cls')
    game()

