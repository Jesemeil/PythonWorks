def fizz_buzz():
    for num in range(1, 50):
        if num % 3 == 0 and num % 5 == 0:
            print("Fizz Buzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


fizz_buzz()
