from turtle import Turtle
from random import randint, choice


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.collection = []

    def create_car(self):
        if len(self.collection) < 50:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.goto(randint(320, 1520), randint(-250, 250))
            self.collection.append(new_car)

    def move_car(self, level):
        for car in self.collection:
            if car.xcor() > -320:
                new_x = car.xcor() - STARTING_MOVE_DISTANCE * level
                car.goto(new_x, car.ycor())
            else:
                self.collection.remove(car)


