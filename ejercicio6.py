"""
 => Ejercicio 6:
      Extender el ejercicio anterior, crear una función ordenarPorCategoria 
      que reciba como param el diccionario, que devuelve la función asociar, 
      y devuelva un nuevo diccionario ordenado por categoria.

      Ej: 
        print(ordenarPorCategoria(diccionario))

        >>> {
          'Roberto': 'Categoria A', 
          'Juli': 'Categoria B', 
          'Carlos': 'Categoria C', 
          'Marta': 'Categoria D'
          }
"""
from operator import itemgetter

empleado = ['Juli', 'Carlos', 'Roberto', 'Marta']
categoria = ['Categoria B', 'Categoria C', 'Categoria A', 'Categoria D']

def asociar(lista1, lista2):
    
    return dict(zip(lista1, lista2))

diccionario = asociar(empleado, categoria)    

# for key, value in diccionario.items():
#     print(key, value)  
    
    
def segundoElemento(una_lista):
    """ La fn espera recibir una lista de dos elementos
    y devuelve el segundo."""
    return una_lista[1]


def ordenarPorCategoria(dict_a_ordenar: dict) -> dict:
    
    lista_ordenada = sorted(dict_a_ordenar.items(), key=itemgetter(1))
    return lista_ordenada

print(ordenarPorCategoria(diccionario))

    
    
