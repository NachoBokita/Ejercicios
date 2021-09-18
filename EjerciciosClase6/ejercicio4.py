"""Ejercicio 4
Genenerar su propia funcion enumerate que agrega un contador a un 
iterable y lo devuelva en forma de objeto enumerador. 
Por ultimo convertirlo en un diccionario e imprimirlo.

  Ej: 
    objeto_enumerado = myEnumerate(
    ["Pasta", "Ensalada", "Bebida", "Carne", "Aperitivo"], 10)

    print(dict(list(objeto_enumerado)))
    
    >>> {10: 'Pasta', 11: 'Ensalada', 12: 'Bebida', 13: 'Carne', 14: 'Aperitivo'}
"""

def myEnumerate(iterable, contador):
    for ele in iterable:
        yield(ele, contador) 
        contador += 1

objeto_enumerado = myEnumerate(["Pasta", "Ensalada", "Bebida", "Carne", "Aperitivo"], 10) 

print(dict(list(objeto_enumerado)))

