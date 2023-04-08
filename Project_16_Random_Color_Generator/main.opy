import random
import turtle as turtle_module
turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list =[(253, 251, 248), (254, 250, 252),(232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229,17, 121), (73, 9, 31), (60,14, 8), (224, 141, 211), (10, 97,61), (221,160, 9), (17, 18, 43), (46, 214, 232), (11, 227,239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]
tim.penup()
tim.hideturtle()
tim.speed('fastest')
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots =100
for dot_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count%10==0:

        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)






screen =turtle_module.Screen()
screen.exitonclick()
