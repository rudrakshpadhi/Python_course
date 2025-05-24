from turtle import Turtle,Screen

import random
class Ball():
    def __init__(self,paddles,screen):
        self.ball = Turtle(shape="circle")
        self.ball.speed(1)
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0,random.randint(-150,150))
        self.paddles = paddles
        self.screen = screen
        self.random_turn()
        self.movement()
    def random_turn(self):
        self.ball.setheading(random.randint(135,225))     
    def movement(self):
        self.wallCollision()
        self.paddleCollision()
        self.GameOver()
        self.ball.forward(5)
        self.screen.update()
        self.screen.ontimer(self.movement, 13)
    def wallCollision(self):
        y_pos = self.ball.ycor()
        if(y_pos>340 or y_pos<-330):
            angle = self.ball.heading()
            new_heading = (360-angle+random.randint(-10,10))%360
            self.ball.setheading(new_heading)
    def paddleCollision(self): 
        first_paddle = self.paddles[0]
        second_paddle = self.paddles[1]
        bx, by = self.ball.xcor(), self.ball.ycor()
        for part in first_paddle.paddle_struct:
            px, py = part.xcor(), part.ycor()
            if abs(bx - px) < 20 and abs(by - py) < 10:
                print("paddle 1 has hit")
                self.ball.setheading((180 - self.ball.heading() + random.randint(-10, 10)) % 360)
                return  
        for part in second_paddle.paddle_struct:
            px, py = part.xcor(), part.ycor()
            if abs(bx - px) < 20 and abs(by - py) < 10:
                print("paddle 2 has hit")
                self.ball.setheading((180 - self.ball.heading() + random.randint(-10, 10)) % 360)
                return
    def GameOver(self):
        if(self.ball.xcor()<-600):
            msg = Turtle()
            msg.hideturtle()
            msg.color("red")
            msg.penup()
            msg.goto(0, 0)
            msg.write("GAME OVER. PLAYER 2 HAS WON", align="center", font=("Courier", 36, "bold"))
            self.screen.update()
        elif(self.ball.xcor()>600):
            msg = Turtle()
            msg.hideturtle()
            msg.color("red")
            msg.penup()
            msg.goto(0, 0)
            msg.write("GAME OVER. PLAYER 1 HAS WON", align="center", font=("Courier", 36, "bold"))
            self.screen.update()    
            
