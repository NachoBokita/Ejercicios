"""Ejercicio 1
Genenerar su propia funcion map, que tome como parametro 
una funcion y una coleccion, aplicando dicha fn recibida como
param y se la aplique a cada elemento de la coleccion, retornando 
un objeto generador.
Luego pasar el objeto resultante por una fn list() e imprimirlo.

  Ej: 
    objeto_resultante = myMap(lambda x: x + 3, range(10))

    print(list(objeto_resultante))
    
    >>> [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
"""

from operator import itemgetter
from functools import reduce

def myMap(funcion, coleccion):
    for i in coleccion:
        yield funcion(i)

objeto_resultante = myMap(lambda x: x + 3, range(10))

print(list(objeto_resultante)) 