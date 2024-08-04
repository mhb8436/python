import turtle

class Shape:
    def __init__(self, t, color, length):
        self.t = t
        self.color = color
        self.length = length

    def draw(self):
        pass

    def move_to(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()


class Triangle(Shape):
    def __init__(self, t, color, length):
        super().__init__(t, color, length)
        self.angle = 120
    
    def draw(self):
        self.t.color(self.color)
        for _ in range(3):
            self.t.forward(self.length)
            self.t.right(self.angle)

class Square(Shape):
    def __init__(self, t, color, length):
        super().__init__(t,color,length)
        self.angle = 90
    
    def draw(self):
        self.t.color(self.color)
        for _ in range(4):
            self.t.forward(self.length)
            self.t.right(self.angle)


t = turtle.Turtle()
t.speed(3)

t1 = Triangle(t, "red", 100)
t1.move_to(-100, 0)
t1.draw()

t2 = Square(t, "blue", 200)
t2.move_to(200, 0)
t2.draw()

turtle.exitonclick()