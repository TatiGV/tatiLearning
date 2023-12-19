# Escribir un programa que lea un entero positivo,
# introducido por el usuario y después muestre en pantalla 
# la suma de todos los enteros desde 1. 
# La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:
# suma =n(n + 1)/ 2


numero = int(input('Inserte un número entero positivo: '))
suma = int(numero * (numero + 1) / 2)

print('La suma desde 1 hasta', numero, 'es', suma)

