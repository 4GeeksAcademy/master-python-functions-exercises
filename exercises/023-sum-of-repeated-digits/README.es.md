# `023` Suma de dígitos repetidos

Dado un dígito `a`, podemos construir los números `a`, `aa`, `aaa` y `aaaa`. Por ejemplo, con `a = 9` obtenemos `9`, `99`, `999` y `9999`.

## 📝 Instrucciones:

1. Completa la función `sum_of_repeated_digits(digit)`. Recibe un entero entre `1` y `9`.

2. **Retorna** el resultado de `a + aa + aaa + aaaa`.

## 📎 Ejemplo:

```py
print(sum_of_repeated_digits(9))  # 11106
print(sum_of_repeated_digits(1))  # 1234
```

## 💡 Pistas:

+ Opción 1 (strings): `str(9) * 3` es `"999"` e `int("999")` es `999`.

+ Opción 2 (matemática): `aa` es `a * 11`, `aaa` es `a * 111`...
