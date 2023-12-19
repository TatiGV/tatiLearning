lista = [1, 2, 3]
lista2 = [4, 5, 6]

lista3 = lista + lista2
print(lista3) # me devuelve una unica lista [1, 2, 3, 4, 5, 6] solo funciona suma(esto no es concatenar)

print('Esto es una lista de distintos datos: ', lista3) # esto es concatenar

lista4 = []

edad = int(input('ingresa tu edad: '))
lista4.append(edad) # Esto incorpora datos a la lista vacia.
print(lista4)


