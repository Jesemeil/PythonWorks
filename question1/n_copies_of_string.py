def copy_string(input_string, n):
    if n < 0:
        return "Number of copies should be non-negative."

    if len(input_string) < 2:
        copied_string = input_string * n
    else:
        copied_string = input_string[:2] * n

    return copied_string


def main():
    input_string = input("Enter a string: ")
    n = int(input("Enter the number of copies: "))

    result = copy_string(input_string, n)
    print("Result:", result)


if __name__ == "__main__":
    main()
