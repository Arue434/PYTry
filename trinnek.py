import turtle

print("gambar segitiga")

screen = turtle.Screen()
segitiga = turtle.Turtle()

segitiga.fillcolor("green")
segitiga.begin_fill()

for i in range (3):
    segitiga.forward(180)
    segitiga.left(120)

segitiga.end_fill()

print ("lingkaran")

lingkaran = turtle.Turtle()

lingkaran.penup()
lingkaran.goto(-200, 0)
lingkaran.pendown()

lingkaran.fillcolor("red")
lingkaran.begin_fill()

lingkaran.circle(75)
lingkaran.end_fill()

turtle.done()