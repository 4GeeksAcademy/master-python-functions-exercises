# `016` Primer decimal

## 📝 Instrucciones:

1. Completa la función `first_decimal_digit(number)`. Recibe un número decimal positivo (un `float`).

2. **Retorna** el primer dígito después del punto decimal, como entero.

## 📎 Ejemplo:

```py
print(first_decimal_digit(1.79))  # 7
print(first_decimal_digit(10.2))  # 2
```

## 💡 Pistas:

+ Multiplica por `10` para mover el primer decimal a la izquierda del punto: `1.79 * 10` es `17.9`.

+ `int()` elimina los decimales y `% 10` se queda con el último dígito.
