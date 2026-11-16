# `018` Car Route

A car can drive `daily_distance` kilometers per day. How many days does it need to complete a route of `route_length` kilometers?

## 📝 Instructions:

1. Complete the function `car_route(daily_distance, route_length)`.

2. **Return** the number of days needed. If the last day is not complete, it still counts as a full day.

## 📎 Example:

```py
print(car_route(20, 40))  # 2
print(car_route(20, 41))  # 3
```

## 💡 Hints:

+ If the trip takes `2.05` days, the answer is `3`: you need to round **up**.

+ `math.ceil()` rounds up. Remember to write `import math` at the top of your file.
