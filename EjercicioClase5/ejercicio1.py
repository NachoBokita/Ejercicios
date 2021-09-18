"""
Ejercicio 1:
    Realiza una función separar(lista) que tome una lista de números enteros
    y devuelva dos listas la primera con los números pares
    y la segunda con los números impares.

    Ej:
        pares, impares = separar([6,5,2,1,7])
        print(pares)
        print(impares)

        >>> [2, 6]
        >>> [1, 5, 7]
"""


valores = [1, 2, 412, 543, 634, 1234, 62, 6474, 5, 2, 0]  

def separar(una_lista):
    
    pares = list(filter(lambda x: x % 2 == 0 and x != 0, una_lista))
    impares = list(filter(lambda x: x % 2 != 0 or x == 0, una_lista))
    
    return pares, impares

pares, impares = separar(valores)

print(pares)
print(impares)