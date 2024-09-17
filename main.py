import turtle
from util import Lawn, Lawnmower
import time
import random
from math import atan2

def generate_random_polygon(min_vertices=3, max_vertices=50, x_range=(-200, 200), y_range=(-200, 200)):
    num_vertices = random.randint(min_vertices, max_vertices)
    points = [(random.randint(x_range[0], x_range[1]), random.randint(y_range[0], y_range[1])) for _ in range(num_vertices)]

    # Sort points by angle around the centroid to form a valid simple polygon
    centroid_x = sum(p[0] for p in points) / len(points)
    centroid_y = sum(p[1] for p in points) / len(points)

    def angle_from_centroid(point):
        return atan2(point[1] - centroid_y, point[0] - centroid_x)

    sorted_points = sorted(points, key=angle_from_centroid)

    return sorted_points

def main():
    # Number of polygons to generate and test
    num_polygons = 5
    
    for i in range(num_polygons):
        turtle.clearscreen()  # Clear the screen for the next polygon
        turtle.bgcolor("white")
        
        # Generate a random polygon
        vertices = generate_random_polygon()
        
        # Ensure the polygon has a minimum size for mowing
        if len(vertices) < 3:
            continue
        
        # Create a Lawn instance with the current polygon
        lawn = Lawn(vertices)
        
        # Find the leftmost point along the bottom edge of the polygon
        min_y = min(vertices, key=lambda v: v[1])[1]
        start_x = min([v[0] for v in vertices if v[1] == min_y])

        # Create a Lawnmower instance for the current polygon
        lawnmower = Lawnmower(start_position=(start_x, min_y), mower_width=20)
        
        # Simulate mowing the lawn
        lawnmower.mow(vertices)
        
        time.sleep(1)  # Pause to observe the result before moving to the next polygon
    
    # Keep window open
    turtle.done()

if __name__ == "__main__":
    main()
