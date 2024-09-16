import turtle
def draw_slice(side_length):
    for i in range (3):
        turtle.forward(side_length)
        turtle.left(120)

for i in range (6):
    draw_slice(200)
    turtle.left(60)
turtle.done()

