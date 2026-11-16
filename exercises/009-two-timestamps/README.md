# `009` Two Timestamps

You have two moments of the same day, each one given as hours, minutes and seconds. The first moment happens before the second.

## 📝 Instructions:

1. Complete the function `two_timestamps(hour1, min1, sec1, hour2, min2, sec2)`.

2. **Return** how many seconds passed between the two moments.

## 📎 Example:

```py
print(two_timestamps(1, 1, 1, 2, 2, 2))  # 3661
print(two_timestamps(1, 2, 30, 1, 3, 20))  # 50
```

## 💡 Hint:

+ Convert each moment to seconds since midnight and subtract them.
