# Escribir una tupla que tenga las letras del alfabeto. 
#Luego, debes pedir al usuario un número, 
#el que haya ingresado, es la letra que debe imprimir el programa

tupla = ('a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

numero = int(input('Ingresa un numero para que te devuelva una leta: '))

print('La letra es: ', tupla[numero-1] )