import math


def area_of_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    formatted_area = "{:.2f}".format(area)
    return formatted_area


result = (area_of_circle())
print("The area of the circle is:", result)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


def main():
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)
    area = circle.calculate_area()
    formatted_area = "{:.2f}".format(area)
    print("The area of the circle with radius", radius, "is:", formatted_area)


if __name__ == "__main__":
    main()
