# `012` Intercambiar dígitos

## 📝 Instrucciones:

1. Completa la función `swap_digits(number)`. Recibe un entero de dos dígitos.

2. **Retorna** un nuevo entero con los dos dígitos intercambiados.

## 📎 Ejemplo:

```py
print(swap_digits(79))  # 97
print(swap_digits(30))  # 3
```

Fíjate que `30` se convierte en `03`, que como entero es `3`. El resultado debe ser un `int`, no un string.

## 💡 Pista:

+ Reutiliza la idea del ejercicio anterior: obtén ambos dígitos y construye el nuevo número como `units * 10 + tens`.
