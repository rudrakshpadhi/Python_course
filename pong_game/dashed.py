from turtle import Turtle

class Dashed():
    def __init__(self):
        self.player_tag1 = Turtle()
        self.player_tag2 = Turtle()
        self.player_tag1.color("white")
        self.player_tag2.color("white")
        self.player_tag1.penup()
        self.player_tag2.penup()
        self.player_tag1.goto(-350,200)
        self.player_tag2.goto(350,200)
        self.player_tag1.hideturtle()
        self.player_tag2.hideturtle()
        self.player_tag1.write("PLAYER 1",align = "left", font=("Courier", 20, "bold"))
        self.player_tag2.write("PLAYER 2",align = "left", font=("Courier", 20, "bold"))
        self.down = Turtle()
        self.down.color("white")
        self.up = Turtle()
        self.up.color("white")
        self.up.pensize(5)
        self.down.pensize(5)
        self.up.left(90)
        self.down.right(90)
        self.up.penup()
        self.down.penup()
        self.up.forward(5)
        self.down.forward(5)
        self.dash_lines(self.up)
        self.dash_lines(self.down)
    def dash_lines(self,random_turtle):
        for i in range(0,20):
            random_turtle.pendown()
            random_turtle.forward(10)
            random_turtle.penup()
            random_turtle.forward(10)




