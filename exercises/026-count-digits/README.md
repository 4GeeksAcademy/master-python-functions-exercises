# `026` Count Digits

A `while` loop repeats a block of code **while** a condition is true. It's useful when you don't know in advance how many repetitions you need.

## 📝 Instructions:

1. Complete the function `count_digits(number)`. It receives an integer greater than or equal to `0`.

2. **Return** how many digits the number has. Solve it with numbers (`//`) and a `while` loop, without converting it to a string.

## 📎 Example:

```py
print(count_digits(2026))  # 4
print(count_digits(7))  # 1
print(count_digits(0))  # 1
```

## 💡 Hints:

+ Each time you do `number = number // 10`, the number loses one digit.

+ Be careful with `0`: it has one digit.
