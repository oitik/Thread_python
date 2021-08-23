import turtle

s = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
s.bgcolor('grey')
color = ['orange']

a = 0
b = 0
t.penup()
t.goto(0, 200)
t.pendown()
while True:
    t.pencolor(color[0])
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b == 210:
        break
    t.hideturtle()

turtle.exitonclick()