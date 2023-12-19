conjunto = {1, 2, 3, 4, 5}
lista = [1, 1, 2, 3, 4, 4]

print(lista) #la lista si permite datos repetidos
print(conjunto) # no te muestra los elementos repetidos

conjunto.add(20) # añade el elemento que pongas en los ()
print(conjunto)

conjunto.remove(1)# elimina el valor que pongas en los ()
conjunto.discard(2)# tambien elimina el valor que pongas en los ()
print(conjunto)

conjunto.pop() # elimina valores al azar cada vez que ejecutas
print(conjunto)

conjunto.update([1, 2, 3]) #añade los elementos que metas en el conjunto
print(conjunto)

conjunto.clear()# deja el conjunto vacio
print(conjunto)
