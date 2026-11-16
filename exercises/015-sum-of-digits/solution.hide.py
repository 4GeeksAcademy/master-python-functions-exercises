def sum_of_digits(number):
    return number // 100 + (number // 10) % 10 + number % 10


# Try your function with different values
print(sum_of_digits(123))
