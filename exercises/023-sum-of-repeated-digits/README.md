# `023` Sum of Repeated Digits

Given a digit `a`, we can build the numbers `a`, `aa`, `aaa` and `aaaa`. For example, with `a = 9` we get `9`, `99`, `999` and `9999`.

## 📝 Instructions:

1. Complete the function `sum_of_repeated_digits(digit)`. It receives an integer between `1` and `9`.

2. **Return** the result of `a + aa + aaa + aaaa`.

## 📎 Example:

```py
print(sum_of_repeated_digits(9))  # 11106
print(sum_of_repeated_digits(1))  # 1234
```

## 💡 Hints:

+ Option 1 (strings): `str(9) * 3` is `"999"` and `int("999")` is `999`.

+ Option 2 (math): `aa` is `a * 11`, `aaa` is `a * 111`...
