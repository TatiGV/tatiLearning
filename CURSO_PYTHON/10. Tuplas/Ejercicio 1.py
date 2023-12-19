#Escribir una tupla con los meses del año, 
#  luego, pide al usuario un numero, el que haya ingresado, 
#es el mes que debe mostrar en la tupla

tupla = ('Enero', 'Febrero', 'Marzo', 'Abril','Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

numero =int(input('Ingresa un número para que salga el mes correspondiente: '))
numero -= 1

print('El mes correspondiente al numero elegido es: ',tupla[numero])



