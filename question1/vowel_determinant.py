def is_vowel(letter):
    vowels = "aeiouAEIOU"
    return letter in vowels


def main():
    letter_to_check = input("Enter a letter: ")

    if len(letter_to_check) == 1 and letter_to_check.isalpha():
        if is_vowel(letter_to_check):
            print(f"{letter_to_check} is a vowel.")
        else:
            print(f"{letter_to_check} is not a vowel.")
    else:
        print("Please enter a single letter.")


if __name__ == "__main__":
    main()
