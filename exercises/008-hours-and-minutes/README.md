# `008` Hours and Minutes

## 📝 Instructions:

1. Complete the function `hours_minutes(seconds)`. It receives the number of seconds that have passed.

2. **Return** two values: the number of full hours and the number of full minutes left after those hours.

## 📎 Example:

```py
print(hours_minutes(3900))  # (1, 5)
print(hours_minutes(60))  # (0, 1)
```

## 💡 Hints:

+ One hour has `3600` seconds and one minute has `60` seconds.

+ First calculate the full hours with `//`, then use `%` to get the seconds that are left.
