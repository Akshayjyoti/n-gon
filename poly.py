import turtle
import time

t = turtle.Turtle()

n = int(input("Enter number of sides: "))
l = int(input("Enter length of each side: "))

for _ in range(n):
    turtle.forward(l)
    turtle.right(360/n)
    time.sleep(1)

time.sleep(10)
