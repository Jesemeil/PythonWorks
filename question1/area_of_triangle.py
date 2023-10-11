def triangle_area(base, height):
    return 0.5 * base * height


def main():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))

    area = triangle_area(base, height)
    print("The area of the triangle is:", area)


if __name__ == "__main__":
    main()
