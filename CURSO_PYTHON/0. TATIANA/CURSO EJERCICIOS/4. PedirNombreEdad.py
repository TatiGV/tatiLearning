#Cree un programa que solicite al usuario su nombre y su edad.   
#Imprimir un mensaje personalizado con el nombre del usuario 
#que indique el año en el cual la persona cumplirá 100 años.

nombre = input('Indique su nombre: ')
edad = int(input('Indica tu edad: '))

año = ((2023 - edad) + 100 )

print(f'{nombre}, en el {año}, tendrás 100 años')


