# importing turlte
from turtle import *

# creating window
window = Screen()
window.bgcolor("black")

# creating a turtle object
paint = Turtle()
paint.speed(0)
paint.color("white")

# drawing the fractal
def polygon(side, side_len):
    # creating shape
    for i in range(side):
        paint.forward(side_len)
        paint.left(360/side)
    side_len-=1
    paint.forward(10)
    paint.left(2)
    # condition to call the function again
    if side_len>=0:
        polygon(side, side_len)
    return

# calling the function
polygon(9, 60)

# putting screen into loop
mainloop()