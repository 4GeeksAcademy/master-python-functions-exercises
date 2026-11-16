# `007` Repartir manzanas

`n` estudiantes se reparten `k` manzanas de la forma más equitativa posible. Cada estudiante recibe la misma cantidad y las manzanas que no se pueden repartir se quedan en la cesta.

## 📝 Instrucciones:

1. Completa la función `apple_sharing(n, k)`, donde `n` es el número de estudiantes y `k` el número de manzanas.

2. **Retorna** dos valores: cuántas manzanas recibe cada estudiante y cuántas quedan en la cesta.

## 📎 Ejemplo:

```py
print(apple_sharing(6, 50))  # (8, 2)
print(apple_sharing(5, 10))  # (2, 0)
```

## 💡 Pistas:

+ La división entera `//` descarta los decimales: `50 // 6` es `8`.

+ El operador módulo `%` da el resto de una división: `50 % 6` es `2`.
