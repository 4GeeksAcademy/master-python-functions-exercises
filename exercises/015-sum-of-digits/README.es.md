# `015` Suma de dígitos

## 📝 Instrucciones:

1. Completa la función `sum_of_digits(number)`. Recibe un entero de tres dígitos.

2. **Retorna** la suma de sus tres dígitos.

## 📎 Ejemplo:

```py
print(sum_of_digits(123))  # 6
print(sum_of_digits(905))  # 14
```

## 💡 Pista:

+ Combina lo que practicaste: las centenas son `number // 100`, las decenas `(number // 10) % 10` y las unidades `number % 10`.
