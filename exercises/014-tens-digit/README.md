# `014` Tens Digit

## 📝 Instructions:

1. Complete the function `tens_digit(number)`. It receives a positive integer.

2. **Return** its tens digit (the second digit from the right).

## 📎 Example:

```py
print(tens_digit(1234))  # 3
print(tens_digit(179))  # 7
print(tens_digit(5))  # 0
```

## 💡 Hint:

+ First remove the units digit with `// 10`, then take the last digit of what's left with `% 10`.
