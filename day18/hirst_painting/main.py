import turtle 
from turtle import Turtle,Screen
import random
import colorgram
# colors = colorgram.extract('pic.jpg',15)
# print(colors[0].rgb)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))
# print(rgb_colors)    
color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251)]
screen = Screen()
screen.setup(width=800,height=600)
turtle.colormode(255)
tim = Turtle()
tim.penup()
tim.goto(-400,-300)
tim.speed(0)
tim.hideturtle()
for i in range(0,10):
    if(i%2==0):
        for j in range(0,10):
            tim.pendown()
            tim.dot(20,random.choice(color_list))
            tim.penup()
            tim.forward(66.67)
        tim.left(90)
        tim.forward(66.67)
    else:
        tim.left(90)
        tim.forward(66.67)
        for j in range(0,10):
            tim.pendown()
            tim.dot(20,random.choice(color_list))
            tim.penup()
            tim.forward(66.67)
        tim.right(90)
        tim.forward(66.67)  
        tim.right(90)
        tim.forward(66.67)  

screen.exitonclick()