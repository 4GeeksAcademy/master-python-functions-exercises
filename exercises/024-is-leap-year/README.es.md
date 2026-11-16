# `024` ¿Es año bisiesto?

Un año bisiesto tiene 366 días. Un año es bisiesto cuando:

+ Es divisible entre `4`, **y**
+ **no** es divisible entre `100`, **salvo** que también sea divisible entre `400`.

Así, 2024 y 2000 son bisiestos, pero 1900 y 2023 no lo son.

## 📝 Instrucciones:

1. Completa la función `is_leap_year(year)`.

2. **Retorna** `True` si el año es bisiesto y `False` si no lo es.

## 📎 Ejemplo:

```py
print(is_leap_year(2024))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2000))  # True
```

## 💡 Pistas:

+ Un número es divisible entre otro cuando el resto es cero: `year % 4 == 0`.

+ Puedes combinar condiciones con `and`, `or` y `not`, o usar `if` / `elif` / `else`.
