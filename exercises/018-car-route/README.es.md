# `018` Ruta en carro

Un carro puede recorrer `daily_distance` kilómetros por día. ¿Cuántos días necesita para completar una ruta de `route_length` kilómetros?

## 📝 Instrucciones:

1. Completa la función `car_route(daily_distance, route_length)`.

2. **Retorna** la cantidad de días necesarios. Si el último día no se completa, igual cuenta como un día entero.

## 📎 Ejemplo:

```py
print(car_route(20, 40))  # 2
print(car_route(20, 41))  # 3
```

## 💡 Pistas:

+ Si el viaje toma `2.05` días, la respuesta es `3`: necesitas redondear **hacia arriba**.

+ `math.ceil()` redondea hacia arriba. Recuerda escribir `import math` al inicio de tu archivo.
