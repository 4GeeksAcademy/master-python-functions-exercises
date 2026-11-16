# `025` Factorial

El factorial de un número `n` (se escribe `n!`) es el producto de todos los enteros desde `1` hasta `n`:

```text
5! = 1 * 2 * 3 * 4 * 5 = 120
```

Por definición, `0!` es `1`.

## 📝 Instrucciones:

1. Completa la función `factorial(number)`. Recibe un entero mayor o igual que `0`.

2. **Retorna** su factorial. Resuélvelo con un bucle, sin usar `math.factorial()`.

## 📎 Ejemplo:

```py
print(factorial(5))  # 120
print(factorial(8))  # 40320
print(factorial(0))  # 1
```

## 💡 Pistas:

+ Empieza con una variable `result = 1` y multiplícala por cada número del rango.

+ `range(1, number + 1)` genera los números desde `1` hasta `number`, ambos incluidos.
