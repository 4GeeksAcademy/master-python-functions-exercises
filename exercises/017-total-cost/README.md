# `017` Total Cost

A cupcake costs `dollars` dollars and `cents` cents. Someone wants to buy `quantity` cupcakes.

## 📝 Instructions:

1. Complete the function `total_cost(dollars, cents, quantity)`.

2. **Return** two values: the total dollars and the remaining cents to pay. The cents must always be between `0` and `99`.

## 📎 Example:

```py
print(total_cost(10, 15, 2))  # (20, 30)
print(total_cost(2, 50, 4))  # (10, 0)
```

## 💡 Hint:

+ It's easier to work only in cents: calculate the total in cents and then split it into dollars (`// 100`) and cents (`% 100`).
