# Programa que solicite al usuario los datos para calcular el área de un Triángulo (▲), 
# finalmente mostrar el resultado en pantalla.
# ► Fórmula: Área del Triángulo
# Area = (Base*Altura)/2

base = int(input('Inserte el valor de la base: '))
altura = int(input('Inserte el valor para la altura: '))

float_Area = int(base * altura) / 2

print('El área del triángulo es de: ', float_Area, 'm2')
