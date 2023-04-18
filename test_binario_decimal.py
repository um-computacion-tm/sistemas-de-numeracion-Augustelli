
def b2d(binario: str) -> int:

    decimal = 0
    longitud = len(binario)
    binario_reordenado = binario[::-1]
    binario_lista = list()

    for x in binario_reordenado:
        binario_lista.append(x)

    for i in range(longitud):
        for j in binario_lista:
            decimal += int(j)*(2**i)
            binario_lista.remove(j)
            break
    return decimal


print(b2d('1101'))


def d2b(decimal):
    sigue = True
    if decimal == 1:
        return 1
    elif decimal == 2:
        return 10
    dividendo = decimal
    listado = list()
    while sigue:
        if dividendo == 2:
            listado.append(1)
            sigue = False
        elif dividendo == 1:
            listado.append(0)
            sigue = False

        resto = dividendo % 2
        dividendo = int(dividendo/2)
        listado.append(resto)
    return listado


print(d2b(10))

