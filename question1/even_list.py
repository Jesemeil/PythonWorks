def print_even_numbers(numbers):
    for num in numbers:
        if num == 237:
            break
        if num % 2 == 0:
            print(num, end=" ")


def main():
    numbers = [
        386, 462, 47, 418, 907, 304, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
        399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
        815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
        958, 743, 527
    ]

    print("Even numbers:")
    print_even_numbers(numbers)


if __name__ == "__main__":
    main()
