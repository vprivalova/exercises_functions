import turtle as t


def triangle(x1, y1, x2, y2, x3, y3, color):
    t.pencolor('black')
    t.pensize(1)
    t.speed(11)
    t.goto(x1, y1)
    t.pd()
    t.fillcolor(color)
    t.begin_fill()
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.end_fill()
    t.pu()


def square(x1, y1, x2, y2, x3, y3, x4, y4, color_d, color_u):
    t.setheading(90)
    triangle(x1, y1, x2, y2, x3, y3, color_d)
    triangle(x3, y3, x4, y4, x1, y1, color_u)


dark = '#000080'
middle = '#87CEFA'
light = '#E0FFFF'

#1 quater
square(0, 0, 0, -50, 50, -50, 50, 0, middle, dark)
square(50, 0, 50, -50, 100, -50, 100, 0, dark, middle)
square(100, 0, 100, -50, 150, -50, 150, 0, middle, light)

square(0, -50, 0, -100, 50, -100, 50, -50, light, middle)
square(50, -50, 50, -100, 100, -100, 100, -50, middle, dark)
square(100, -50, 100, -100, 150, -100, 150, -50, dark, middle)

square(0, -100, 0, -150, 50, -150, 50, -100, middle, light)
square(50, -100, 50, -150, 100, -150, 100, -100, light, middle)
square(100, -100, 100, -150, 150, -150, 150, -100, middle, dark)

#2 quater
square(0, -200, 0, -150, 50, -150, 50, -200, middle, light)
square(50, -200, 50, -150, 100, -150, 100, -200, light, middle)
square(100, -200, 100, -150, 150, -150, 150, -200, middle, dark)

square(0, -250, 0, -200, 50, -200, 50, -250, light, middle)
square(50, -250, 50, -200, 100, -200, 100, -250, middle, dark)
square(100, -250, 100, -200, 150, -200, 150, -250, dark, middle)

square(0, -300, 0, -250, 50, -250, 50, -300, middle, dark)
square(50, -300, 50, -250, 100, -250, 100, -300, dark, middle)
square(100, -300, 100, -250, 150, -250, 150, -300, middle, light)

#3 quater
square(150, -50, 150, 0, 200, 0, 200, -50, light, middle)
square(200, -50, 200, 0, 250, 0, 250, -50, middle, dark)
square(250, -50, 250, 0, 300, 0, 300, -50, dark, middle)

square(150, -100, 150, -50, 200, -50, 200, -100, middle, dark)
square(200, -100, 200, -50, 250, -50, 250, -100, dark, middle)
square(250, -100, 250, -50, 300, -50, 300, -100, middle, light)

square(150, -150, 150, -100, 200, -100, 200, -150, dark, middle)
square(200, -150, 200, -100, 250, -100, 250, -150, middle, light)
square(250, -150, 250, -100, 300, -100, 300, -150, light, middle)

#4 quater
square(150, -150, 150, -200, 200, -200, 200, -150, dark, middle)
square(200, -150, 200, -200, 250, -200, 250, -150, middle, light)
square(250, -150, 250, -200, 300, -200, 300, -150, light, middle)

square(150, -200, 150, -250, 200, -250, 200, -200, middle, dark)
square(200, -200, 200, -250, 250, -250, 250, -200, dark, middle)
square(250, -200, 250, -250, 300, -250, 300, -200, middle, light)

square(150, -250, 150, -300, 200, -300, 200, -250, light, middle)
square(200, -250, 200, -300, 250, -300, 250, -250, middle, dark)
square(250, -250, 250, -300, 300, -300, 300, -250, dark, middle)


t.mainloop()
