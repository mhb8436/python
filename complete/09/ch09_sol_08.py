import turtle

polygons = {
    'triangle': {
        'color':'red', 'sides': 3, 'length': 100,
    },
    'square': {
        'color':'blue', 'sides': 4, 'length': 100,
    },
    'pentagon': {
        'color':'green', 'sides': 5, 'length': 100,
    },
    'hexagon': {
        'color':'purple', 'sides': 6, 'length': 100,
    },
}

for name, settings in polygons.items():
    t = turtle.Turtle()
    t.color(settings['color'])
    t.penup()
    t.goto(0,0)
    t.pendown()
    angle = 360 / settings['sides']
    for _ in range(settings['sides']):
        t.forward(settings['length'])
        t.right(angle)

turtle.exitonclick()    

