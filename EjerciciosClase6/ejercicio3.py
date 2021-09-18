
"""Ejercicio 3
Genenerar su propia funcion reduce, que tome como parametro 
una funcion y una coleccion, devolviendo el acumulador resultante.
Luego imprimirlo.

  Ej: 
    acumulador = myReduce(lambda x, b: x + b, [3, 1, 10, 8, 6, 2])

    print(acumulador)
    
    >>> 30
"""

def myReduce(funcion, coleccion):
    var = 0
    for i in coleccion: 
        var = funcion(i, var) 
    return var
        

acumulador = myReduce(lambda x, b: x + b, [3, 1, 10, 8, 6, 2])

print(acumulador) 