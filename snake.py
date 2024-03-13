""" 
calls Turtle class from turtle module
creates a snake object.
"""
from turtle import Turtle
class Snake():
    """ 
    stores every turtle in a list and calls the 'create_body' function,
    to create 3 turtles next to each other.
    """
    def __init__(self) -> None:
        self.body_list = []
        self.create_body()
    def create_body(self):
        """
        initial function after creating a snake object, 3 turtles next to each other.
        """
        for index in range(3):
            new_body=Turtle(shape="square")
            new_body.color("white")
            new_body.penup()
            new_body.goto(x=index*-20, y=0)
            self.body_list.append(new_body)
    def move(self):
        """
        A function gets the first turtle position stored in variables, and passes to the second,
        keep doing this until the last turtle in the turtle list variable. 
        """
        snake_head_xcor = self.body_list[0].xcor()
        snake_head_ycor = self.body_list[0].ycor()
        self.body_list[0].forward(20)
        for body in self.body_list[1:len(self.body_list)]:
            body_head_xcor = body.xcor()
            body_head_ycor = body.ycor()
            body.goto(x=snake_head_xcor, y=snake_head_ycor)
            snake_head_xcor = body_head_xcor
            snake_head_ycor = body_head_ycor
    def update(self):
        """
        A function adds a new turtle to the tail of the snake. 
        """
        snake_tail_xcor = self.body_list[-1].xcor()
        snake_tail_ycor = self.body_list[-1].ycor()
        new_body=Turtle(shape="square")
        new_body.color("white")
        new_body.penup()
        new_body.goto(snake_tail_xcor , snake_tail_ycor)
        self.body_list.append(new_body)


    def turn_left(self):
        """
        A function changes the direction of the snake to the left if the direction is not right.
        """
        if self.body_list[0].heading() != 0:
            self.body_list[0].setheading(180)
    def turn_right(self):
        """
        A function changes the direction of the snake to right, if the direction is not left.
        """
        if self.body_list[0].heading() != 180:
            self.body_list[0].setheading(0)
    def up(self):
        """
        A function changes the direction of the snake to up, if the direction is not down.
        """
        if self.body_list[0].heading() != 270:
            self.body_list[0].setheading(90)
    def down(self):
        """
        A function changes the direction of the snake to down, if the direction is not up.
        """
        if self.body_list[0].heading() != 90:
            self.body_list[0].setheading(270)

    def tail_collision(self):
        """
        A function checks the head of the snake distance to the body apart from itself.
        """
        result = False
        snake_head = self.body_list[0]
        next_body = 1
        end_body = len(self.body_list)-1
        while next_body <= end_body:
            #checking the distance from index 1 to the last index in the body list.
            if snake_head.distance(self.body_list[next_body]) < 15:
                result = True
                break
            next_body +=1
        return result
# End-Of-Line (EOL)