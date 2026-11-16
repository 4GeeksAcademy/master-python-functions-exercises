# `025` Factorial

The factorial of a number `n` (written `n!`) is the product of all the integers from `1` to `n`:

```text
5! = 1 * 2 * 3 * 4 * 5 = 120
```

By definition, `0!` is `1`.

## 📝 Instructions:

1. Complete the function `factorial(number)`. It receives an integer greater than or equal to `0`.

2. **Return** its factorial. Solve it with a loop, without using `math.factorial()`.

## 📎 Example:

```py
print(factorial(5))  # 120
print(factorial(8))  # 40320
print(factorial(0))  # 1
```

## 💡 Hints:

+ Start with a variable `result = 1` and multiply it by each number of the range.

+ `range(1, number + 1)` generates the numbers from `1` to `number`, both included.
