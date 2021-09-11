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

listaNumeros = [1, 2, 412, 543, 634, 1234, 62, 6474, 5, 2]

def separar(listaNumeros):
    
    listaPares = []
    listaImpares = []
   
    for elemento in listaNumeros:
        if elemento % 2 == 0:
            listaPares.append(elemento) 
        else:
            listaImpares.append(elemento)
            
    print("Lista pares: ", listaPares)
    print("Lista impares: ",  listaImpares)        
            
        
separar(listaNumeros)