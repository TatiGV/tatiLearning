#Programa que solicite al usuario los datos para calcular el área de un Círculo (●),
# finalmente mostrar el resultado en pantalla.
# ► Fórmula: Área del Círculo
# Area = PI*(Radio**2)

int_Radio = int(input('Inserte un valor para calcular el área del circulo: '))

pi = 3.14

float_Area = pi * (int_Radio ** 2)

print('El área del circulo es: ', float_Area, 'm2')



