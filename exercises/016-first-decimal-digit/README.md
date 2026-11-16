# `016` First Decimal Digit

## 📝 Instructions:

1. Complete the function `first_decimal_digit(number)`. It receives a positive decimal number (a `float`).

2. **Return** the first digit after the decimal point, as an integer.

## 📎 Example:

```py
print(first_decimal_digit(1.79))  # 7
print(first_decimal_digit(10.2))  # 2
```

## 💡 Hints:

+ Multiply by `10` to move the first decimal to the left of the point: `1.79 * 10` is `17.9`.

+ `int()` removes the decimals and `% 10` keeps the last digit.
