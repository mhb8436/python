import turtle

t= turtle.Turtle()
t.shape("turtle")

for i in range(11):    
    t.circle(20)

    t.up()
    t.goto(i*30, 0)
    t.down()

turtle.exitonclick()


