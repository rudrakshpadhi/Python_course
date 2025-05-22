FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 1
        self.penup()
        self.hideturtle()
        self.goto(-240,260)
        self.write(f"Level: {self.points}", align="center", font=("Arial", 15, "bold"))
    def updateLevel(self):
        self.points+=1 
        self.clear()
        self.write(f"Level: {self.points}", align="center", font=("Arial", 15, "bold"))  
    def displayGameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "bold"))    
    
