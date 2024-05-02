# Create a snake body
# Move the snake 
# Create the snake food
# Detect collision with food
# Create a scoreboard
# Detect collision with wall
# Detect collsion with tail
# from turtle import Screen,Turtle
# import time
# from food import Food
# from snake import Snake
# from scoreboard import Scoreboard

# screen=Screen()
# screen.setup(width=600,height=600)
# screen.bgcolor("black")
# screen.title("Snake Game")
# screen.tracer(0)

# # tom=Turtle("square")
# # tom.color("white")


# # om=Turtle("square")
# # om.color("white")
# # om.goto(-40,0)
# # 1st task completed

# starting_position=[(0,0),(-20,0),(-40,0)]
# segments=[]
# for position in starting_position:
    
#     tim=Turtle("square")
#     tim.color("white")
#     tim.penup()
#     tim.goto(position)
#     segments.append(tim)

# game_is_on=True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     for seg in range(len(segments)-1, 0,-1):
#         new_x=segments[seg-1].xcor()#pichla wala segment agle wala ki position le lega
#         new_y=segments[seg-1].ycor()
#         segments[seg].goto(new_x,new_y)
#     segments[0].fd(20)

# # 2nd task 
# # move the snake












from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()





screen.exitonclick()
