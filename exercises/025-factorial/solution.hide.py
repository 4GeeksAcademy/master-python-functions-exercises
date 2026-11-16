def factorial(number):
    result = 1
    for value in range(1, number + 1):
        result *= value
    return result


# Try your function with different values
print(factorial(5))
