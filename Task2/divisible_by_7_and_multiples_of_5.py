def divisible_by_7_and_5():
    divisible_numbers = []
    for number in range(1500, 2701):
        if number % 7 == 0 and number % 5 == 0:
            divisible_numbers.append(number)
    return divisible_numbers


result = divisible_by_7_and_5()

print("Numbers divisible by 7 and multiples of 5 between 1500 and 2700:", result)
