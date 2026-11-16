# `020` Day of the Week

This year, January 1st was a **Thursday**. Days of the week are numbered like this:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| - | - | - | - | - | - | - |
| Sunday | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday |

## 📝 Instructions:

1. Complete the function `day_of_week(day_number)`. It receives the number of a day of the year, between `1` and `365`.

2. **Return** the number of the day of the week for that day.

## 📎 Example:

```py
print(day_of_week(1))  # 4 (Thursday)
print(day_of_week(4))  # 0 (Sunday)
```

## 💡 Hint:

+ The week repeats every 7 days, so `% 7` is your friend. Day `1` must give `4`: what do you need to add before applying `% 7`?
