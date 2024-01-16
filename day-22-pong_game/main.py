from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from score import Score, Centerline

WIDTH = 380
HEIGHT = 280
DIST_TO_PADDLE = 55
DIST_TO_XCOR = 320

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

score = Score()
centerline = Centerline()

ball = Ball()

game_is_on = True
while game_is_on:
    screen.update()
    sleep(ball.move_speed)
    ball.move_ball()

    if ball.distance(l_paddle) < DIST_TO_PADDLE and ball.xcor() < -DIST_TO_XCOR or ball.distance(r_paddle) < \
            DIST_TO_PADDLE and ball.xcor() > DIST_TO_XCOR:
        ball.bounce_paddle()

    if ball.ycor() > HEIGHT or ball.ycor() < -HEIGHT:
        ball.bounce_wall()

    if ball.xcor() > WIDTH:
        score.increase_l_score()
        ball.reset()

    elif ball.xcor() < -WIDTH:
        score.increase_r_score()
        ball.reset()


screen.exitonclick()
