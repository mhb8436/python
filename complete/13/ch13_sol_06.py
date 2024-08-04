import turtle
import json

coordinates = []
t = turtle.Turtle()
screen = turtle.Screen()

def add_point(x, y):
    coordinates.append((x, y))
    t.goto(x, y)
    t.dot(5, "red")

screen.onscreenclick(add_point)

def save_coordinates(filename, coords):
    data = {"coordinates": [{"x":x, "y":y} for x, y in coords]}
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def save_points():
    save_coordinates('points.json', coordinates)
    print('Points saved to points.json')

def read_coordinates(filename):
    try:
        file = open(filename, 'r')
        data = json.load(file)
        coords = [(point['x'], point['y']) for point in data['coordinates']]
        return coords
    except FileNotFoundError as e:
        print('read_coordinates error', e)
        return []
    else:
        print(f"successfully read file {filename}")
    finally:
        file.close()

def load_points():
    global coordinates
    coordinates = read_coordinates('points.json')
    t.clear()
    for x, y in coordinates:
        t.pendown()
        t.goto(x, y)
        t.dot(5, "red")
    print('Points loaded from points.json')

screen.listen()
screen.onkey(save_points, "s")
screen.onkey(load_points, "l")

screen.mainloop()



