from turtle import Turtle,Screen
from snake import Snake
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


""" Upto this Created Snake Body """
# ____________________________________________________________________________________________
""" From Now we will create the Animations """
snake =Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

# __________________________________________________________________________________
""" Upto this we made the tail to follow the head"""

screen.exitonclick()
