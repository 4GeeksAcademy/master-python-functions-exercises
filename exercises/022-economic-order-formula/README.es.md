# `022` Fórmula de pedido económico

Una tienda usa esta fórmula para decidir cuántas unidades pedir:

```text
Q = raíz cuadrada de ((2 * C * D) / H)
```

Donde `C = 50` y `H = 30` son valores fijos y `D` cambia cada vez.

## 📝 Instrucciones:

1. Completa la función `order_quantity(demand)`, donde `demand` es el valor de `D`.

2. **Retorna** `Q` redondeado al entero más cercano.

## 📎 Ejemplo:

```py
print(order_quantity(150))  # 22
print(order_quantity(100))  # 18
```

## 💡 Pistas:

+ Define los valores fijos como variables dentro de la función: `C = 50` y `H = 30`.

+ `round(value)` sin segundo argumento retorna el `int` más cercano.
