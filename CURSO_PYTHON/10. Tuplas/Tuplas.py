# es una lista que NO se puede modificar. Son inmutables. NO TIENE MÉTODOS PORQUE LOS METODOS MODIFICAN DATOS
tupla = (1, 2, 3, 4, 5) # se puede poner sin los paréntesis. pero es recomendable
tupla2 = (5, 6, 7, 8)

print(tupla)
print(type(tupla))
print(tupla[2]) # Te imprime el dato que haya en la posición que pones en los [] 3
print(tupla[0 : 3]) # Hace lo que hace el debanado (1, 2, 3)
print(tupla + tupla2) # añade la tupla2 a la tupla1 (1, 2, 3, 4, 5, 5, 6, 7, 8)

tupla[2] = 10
print(tupla) # da error porque una tupla no se puede modificar // TypeError: 'tuple' object does not support item assignment






