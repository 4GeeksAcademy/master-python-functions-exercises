def count_digits(number):
    digits = 1
    while number >= 10:
        number = number // 10
        digits += 1
    return digits


# Try your function with different values
print(count_digits(2026))
