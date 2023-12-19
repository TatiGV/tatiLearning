lista = ['Python', 120, 'Nombre', 4.14, 6.28]

print(lista)
print(lista[3]) # cuando imprimes te imprime el dato que está en la posicion 3 (teniendo en cuenta de que empieza por 0) que es 4.14
print(len(lista)) # te dice cuantas posiciones tiene la lista, en este caso son 5 [0,1,2,3,4]
lista[0] = 'Tati' # esto hace posible que puedas cambiar un dato de dentro de la lista

print(lista) # ['Tati', 120, 'Nombre', 4.14, 6.28] se ha cambiado 'Python' por 'Tati'

