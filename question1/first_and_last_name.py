def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    reversed_first_name = first_name[::-1]
    reversed_last_name = last_name[::-1]
    full_name_reversed = reversed_first_name + " " + reversed_last_name
    print("Reversed name:", full_name_reversed)


if __name__ == "__main__":
    main()
