STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.right(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.right(180)
    def moveUp(self):
        self.forward(10) 
    def reachedFinish(self):
        if(self.ycor()>280):
            return True 
    def return_pos(self):
        self.goto(STARTING_POSITION)      

