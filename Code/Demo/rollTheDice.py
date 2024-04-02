import turtle
import random
turtle.speed(0)
color = ['red','yellow','green','blue','pink','cyan']
dice_color = random.choice(color)
turtle.color(dice_color)
turtle.begin_fill()
for n in range(4):
    turtle.fd(100)
    turtle.rt(90)
turtle.end_fill()
turtle.pu()
d = random.randint(1,6)
turtle.color('white')
turtle.goto(30,-80)
turtle.write(d,font=('arial',60,'normal'))
