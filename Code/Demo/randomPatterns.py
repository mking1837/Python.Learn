import turtle
import random

cols = ['blue','red','green','yellow','pink','purple','orange','cyan']

for c in range(200):
    turtle.pensize(10)
    x = random.randint(-100,100)
    y = random.randint(-100,100)
    turtle.color(random.choice(cols))
    turtle.goto(x,y)
