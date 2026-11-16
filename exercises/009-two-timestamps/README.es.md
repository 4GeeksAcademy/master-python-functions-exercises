# `009` Dos marcas de tiempo

Tienes dos momentos del mismo día, cada uno expresado en horas, minutos y segundos. El primer momento ocurre antes que el segundo.

## 📝 Instrucciones:

1. Completa la función `two_timestamps(hour1, min1, sec1, hour2, min2, sec2)`.

2. **Retorna** cuántos segundos pasaron entre los dos momentos.

## 📎 Ejemplo:

```py
print(two_timestamps(1, 1, 1, 2, 2, 2))  # 3661
print(two_timestamps(1, 2, 30, 1, 3, 20))  # 50
```

## 💡 Pista:

+ Convierte cada momento a segundos desde la medianoche y réstalos.
