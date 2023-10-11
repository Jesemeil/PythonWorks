def fibonacci_series(limit):
    fib_series = [0, 1]
    while True:
        next_fib = fib_series[-1] + fib_series[-2]
        if next_fib <= limit:
            fib_series.append(next_fib)
        else:
            break
    return fib_series


fibonacci_series_50 = fibonacci_series(60)
print(fibonacci_series_50)
