import turtle
from turtle import Turtle,Screen
import random
colors = ["red","green","yellow","blue","violet","orange"]
screen = Screen()
screen.setup(height=600,width=1000)
screen.title("Turtle racing game")
user_color = screen.textinput("turtle game","Enter the color of the turtle that will win: ")
turtles = []
distances = []
movement = []
y_cord = 150
for color in colors:
    curr_turtle = Turtle(shape="turtle")
    curr_turtle.penup()
    curr_turtle.color(color)
    curr_turtle.speed(10)
    curr_turtle.goto(-475,y_cord)
    turtles.append(curr_turtle)
    distances.append(0)
    movement.append(True)
    y_cord-=50
race_on = True
while(race_on):   
    for curr_turtle in turtles:
        random_dist = random.randint(0,10)
        curr_turtle.forward(random_dist)
        if(curr_turtle.pos()[0]>=480):
            if(curr_turtle.color()[0]==user_color):
                print("Your turtle has won! ")
            else:
                
                print(f"Your turtle has lost. The {curr_turtle.color()[0]} turtle has won.")    
            race_on = False   
screen.bye()                     
# screen.exitonclick()