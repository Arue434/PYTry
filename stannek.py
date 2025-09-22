import turtle

print("gambar segitiga")

segitiga = turtle.Turtle()

segitiga.fillcolor("green")
segitiga.begin_fill()

for i in range (5):
    segitiga.forward(150)
    segitiga.right(144)

segitiga.end_fill()

print ("persegi")
persegi = turtle.Turtle()
persegi.penup()
persegi.goto(200, 0)
persegi.pendown()

persegi.fillcolor("blue")
persegi.begin_fill()
for i in range(4):
    persegi.forward(100)
    persegi.right(90)
persegi.end_fill()

turtle.done()