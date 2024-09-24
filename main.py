import turtle
from util import Lawn, Lawnmower
import time

from math import cos, sin, pi, atan2
import random

def generate_random_polygon(shape="circle", x_range=(-20, 20), y_range=(-20, 20), variation=10):
    if shape == "circle":
        return generate_circle_variation(x_range, y_range, variation)
    elif shape == "square":
        return generate_square_variation(x_range, y_range, variation)
    elif shape == "rectangle":
        return generate_rectangle_variation(x_range, y_range, variation)
    elif shape == "L":
        return generate_l_shape_variation(x_range, y_range, variation)
    else:
        return generate_circle_variation(x_range, y_range, variation)

def generate_circle_variation(x_range, y_range, variation):
    center_x = random.randint(x_range[0], x_range[1])
    center_y = random.randint(y_range[0], y_range[1])
    radius = random.randint(150, 200)
    num_vertices = random.randint(12, 20)
    
    points = []
    for i in range(num_vertices):
        angle = 2 * pi * i / num_vertices
        random_radius = radius + random.randint(-variation, variation)
        x = int(center_x + random_radius * cos(angle))
        y = int(center_y + random_radius * sin(angle))
        points.append((x, y))
    
    return points

def generate_square_variation(x_range, y_range, variation):
    center_x = random.randint(x_range[0], x_range[1])
    center_y = random.randint(y_range[0], y_range[1])
    side_length = random.randint(250, 300)
    
    half_side = int (side_length / 2)
    points = [
        (center_x - half_side + random.randint(-variation, variation), center_y - half_side + random.randint(-variation, variation)),
        (center_x + half_side + random.randint(-variation, variation), center_y - half_side + random.randint(-variation, variation)),
        (center_x + half_side + random.randint(-variation, variation), center_y + half_side + random.randint(-variation, variation)),
        (center_x - half_side + random.randint(-variation, variation), center_y + half_side + random.randint(-variation, variation))
    ]
    
    return points

def generate_rectangle_variation(x_range, y_range, variation):
    center_x = random.randint(x_range[0], x_range[1])
    center_y = random.randint(y_range[0], y_range[1])
    width = random.randint(250, 300)
    height = random.randint(100, 200)
    
    half_width = int ( width / 2 )
    half_height = int( height / 2 )
    points = [
        (center_x - half_width + random.randint(-variation, variation), center_y - half_height + random.randint(-variation, variation)),
        (center_x + half_width + random.randint(-variation, variation), center_y - half_height + random.randint(-variation, variation)),
        (center_x + half_width + random.randint(-variation, variation), center_y + half_height + random.randint(-variation, variation)),
        (center_x - half_width + random.randint(-variation, variation), center_y + half_height + random.randint(-variation, variation))
    ]
    
    return points

def generate_l_shape_variation(x_range, y_range, variation):
    center_x = random.randint(x_range[0], x_range[1])
    center_y = random.randint(y_range[0], y_range[1])
    width = random.randint(250, 300)
    height = random.randint(250, 300)
    arm_length = random.randint(50, 100)
    
    points = [
        (center_x - int(width / 2) + random.randint(-variation, variation), center_y - int(height / 2) + random.randint(-variation, variation)),
        (center_x + int(width / 2) + random.randint(-variation, variation), center_y - int(height / 2) + random.randint(-variation, variation)),
        (center_x + int(width / 2) + random.randint(-variation, variation), center_y - int(arm_length / 2) + random.randint(-variation, variation)),
        (center_x + int(arm_length / 2) + random.randint(-variation, variation), center_y + int(height / 2) + random.randint(-variation, variation)),
        (center_x - int(width / 2) + random.randint(-variation, variation), center_y + int(height / 2) + random.randint(-variation, variation))
    ]
    
    return points


def main():
    # Number of polygons to generate and test
    num_polygons = 20
    shapes = ["circle", "square", "rectangle", "L"]

    for i in range(num_polygons):
        turtle.clearscreen()  # Clear the screen for the next polygon
        turtle.bgcolor("white")
        
        # Randomly pick a shape type
        shape = random.choice(shapes)
        print(f"Generating a {shape} lawn.")
        
        # Generate a random polygon based on the chosen shape
        vertices = generate_random_polygon(shape=shape)

        # Ensure the polygon has a minimum size for mowing
        if len(vertices) < 3:
            continue
        
        # Create a Lawn instance with the current polygon
        lawn = Lawn(vertices)
        
        # Find the leftmost point along the bottom edge of the polygon
        min_y = min(vertices, key=lambda v: v[1])[1]
        start_x = min([v[0] for v in vertices if v[1] == min_y])

        # Create a Lawnmower instance for the current polygon
        lawnmower = Lawnmower(start_position=(start_x, min_y), mower_width=20, pattern="horizontal")
        
        # Simulate mowing the lawn
        lawnmower.mow(vertices)
        
        time.sleep(1)  # Pause to observe the result before moving to the next polygon
    
    # Keep window open
    turtle.done()

if __name__ == "__main__":
    main()
