def mayor_estricto1(a, b, c):
    datos = (a, b, c)
    maximo = max(datos)
    ocurrencia = datos.count(maximo)
    if ocurrencia == 1:
        return maximo
    else:
        return -1

assert (-1 == mayor_estricto1(3, 5, 5))
assert (7 == mayor_estricto1(3, 5, 7))
assert (5 == mayor_estricto1(3, 3, 5))

def mayor_estricto2(a, b, c):
    salida = (
        a * int(a > b) * int(a > c)
        + b * int(b > a) * int(b > c)
        + c * int(c > a) * int(c > b)
    )
    return salida * int(salida != 0) + -1 * int(salida == 0)


assert (-1 == mayor_estricto2(3, 5, 5))
assert (7 == mayor_estricto2(3, 5, 7))
assert (5 == mayor_estricto2(3, 3, 5))