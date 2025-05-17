from turtle import Turtle
from food import Food
class Snake:
    def __init__(self):
        self.snake_struct = []
        x_coord = 0
        for i in range(0,3):
            snake = Turtle(shape = "square")
            snake.penup()
            snake.color("white")
            
            snake.goto(x_coord,0)
            x_coord-=20
            self.snake_struct.append(snake)
        self.head = self.snake_struct[0]    
    def movement(self):
        for i in range(len(self.snake_struct)-1,0,-1):
            self.snake_struct[i].goto(self.snake_struct[i-1].pos())
        self.head.forward(20)
    def up(self):
        if(self.head.heading()!=270):
            self.head.setheading(90)
    def down(self):
        if(self.head.heading()!=90):
            self.head.setheading(270)    
    def right(self):
        if(self.head.heading()!=180):
            self.head.setheading(0) 
    def left(self):
        if(self.head.heading()!=0):
            self.head.setheading(180)
    def extend(self):
        new_snake = Turtle(shape = "square")
        new_snake.penup()
        new_snake.color("white")
        curr_x = self.snake_struct[len(self.snake_struct)-1].xcor()
        curr_y = self.snake_struct[len(self.snake_struct)-1].ycor()
        if(self.head.heading()==90):
            new_snake.goto(curr_x,curr_y-20)
        elif(self.head.heading()==0):
            new_snake.goto(curr_x-20,curr_y)
        elif(self.head.heading()==270):
            new_snake.goto(curr_x,curr_y+20)
        elif(self.head.heading()==180):
            new_snake.goto(curr_x+20,curr_y)
        self.snake_struct.append(new_snake)                    
    def self_collision(self):
        for i in range(1,len(self.snake_struct)):
            if(self.snake_struct[i].distance(self.head)<15):
                return True
                        