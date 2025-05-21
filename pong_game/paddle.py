from turtle import Turtle
STARTING_POS = [-570,570]
class Paddle():
    def __init__(self,type):
        self.paddle_struct = []
        self.makePaddle(type)
    def makePaddle(self,type):
        offset = 0
        for i in range(0,5):
            padding_part = Turtle(shape="square")
            padding_part.penup()
            padding_part.color("white")
            padding_part.goto((STARTING_POS[type],offset))
            self.paddle_struct.append(padding_part)
            padding_part.left(90)
            offset+=20
    def paddle_up(self):
        self._move_paddle(20)
    
    def paddle_down(self):
        self._move_paddle(-20)

    def _move_paddle(self, distance):
        base_x = self.paddle_struct[0].xcor()
        base_y = self.paddle_struct[0].ycor() + distance
        for i, part in enumerate(self.paddle_struct):
            part.goto(base_x, base_y + i * 20)
