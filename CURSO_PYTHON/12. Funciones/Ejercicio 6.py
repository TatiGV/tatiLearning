# Escribir una función que reciba una muestra de números en una tupla y devuelva su medida.
def medida(*tupla):
    
    return len(tupla)

print(medida(5, 7, 10, 8))

# Escribir una función que reciba una muestra de números en una lista y devuelva la media de los numeros de la lista.
def lista(*num):
   inicio = 0
   for i in num:
        inicio = inicio + i / len(num)
      
   return inicio

print(lista(3, 7, 8))
