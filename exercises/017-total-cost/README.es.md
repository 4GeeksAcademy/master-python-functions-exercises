# `017` Costo total

Un cupcake cuesta `dollars` dólares y `cents` centavos. Alguien quiere comprar `quantity` cupcakes.

## 📝 Instrucciones:

1. Completa la función `total_cost(dollars, cents, quantity)`.

2. **Retorna** dos valores: el total de dólares y los centavos restantes a pagar. Los centavos siempre deben estar entre `0` y `99`.

## 📎 Ejemplo:

```py
print(total_cost(10, 15, 2))  # (20, 30)
print(total_cost(2, 50, 4))  # (10, 0)
```

## 💡 Pista:

+ Es más fácil trabajar solo en centavos: calcula el total en centavos y luego sepáralo en dólares (`// 100`) y centavos (`% 100`).
