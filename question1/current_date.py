import datetime


def main():
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d   %H:%M:%S")
    print("Current date and time:")
    print(formatted_datetime)


if __name__ == "__main__":
    main()
