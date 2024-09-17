
import turtle
import math

# Helper function to check if a point is inside the polygon
def point_in_polygon(x, y, polygon):
    # Ray-casting algorithm to test if a point is in a polygon
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

# Define the lawn (polygon) and the lawnmower (turtle)
class Lawn:
    def __init__(self, vertices):
        self.vertices = vertices
        self.turtle = turtle.Turtle()
        self.turtle.color("green")
        self.turtle.speed(0)  # Fast drawing for the polygon creation
        self.turtle.ht()
        self.create_polygon()

    def create_polygon(self):
        self.turtle.penup()
        self.turtle.goto(self.vertices[0])
        self.turtle.pendown()
        self.turtle.begin_fill()
        for vertex in self.vertices[1:]:
            self.turtle.goto(vertex)
        self.turtle.goto(self.vertices[0])  # Close the polygon
        self.turtle.end_fill()

class Lawnmower:
    def __init__(self, start_position, mower_width):
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
        self.turtle.speed(100)
    
    def toggle_color(self):
        if self.current_color == "light green":
            self.current_color = "dark green"
        else:
            self.current_color = "light green"
        self.turtle.color(self.current_color)

    def mow(self, lawn_bounds):
        left_bound = min([point[0] for point in lawn_bounds])
        right_bound = max([point[0] for point in lawn_bounds])
        top_bound = max([point[1] for point in lawn_bounds])
        bottom_bound = min([point[1] for point in lawn_bounds])
        
        step_size = self.mower_width  # Mowing step (distance between rows)
        y = bottom_bound
        mowing_direction = 1  # 1 for right, -1 for left

        while y <= top_bound:
            # Find the valid x-range for the current y
            x_start, x_end = None, None
            x = left_bound
            while x <= right_bound:
                if point_in_polygon(x, y, lawn_bounds):
                    if x_start is None:
                        x_start = x
                    x_end = x
                x += 1
            
            if x_start is not None and x_end is not None:
                self.turtle.penup()
                if mowing_direction == 1:
                    self.turtle.goto(x_start, y)
                    self.turtle.rt(180)  # Point right
                else:
                    self.turtle.goto(x_end, y)
                    self.turtle.lt(180)  # Point left
                self.turtle.pendown()
                
                # Calculate distance to mow
                distance_to_mow = abs(x_end - x_start)
                self.turtle.forward(distance_to_mow)
                
                self.toggle_color()  # Change color for the next row

            # Move to the next row
            y += step_size
            if y <= top_bound:
                # Determine the starting position for the next row based on direction
                if mowing_direction == 1:
                    # Move to the rightmost valid x for the next row
                    x = right_bound
                    while x >= left_bound:
                        if point_in_polygon(x, y, lawn_bounds):
                            self.turtle.penup()
                            self.turtle.goto(x, y)
                            self.turtle.pendown()
                            break
                        x -= 1
                else:
                    # Move to the leftmost valid x for the next row
                    x = left_bound
                    while x <= right_bound:
                        if point_in_polygon(x, y, lawn_bounds):
                            self.turtle.penup()
                            self.turtle.goto(x, y)
                            self.turtle.pendown()
                            break
                        x += 1

                # Flip the mowing direction for the next row
                mowing_direction *= -1