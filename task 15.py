import turtle as t
import random


def frame():
    t.pu()
    t.fillcolor('#1E1E1E')
    t.begin_fill()
    t.goto(-500, 400)
    t.pd()
    t.speed(1000)
    t.fd(1000)
    t.rt(90)
    t.fd(800)
    t.rt(90)
    t.fd(1000)
    t.rt(90)
    t.fd(800)
    t.end_fill()
    t.pu()
    t.goto(0, 0)
    t.rt(90)


def stars():
    for i in range(50):
        x = random.randint(-500, 500)
        y = random.randint(100, 400)
        t.goto(x, y)
        t.pd()
        t.speed(100000000)
        t.pensize(1)
        t.color('#FFFFC2')
        size = 3
        angle = 120
        t.fillcolor('#FFFFC2')
        t.begin_fill()
        for side in range(5):
            t.fd(size)
            t.rt(angle)
            t.fd(size)
            t.rt(72 - angle)
        t.end_fill()
        t.pu()


def rectangle(x, y, a, b, color):
    t.goto(x, y)
    t.pd()
    t.speed(1000)
    t.pensize(1)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.fd(a)
        t.lt(90)
        t.fd(b)
        t.lt(90)
    t.end_fill()
    t.setheading(0)
    t.pu()


def triangle(x, y, a, color):
    t.goto(x, y)
    t.pd()
    t.speed(1000)
    t.pensize(1)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.fd(a)
    t.lt(120)
    t.fd(a)
    t.lt(120)
    t.fd(a)
    t.end_fill()
    t.pu()
    t.setheading(0)


def home1(x, y, color):
    rectangle(x, y, 200, 400, color)
    triangle(x, y + 400, 200, color)


def home2(x, y, a, b, color):
    rectangle(x, y, a, b, color)


def windows():
    for i in range(20):
        x = random.randint(100, 450)
        y = random.randint(-400, 0)
        rectangle(x, y, 20, 10, '#FBB917')

    for j in range(20):
        x = random.randint(-500, -325)
        y = random.randint(-400, 0)
        rectangle(x, y, 15, 15, '#FBB917')

    for m in range(20):
        x = random.randint(-400, 150)
        y = random.randint(-400, -150)
        rectangle(x, y, 30, 10, '#FBB917')


frame()
stars()

home1(100, -400, '#392147')
home1(-500, -400, '#6960EC')
home1(300, -400, '#2554C7')
home2(-400, -400, 500, 300, '#151B54')
home2(50, -400, 400, 200, '#2B3856')
windows()

t.mainloop()
