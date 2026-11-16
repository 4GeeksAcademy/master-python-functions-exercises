# `019` Century

Centuries start in the year ending in `01`: the 20th century goes from 1901 to 2000 and the 21st century starts in 2001.

## 📝 Instructions:

1. Complete the function `century(year)`. It receives a positive integer.

2. **Return** the number of the century that year belongs to.

## 📎 Example:

```py
print(century(2001))  # 21
print(century(2000))  # 20
print(century(1))  # 1
```

## 💡 Hint:

+ Try dividing by `100` and rounding up with `math.ceil()`. Check that `2000` and `2001` give different centuries.
