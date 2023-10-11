def main():
    filename = input("Enter a filename: ")
    file_extension = filename.split('.')[-1]
    print("File extension:", file_extension)


if __name__ == "__main__":
    main()
