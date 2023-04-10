from turtle import Turtle
STARTING_POSTIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        segments = []
        for positon in starting_positions:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(positon)
            self.segments.append(new_segment)


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.segments[0].setheading(UP)

    def  down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)


    def  left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def  right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

