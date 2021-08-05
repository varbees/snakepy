from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snakehead = self.segments[0]

    def create_snake(self):
        # Creating initial snake
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, location):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(location)
        self.segments.append(new_segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())  

    def move(self):
        # Moving the last segment to its front segment place in for loop all the way to first segment
        for seg_num in range(len(self.segments) - 1, 0, -1):
            front_seg_x, front_seg_y = self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(front_seg_x, front_seg_y)
        self.snakehead.forward(MOVE_DISTANCE)

    def up(self):
        if self.snakehead.heading() != DOWN:
            self.snakehead.setheading(UP)
    
    def down(self):
        if self.snakehead.heading() != UP:
            self.snakehead.setheading(DOWN)

    def left(self):
        if self.snakehead.heading() != RIGHT:
            self.snakehead.setheading(LEFT)

    def right(self):
        if self.snakehead.heading() != LEFT:
            self.snakehead.setheading(RIGHT)

    # def space(self):
    #     if self.keyboard.is_pressed('space'):
    #         return True
    #     else:
    #         return False