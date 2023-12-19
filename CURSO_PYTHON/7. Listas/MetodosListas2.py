lista = [5, 3, 2, 4, 1]

# Hay métodos que funcionan solo metiéndolos dentro del print:
print(lista.count(5)) # Esto te dice la cantidad del valor que pones en los () que hay en la lista (en este caso solo hay un 5)
print(lista.index(4)) # busca en la lista el primer valor de dentro de los() (si hay varios valores iguales en la lista , 
# solo te dice la posicion del primero que encuentra, en este caso la posicion en la que está el 4 es la 3)

# HAY METODOS QUE TIENES QUE PONER PRIMERO LA VARIABLE PUNTO LO QUE SEA Y DESPUES PRINTAR
lista.sort() # esto ordena la lista de menor a mayor [1, 2, 3, 4, 5]. este metodo no lleva parametro dentro de los parentesis.
print(lista)
lista.reverse() # esto ordena la lista de mayor a menor [5, 4, 3, 2, 1]. este metodo no lleva parametro dentro de los parentesis.
print(lista) 

