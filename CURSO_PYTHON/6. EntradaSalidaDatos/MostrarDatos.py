nombre = input('Ingresa tu nombre:')
edad = int(input('Ingresa tu edad:')) # cuando la variable es un número tienes que decir si es INT o FLOAT

# print('Hola', nombre, 'tienes', edad) e

print('Hola', nombre, 'tienes', edad, 'años')
print('Hola {} tienes {} años'.format(nombre, edad)) # Esta manera de imprimirlo es con .format()
print(f'hola {nombre}, tines {edad} años') # Esta forma es la más utilizada