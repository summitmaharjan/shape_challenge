from turtle import Turtle, Screen

s = Turtle()

# for Triangel
for _ in range(3):
    s.forward(100)
    s.right(120)

# for square
for _ in range(4):
    s.forward(100)
    s.right(90)

# for pentagon
for _ in range(5):
    s.forward(100)
    s.right(72)

# for hexagon
for _ in range(6):
    s.forward(100)
    s.right(60)

# for heptagon
for _ in range(7):
    s.forward(100)
    s.right(51.42)

# for octagon
for _ in range(8):
    s.forward(100)
    s.right(45)

# for nonagon
for _ in range(9):
    s.forward(100)
    s.right(40)

# for decagon
for _ in range(10):
    s.forward(100)
    s.right(36)


screen = Screen()
screen.exitonclick()
