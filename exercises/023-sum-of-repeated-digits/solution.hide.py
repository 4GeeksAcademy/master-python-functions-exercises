def sum_of_repeated_digits(digit):
    text = str(digit)
    return int(text) + int(text * 2) + int(text * 3) + int(text * 4)


# Try your function with different values
print(sum_of_repeated_digits(9))
