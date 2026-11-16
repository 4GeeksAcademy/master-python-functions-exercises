# `008` Horas y minutos

## 📝 Instrucciones:

1. Completa la función `hours_minutes(seconds)`. Recibe la cantidad de segundos que han pasado.

2. **Retorna** dos valores: el número de horas completas y el número de minutos completos que quedan después de esas horas.

## 📎 Ejemplo:

```py
print(hours_minutes(3900))  # (1, 5)
print(hours_minutes(60))  # (0, 1)
```

## 💡 Pistas:

+ Una hora tiene `3600` segundos y un minuto tiene `60` segundos.

+ Primero calcula las horas completas con `//` y luego usa `%` para obtener los segundos que sobran.
