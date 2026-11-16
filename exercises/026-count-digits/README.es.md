# `026` Contar dígitos

Un bucle `while` repite un bloque de código **mientras** una condición sea verdadera. Es útil cuando no sabes de antemano cuántas repeticiones necesitas.

## 📝 Instrucciones:

1. Completa la función `count_digits(number)`. Recibe un entero mayor o igual que `0`.

2. **Retorna** cuántos dígitos tiene el número. Resuélvelo con números (`//`) y un bucle `while`, sin convertirlo a string.

## 📎 Ejemplo:

```py
print(count_digits(2026))  # 4
print(count_digits(7))  # 1
print(count_digits(0))  # 1
```

## 💡 Pistas:

+ Cada vez que haces `number = number // 10`, el número pierde un dígito.

+ Cuidado con el `0`: tiene un dígito.
