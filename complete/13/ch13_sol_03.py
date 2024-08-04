import turtle

class TurtleManager():
    def __init__(self, color, shape, start_x, start_y):
        self.t = turtle.Turtle()
        self.color = color
        self.shape = shape
        self.t.penup()
        self.t.goto(start_x, start_y)
        self.t.pendown()

    def draw_shape(self, length):
        self.t.color(self.color)
        if self.shape == 'circle':
            self.t.circle(length)
        elif self.shape == 'square':
            for _ in range(4):
                self.t.forward(length)
                self.t.right(90)
        elif self.shape == 'triangle':
            for _ in range(3):
                self.t.forward(length)
                self.t.right(120)
    
    def move_to(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()


t1 = TurtleManager("blue", "square", -100, 0)
t1.draw_shape(100)
t1.move_to(100, 0)
t1.draw_shape(50)

t2 = TurtleManager("orange", 'circle', 0, -100)
t2.draw_shape(100)
t2.move_to(100,0)
t2.draw_shape(50)


turtle.exitonclick()



