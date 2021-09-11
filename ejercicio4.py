"""
   => Ejercicio 4:
    Realizar una fn mostrar, que reciba una lista de frutas y un numero, e imprima 
    un numero y el elemento asociado. 

    Ej: 

      frutas = ['Banana', 'kiwi', 'Pera', 'Naranja', 'Manzana']

      mostrar(frutas, 100)

      >>> 100 Banana
      >>> 101 kiwi
      >>> 102 Pera
      >>> 103 Naranja
      >>> 104 Manzana 
"""

numero = int(input("Ingrese un número: "))
frutas = ["Melón", "Sandia", "Pera", "Banana", "Tomate", "Manzana"]

def mostrar(frutas, numero):
   
    frutas_numeros = {}
   
    for i in frutas:
        frutas_numeros[numero] = i
        numero = numero + 1
        
    print(frutas_numeros) 
          
mostrar(frutas, numero)        