from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
b = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    b.move()
    # b.speed=0.1

    #Detect collision with wall
    if b.ycor() > 280 or b.ycor() < -280:
        b.bounce_y()

    #Detect collision with paddle
    if b.distance(r_paddle) < 50 and b.xcor() > 320 or b.distance(l_paddle) < 50 and b.xcor() < -320:
        b.bounce_x()

    #Detect R paddle misses
    if b.xcor() > 380:
        b.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses:
    if b.xcor() < -380:
        b.reset_position()
        scoreboard.r_point()

screen.exitonclick()