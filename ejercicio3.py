from functools import reduce

"""=> Ejercicio 3:
    Realiza una fn aculado, que devuelva el valor acumulado 
    de la suma de una lista de numeros mas 100.

    Ej: 
      mis_numeros = [2, 4, 6]

      valor_final = acumulado(mis_numeros)

      print(mis_numeros)

      >>> 112
"""

mis_numeros = [5, 4, 1]

def acumulado():
   
    suma = reduce(lambda x, y: x + y, mis_numeros)
    print(suma + 100)     
 
acumulado()  
