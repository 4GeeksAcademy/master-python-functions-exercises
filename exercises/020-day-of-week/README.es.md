# `020` Día de la semana

Este año, el 1 de enero fue **jueves**. Los días de la semana se numeran así:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| - | - | - | - | - | - | - |
| Domingo | Lunes | Martes | Miércoles | Jueves | Viernes | Sábado |

## 📝 Instrucciones:

1. Completa la función `day_of_week(day_number)`. Recibe el número de un día del año, entre `1` y `365`.

2. **Retorna** el número del día de la semana correspondiente a ese día.

## 📎 Ejemplo:

```py
print(day_of_week(1))  # 4 (Thursday)
print(day_of_week(4))  # 0 (Sunday)
```

## 💡 Pista:

+ La semana se repite cada 7 días, así que `% 7` es tu aliado. El día `1` debe dar `4`: ¿qué necesitas sumar antes de aplicar `% 7`?
