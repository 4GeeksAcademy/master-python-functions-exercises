# `019` Siglo

Los siglos empiezan en el año que termina en `01`: el siglo XX va de 1901 a 2000 y el siglo XXI empieza en 2001.

## 📝 Instrucciones:

1. Completa la función `century(year)`. Recibe un entero positivo.

2. **Retorna** el número del siglo al que pertenece ese año.

## 📎 Ejemplo:

```py
print(century(2001))  # 21
print(century(2000))  # 20
print(century(1))  # 1
```

## 💡 Pista:

+ Prueba a dividir entre `100` y redondear hacia arriba con `math.ceil()`. Comprueba que `2000` y `2001` den siglos distintos.
