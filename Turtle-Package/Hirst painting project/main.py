import colorgram
import turtle
import random


timmy=turtle.Turtle()
timmy_screen=turtle.Screen()
timmy_screen.colormode(255)
timmy.penup()
timmy.hideturtle()

colors = colorgram.extract('image/colourgm.jpg', 50)
rgb_colors=[]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    rgb_tup=(r,g,b)
    rgb_colors.append(rgb_tup)

timmy.setheading(220)
timmy.forward(400)
timmy.setheading(0)
timmy.speed("fastest")
number_of_dots=100

for dot_count in range(1,number_of_dots+1):

    timmy.dot(20, random.choice(rgb_colors))
    timmy.penup()
    timmy.forward(50)
    timmy.dot(20, random.choice(rgb_colors))

    if dot_count%10==0:
        timmy.left(90)
        timmy.forward(50)
        timmy.left(90)
        timmy.forward(500)
        timmy.setheading(0)




timmy_screen.exitonclick()
