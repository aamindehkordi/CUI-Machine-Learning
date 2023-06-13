import math

class Point:

    def __init__(self, name, x, y):
        self.x = x
        self.y = y
        self.name = name

    def __str__(self):
        return "{} ({}, {})".format(self. name, self.x, self.y)

    def distance_to(self, point):
        x_dist = abs(self.x - point.x)
        y_dist = abs(self.y - point.y)
        return math.sqrt(x_dist ** 2 + y_dist ** 2)

    def bearing_to(self, point):
        x = abs(self.x - point.x)
        y = abs(self.y - point.y)
        angle = 360 * math.atan(y / x) / (2 * math.pi)
        return angle


if __name__ == "__main__":

    house = Point("House", -5, 12)
    treasure = Point("Treasure", 9, 3)

    print("Distance between {} and {} is {} units at {} degrees".format(
        house,
        treasure,
        house.distance_to(treasure),
        house.bearing_to(treasure)))
