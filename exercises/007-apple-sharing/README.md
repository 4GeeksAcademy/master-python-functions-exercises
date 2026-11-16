# `007` Apple Sharing

`n` students share `k` apples as evenly as possible. Each student gets the same amount and the apples that can't be split stay in the basket.

## 📝 Instructions:

1. Complete the function `apple_sharing(n, k)`, where `n` is the number of students and `k` the number of apples.

2. **Return** two values: how many apples each student gets and how many stay in the basket.

## 📎 Example:

```py
print(apple_sharing(6, 50))  # (8, 2)
print(apple_sharing(5, 10))  # (2, 0)
```

## 💡 Hints:

+ Integer division `//` drops the decimals: `50 // 6` is `8`.

+ The modulo operator `%` gives the remainder of a division: `50 % 6` is `2`.
