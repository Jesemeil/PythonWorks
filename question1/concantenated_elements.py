def concatenate_elements(input_list):
    concatenated_string = ''.join(input_list)
    return concatenated_string


def main():
    input_list = input("Enter elements separated by spaces: ").split()
    result = concatenate_elements(input_list)
    print("Concatenated string:", result)


if __name__ == "__main__":
    main()
