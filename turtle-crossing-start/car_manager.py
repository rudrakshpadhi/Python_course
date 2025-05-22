COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
TOP = 250
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3
GEN_SPEED = 800
from turtle import Turtle
import random
class CarManager():
    def __init__(self,screen,player):
        self.moving_cars = []
        self.y_cords = []
        self.screen = screen
        self.player = player
        self.cnt = 0
        self.current_speed = STARTING_MOVE_DISTANCE
        self.increment = MOVE_INCREMENT
        start = TOP
        self.generate_speed = GEN_SPEED
        while(start>-230):
            start-=20
            self.y_cords.append(start)   
        self.generateRandomCars()
        self.startMoving() 
    def generateRandomCars(self):
        random_y = random.choice(self.y_cords)   
        car = Turtle(shape = "square")
        car.color(random.choice(COLORS))   
        car.penup()
        car.goto(320,random_y)   
        car.shapesize(stretch_wid=1,stretch_len=2.5)
        self.moving_cars.append(car)
        car.right(180)
        car.screen.ontimer(self.generateRandomCars,self.generate_speed) 
    def startMoving(self):
        for car in self.moving_cars:
            car.forward(self.current_speed)
            if(self.isCollision(car)):
                self.gameOver()
        self.screen.ontimer(self.startMoving,100)  
    def isCollision(self,car):
        x_dif = abs(self.player.xcor()-car.xcor())
        y_dif = abs(self.player.ycor()-car.ycor())
        if(x_dif<40 and y_dif<30):
            self.gameOver()
    def increaseSpeed(self):
        self.current_speed+=self.increment
        self.generate_speed-=100 
    def gameOver(self):
        writer = Turtle()
        writer = Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(0, 0)
        writer.write("Game Over", align="center", font=("Arial", 24, "bold"))
        self.screen.ontimer(lambda: None, 1000000)
        self.screen.bye()
        
        
