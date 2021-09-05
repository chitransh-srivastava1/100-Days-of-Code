import turtle

tom=turtle.Turtle()
tom_screen=turtle.Screen()

def move_forward():   
    tom.forward(20)

def move_backward():
    tom.backward(20)

def counter_clock_mov():
    tom.left(15)

def clock_mov():
    tom.right(15)

def clear_screen():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()

tom_screen.listen()
tom_screen.onkey(fun=move_forward,key="w")
tom_screen.onkey(fun=move_backward,key="s")
tom_screen.onkey(fun=counter_clock_mov,key="a")
tom_screen.onkey(fun=clock_mov,key="d")
tom_screen.onkey(fun=clear_screen,key="c")


tom_screen.exitonclick()
