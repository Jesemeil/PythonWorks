def is_value_contained(value, value_list):
    return value in value_list


def main():
    test_data = [1, 5, 8, 3]
    value_to_check = int(input("Enter the value to check: "))

    if is_value_contained(value_to_check, test_data):
        print(f"{value_to_check} - {test_data}: True")
    else:
        print(f"{value_to_check} - {test_data}: False")


if __name__ == "__main__":
    main()
