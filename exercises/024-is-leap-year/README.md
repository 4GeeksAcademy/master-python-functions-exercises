# `024` Is It a Leap Year?

A leap year has 366 days. A year is a leap year when:

+ It is divisible by `4`, **and**
+ it is **not** divisible by `100`, **unless** it is also divisible by `400`.

So 2024 and 2000 are leap years, but 1900 and 2023 are not.

## 📝 Instructions:

1. Complete the function `is_leap_year(year)`.

2. **Return** `True` if the year is a leap year and `False` if it isn't.

## 📎 Example:

```py
print(is_leap_year(2024))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2000))  # True
```

## 💡 Hints:

+ A number is divisible by another when the remainder is zero: `year % 4 == 0`.

+ You can combine conditions with `and`, `or` and `not`, or use `if` / `elif` / `else`.
