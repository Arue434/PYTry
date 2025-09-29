import turtle as lel

print("gambar lingkaran")
screen = lel.Screen()

lingkaran = lel.Turtle()
lingkaran.fillcolor("red")

lingkaran.begin_fill()
lingkaran.circle(100)
lingkaran.end_fill()

lingkaran.penup()
lingkaran.speed(0)
lingkaran.goto(0,0)

def move_up():
    lingkaran.setheading(90)
    lingkaran.forward(10)

def move_down():
    lingkaran.setheading(270)
    lingkaran.forward(10)

def move_left():
    lingkaran.setheading(180)
    lingkaran.forward(10)

def move_right():
    lingkaran.setheading(0)
    lingkaran.forward(10)

screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.mainloop()
