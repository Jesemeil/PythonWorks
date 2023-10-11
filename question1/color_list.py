def main():
    color_list = ["Red", "Green", "White", "Black", "Blue"]

    if len(color_list) >= 2:
        first_color = color_list[0]
        last_color = color_list[-1]
        print("First color:", first_color)
        print("Last color:", last_color)
    else:
        print("The list must contain at least two colors.")


if __name__ == "__main__":
    main()
