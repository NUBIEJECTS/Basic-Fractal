# importing the module
from turtle import *

# creating window and defining attributes
window = Screen()
window.screensize(canvwidth=500, canvheight=50, bg="black")
window.title("Basic fractal")

# creating a turtle object and defining attributes
paint = Turtle()
paint.color("white")
paint.speed(0)
paint.fillcolor("blue")

# drawing shapes
paint.begin_fill()
for i in range(4):
    paint.forward(200)
    paint.left(90)
paint.end_fill()

# putting screen into a loop
mainloop()