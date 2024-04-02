import turtle as t
t.speed(0)
for p in range(24):
    t.rt(15)
    for s in range(36):
        t.lt(10)
        t.fd(15)

t.penup()
t.bk(200)
t.write('Polygon Using Python Turtle Graphics')
t.bk(50)
t.write('Made By Muhammed Mohsin(mdev1836)')
