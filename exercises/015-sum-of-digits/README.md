# `015` Sum of Digits

## 📝 Instructions:

1. Complete the function `sum_of_digits(number)`. It receives a three-digit integer.

2. **Return** the sum of its three digits.

## 📎 Example:

```py
print(sum_of_digits(123))  # 6
print(sum_of_digits(905))  # 14
```

## 💡 Hint:

+ Combine what you practiced: the hundreds are `number // 100`, the tens `(number // 10) % 10` and the units `number % 10`.
