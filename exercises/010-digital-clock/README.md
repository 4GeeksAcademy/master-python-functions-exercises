# `010` Digital Clock

A digital clock shows the time in 24-hour format: hours from `0` to `23` and minutes from `0` to `59`.

## 📝 Instructions:

1. Complete the function `digital_clock(minutes)`. It receives the number of minutes that have passed since midnight.

2. **Return** two values: the hour and the minutes that the clock shows.

## 📎 Example:

```py
print(digital_clock(150))  # (2, 30)
print(digital_clock(1441))  # (0, 1)
```

150 minutes after midnight it's 2:30. And 1441 minutes is one full day plus one minute, so the clock shows 0:01.

## 💡 Hint:

+ After calculating the hours, use `% 24` so the clock starts again at `0` every day.
