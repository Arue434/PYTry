import turtle

print("gambar persegi")

kotak = turtle.Turtle()

kotak.fillcolor("blue")
kotak.begin_fill()

# kotak.forward(100)
# kotak.right(90)
# kotak.forward(100)
# kotak.right(90)
# kotak.forward(100)
# kotak.right(90)
# kotak.forward(100)
# kotak.right(90)

for i in range(4):
    kotak.forward(100)
    kotak.right(90)

kotak.end_fill()

turtle.done()
