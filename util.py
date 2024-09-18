import turtle
import math
import random

# Helper function to check if a point is inside the polygon
def point_in_polygon(x, y, polygon):
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

class Lawn:
    def __init__(self, vertices):
        self.vertices = vertices
        self.turtle = turtle.Turtle()
        self.turtle.color("green")
        self.turtle.speed(0)
        self.turtle.ht()
        self.create_polygon()

    def create_polygon(self):
        self.turtle.penup()
        self.turtle.goto(self.vertices[0])
        self.turtle.pendown()
        self.turtle.begin_fill()
        for vertex in self.vertices[1:]:
            self.turtle.goto(vertex)
        self.turtle.goto(self.vertices[0])
        self.turtle.end_fill()

class Lawnmower:
    PATTERNS = [
        "horizontal",
        "vertical"
    ]

    def __init__(self, start_position, mower_width, pattern="horizontal"):
        if pattern not in Lawnmower.PATTERNS:
            raise ValueError(f"Invalid pattern: {pattern}. Available patterns: {Lawnmower.PATTERNS}")
            
        self.turtle = turtle.Turtle()
        self.turtle.pensize(mower_width)
        self.current_color = "light green"
        self.turtle.color(self.current_color)
        self.turtle.penup()
        self.turtle.goto(start_position)
        self.turtle.pendown()
        self.mower_width = mower_width
        self.turtle.shape("square")
        self.turtle.shapesize(0.75, 0.75)
        self.turtle.speed(10)
        self.pattern = pattern

    def toggle_color(self):
        self.current_color = "dark green" if self.current_color == "light green" else "light green"
        self.turtle.color(self.current_color)

    def mow(self, lawn_bounds):
        if self.pattern == "horizontal":
            self.mow_horizontal(lawn_bounds)
        elif self.pattern == "vertical":
            self.mow_vertical(lawn_bounds)

    def mow_horizontal(self, lawn_bounds):
        left_bound = min(point[0] for point in lawn_bounds)
        right_bound = max(point[0] for point in lawn_bounds)
        top_bound = max(point[1] for point in lawn_bounds)
        bottom_bound = min(point[1] for point in lawn_bounds)

        step_size = self.mower_width
        y = bottom_bound
        mowing_direction = 1  # 1 for right, -1 for left

        while y <= top_bound:
            x_segments = []
            x_start = None
            for x in range(left_bound, right_bound + 1):
                if point_in_polygon(x, y, lawn_bounds):
                    if x_start is None:
                        x_start = x
                else:
                    if x_start is not None:
                        x_segments.append((x_start, x - 1))
                        x_start = None
            if x_start is not None:
                x_segments.append((x_start, right_bound))

            # Mow each segment in alternating directions
            if mowing_direction == 1:
                for x_start, x_end in x_segments:
                    self.turtle.penup()
                    self.turtle.goto(x_start, y)
                    self.turtle.setheading(0)  # Facing right
                    self.turtle.pendown()
                    self.turtle.forward(x_end - x_start)
            else:
                for x_start, x_end in reversed(x_segments):
                    self.turtle.penup()
                    self.turtle.goto(x_end, y)
                    self.turtle.setheading(180)  # Facing left
                    self.turtle.pendown()
                    self.turtle.forward(x_end - x_start)

            self.toggle_color()

            y += step_size
            mowing_direction *= -1  # Reverse the direction for the next row



    def mow_vertical(self, lawn_bounds):
        left_bound = min(point[0] for point in lawn_bounds)
        right_bound = max(point[0] for point in lawn_bounds)
        top_bound = max(point[1] for point in lawn_bounds)
        bottom_bound = min(point[1] for point in lawn_bounds)

        step_size = self.mower_width
        x = left_bound
        mowing_direction = 1  # 1 for up, -1 for down

        while x <= right_bound:
            y_segments = []
            y_start = None
            for y in range(bottom_bound, top_bound + 1):
                if point_in_polygon(x, y, lawn_bounds):
                    if y_start is None:
                        y_start = y
                else:
                    if y_start is not None:
                        y_segments.append((y_start, y - 1))
                        y_start = None
            if y_start is not None:
                y_segments.append((y_start, top_bound))

            # Mow each segment in alternating directions
            if mowing_direction == 1:
                for y_start, y_end in y_segments:
                    self.turtle.penup()
                    self.turtle.goto(x, y_start)
                    self.turtle.setheading(90)  # Facing up
                    self.turtle.pendown()
                    self.turtle.forward(y_end - y_start)
            else:
                for y_start, y_end in reversed(y_segments):
                    self.turtle.penup()
                    self.turtle.goto(x, y_end)
                    self.turtle.setheading(270)  # Facing down
                    self.turtle.pendown()
                    self.turtle.forward(y_end - y_start)

            self.toggle_color()

            x += step_size
            mowing_direction *= -1  # Reverse the direction for the next column

