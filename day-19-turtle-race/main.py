from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

color = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []
y = -175

for n in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[n])
    y += 50
    new_turtle.goto(-230, y)
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!")
            else:
                print(f"You've lost")

        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)





screen.exitonclick()