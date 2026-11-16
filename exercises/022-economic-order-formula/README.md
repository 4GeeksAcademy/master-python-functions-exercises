# `022` Economic Order Formula

A store uses this formula to decide how many units to order:

```text
Q = square root of ((2 * C * D) / H)
```

Where `C = 50` and `H = 30` are fixed values and `D` changes every time.

## 📝 Instructions:

1. Complete the function `order_quantity(demand)`, where `demand` is the value of `D`.

2. **Return** `Q` rounded to the nearest integer.

## 📎 Example:

```py
print(order_quantity(150))  # 22
print(order_quantity(100))  # 18
```

## 💡 Hints:

+ Define the fixed values as variables inside the function: `C = 50` and `H = 30`.

+ `round(value)` without a second argument returns the nearest `int`.
