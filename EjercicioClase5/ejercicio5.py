
"""
 => Ejercicio 5:
      Realizar una función asociar() que reciba como parametro dos listas 
      de la misma longitud de elementos y devuelva un diccionario de pares 
      clave-valor asociando cada elemento de ambas listas segun su indice. 

      Ej:
        empleado = ['Juli', 'Carlos', 'Roberto', 'Marta']
        categoria = ['Categoria B', 'Categoria C', 'Categoria A', 'Categoria D']

        diccionario = asociar(empleado, categoria)

        print(diccionario)

        >>> {
            'Juli': 'Categoria B', 
            'Carlos': 'Categoria C', 
            'Roberto': 'Categoria A', 
            'Marta': 'Categoria D'
          }
"""

empleado = ['Juli', 'Carlos', 'Roberto', 'Marta']
categoria = ['Categoria B', 'Categoria C', 'Categoria A', 'Categoria D']

def asociar(lista1, lista2):
    
    return dict(zip(lista1, lista2))

diccionario = asociar(empleado, categoria)    

for key, value in diccionario.items():
    print(key, ":", value)