

practica1 = float(input('Ingrese el valor de Practica 1:'))
practica2 = float(input('Ingrese el valor de Practica 2:'))
practica3 = float(input('Ingrese el valor de Practica 3:'))
examenParcial = float(input('Ingrese el valor de Examen Parcial:'))
examenFinal = float(input('Ingrese el valor de Examen Final:'))

promedioPractica = (practica1 + practica2 + practica3) / 3
promedio = ( promedioPractica + (2 * examenParcial) + (3 * examenFinal)) / 6

print('El promedio practica del estudiante es de:\n', promedioPractica, '\n y el promedio final del estudiante es de:\n', promedio)



