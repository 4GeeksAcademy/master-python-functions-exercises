# `014` Dígito de las decenas

## 📝 Instrucciones:

1. Completa la función `tens_digit(number)`. Recibe un entero positivo.

2. **Retorna** su dígito de las decenas (el segundo dígito empezando por la derecha).

## 📎 Ejemplo:

```py
print(tens_digit(1234))  # 3
print(tens_digit(179))  # 7
print(tens_digit(5))  # 0
```

## 💡 Pista:

+ Primero elimina el dígito de las unidades con `// 10` y luego toma el último dígito de lo que queda con `% 10`.
