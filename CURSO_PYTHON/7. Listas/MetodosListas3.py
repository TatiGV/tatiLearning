lista = ['Python', 24, 'Rene', 'alexander', 12]

lista[3] = 'Alexander' # esto te modifica un dato de dentro de la lista ['Python', 24, 'Rene', 'Alexander', 12]
#print(lista)

lista.pop() # esto elimina el ultimo dato de la lista(solo elimina el ultimo) ['Python', 24, 'Rene', 'Alexander']
print(lista)
# Pero si lo metes directamente dentro del print o sea print(lista.pop()) te imprime solo el dato eliminado en este caso es el 12

lista.remove('Rene') # elimina el valor que pongo entre () ['Python', 24, 'Alexander']
print(lista)
