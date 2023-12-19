diccionario = {1 : 2, 2 : 3, 3 : 4}
# diccionario2 = {4 : 5, 6 : 7}

# print(diccionario) # imprime el diccionario {1: 2, 2: 3, 3: 4}

# diccionario.pop(3) # esto elimina el número de la clave que quieres eliminar
# print(diccionario) # ha eliminado la key 3:4 {1: 2, 2: 3}

# diccionario.clear() # borra todo lo que hay dentro del diccionario
# print(diccionario) # sale esto : {}

# print(diccionario.get(2)) # Te imprime el valor de la clave que le pongas en los (). tienes que ponerlo directamente dentro del print en este caso es el numero 3

# diccionario.setdefault(4, 5) # Agrega la clave y el valor que pongas en los (). {1: 2, 2: 3, 3: 4, 4: 5}
# print(diccionario)

# diccionario.update(diccionario2) # esto actualiza los datos cuando hay dos diccionarios los une {1: 2, 2: 3, 3: 4, 4: 5, 6: 7}
# print(diccionario)

diccionario.copy() # Te hace una copia del diccionario (a mi no me funciona)
print(diccionario)