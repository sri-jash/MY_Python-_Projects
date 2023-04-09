import random
from turtle import Turtle ,Screen

screen =Screen()
is_race_on = False
screen.setup(width=500,height=400)
# positional arguments

# textinput is gonna show the pop up window
user_bet=screen.textinput(title="Make Your Bet!",prompt="Which turtle will win the race? Enter a color:")
colors =["red","orange","violet","Indigo","blue","green","yellow"]
y_positions =[-70,-40,-10,20,50,80]
all_turtles=[]
for turtle_index in range(0,6):

    new_turtle =Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)



if user_bet:
        is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        winning_color =turtle.pencolor()
        if turtle.xcor()>250:
            is_race_on=False
            if winning_color == user_bet:
                print(f"you've won! The {winning_color} turtle is the winner!")
            else:
                print(f"you've Lost! The {winning_color} turtle is the winner!")

        rand_distance= random.randint(0,10)
        turtle.forward(rand_distance)




screen.exitonclick()
