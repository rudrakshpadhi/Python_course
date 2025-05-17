from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.color("yellow")
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.updateScore()
    def updateScore(self):   
        self.score+=1 
        self.clear()
        self.write(f"Current Score: {self.score-1}", align = 'center',font=('Comic-Sans', 12, 'normal'))
    def GameOver(self):    
        self.goto(0,0)
        self.write(f"GAME OVER", align = 'center',font=('Comic-Sans', 20, 'normal'))
        
        