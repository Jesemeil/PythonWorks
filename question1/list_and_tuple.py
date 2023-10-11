def main():
    input_str = input("Enter comma-separated numbers: ")
    numbers = input_str.split(', ')

    numbers_list = list(numbers)
    numbers_tuple = tuple(numbers)

    print("List:", numbers_list)
    print("Tuple:", numbers_tuple)


if __name__ == "__main__":
    main()
