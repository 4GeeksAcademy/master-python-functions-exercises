# `012` Swap Digits

## 📝 Instructions:

1. Complete the function `swap_digits(number)`. It receives a two-digit integer.

2. **Return** a new integer with the two digits swapped.

## 📎 Example:

```py
print(swap_digits(79))  # 97
print(swap_digits(30))  # 3
```

Note that `30` becomes `03`, which as an integer is `3`. The result must be an `int`, not a string.

## 💡 Hint:

+ Reuse the idea of the previous exercise: get both digits and build the new number as `units * 10 + tens`.
