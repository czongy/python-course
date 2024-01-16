import random
import time

shapes = "---'   ____)____
          ______)
          _______)
         _______)
---.__________)"
print(shapes)


while True:
    random.seed(random.randint(1, 100))

    print("\nWelcome to Rock Paper Scissor. Choose \"1\" for rock, \"2\" for paper and \"3\" for scissor.")
    user_input = int(input("What is your choice? "))
    comp_choice = random.randint(1, 3)
    choices = ["rock", "paper", "scisssor"]

    print(f"You choose {choices[user_input-1]}")
    time.sleep(1)
    print(f"Computer choose {choices[comp_choice-1]}")
    time.sleep(1)
    result = user_input - comp_choice

    if user_input <= 0 or user_input > 3:
        print("Out of range. You lose!")
    elif user_input == comp_choice:
        print("It's a tie!")
    elif result == -1 or result ==2:
        print("You lose!")
    else:
        print("You win!")

    to_continue = input("Type \"y\" to continue or \"n\" to exit program: ")
    if to_continue.lower() == "n":
        break
    