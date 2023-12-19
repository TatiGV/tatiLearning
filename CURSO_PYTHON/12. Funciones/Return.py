'''
El Return, es un valor que va a retornar la funcion. Cuando retornas un valor es necesario que sea impreso. 
Hay que poner print(funcion()) para que retorne lo que hay dentro de la función.



'''


def entero():
    print('este es un dato entero: ')
    return 10

def decimal():
    print('este es un dato decimal: ')
    return 90.99

def frase():
    return 'mi nombre es Tatiana'

def asignacion():
    return 1, 2, 3, 4, 5

print(entero())
print(decimal())
print(frase())
a, b, c, d, e = asignacion() # se puede hacer varias variables con comas. Aque se ha asignado la función a la variable

print(a) # esto devuelve 1
print(b) # esto devuelve 2

# los valores que esta devolviendo esta funcion está siendo igualado a la variable y printa el valor de la variable que se le asigne.

