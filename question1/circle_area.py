import math


def area(radius):
    if type(radius) in (int, float):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * radius ** 2

    if type(radius) is complex:
        raise TypeError("Complex numbers are not supported")

    raise TypeError("Radius must be a numeric value")


result = "{:.2f}".format(area(7))
print(result)
