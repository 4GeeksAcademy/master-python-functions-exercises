# `010` Reloj digital

Un reloj digital muestra la hora en formato de 24 horas: horas de `0` a `23` y minutos de `0` a `59`.

## 📝 Instrucciones:

1. Completa la función `digital_clock(minutes)`. Recibe la cantidad de minutos que han pasado desde la medianoche.

2. **Retorna** dos valores: la hora y los minutos que muestra el reloj.

## 📎 Ejemplo:

```py
print(digital_clock(150))  # (2, 30)
print(digital_clock(1441))  # (0, 1)
```

150 minutos después de la medianoche son las 2:30. Y 1441 minutos es un día completo más un minuto, así que el reloj muestra 0:01.

## 💡 Pista:

+ Después de calcular las horas, usa `% 24` para que el reloj vuelva a `0` cada día.
