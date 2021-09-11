"""
=> Ejercicio 2:
    Realiza una función que tome como parametro una frase y devuelva una 
    lista de palabras en mayuscula. 

      Ej: 
        mi_frase = "Este sabado tenemos el ultimo encuentro online"

        palabras = convertir(mi_frase)

        print(palabras)

        >>> ["ESTE", "SABADO", "TENEMOS", "EL", "ULTIMO", "ENCUENTRO", "ONLINE"]
"""

mi_frase = input("Ingresá un texto a elección: ")

def convertir(frase):
    
    listaFinal = []
    list = frase.split()
    
    for i in list:
        listaFinal.append(i.upper())
    
    print(listaFinal)
    
convertir(mi_frase)  