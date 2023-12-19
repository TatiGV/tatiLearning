#Programa que solicite al usuario los datos para llevar Grados Farenheit a Grados Celcius.
# ► Fórmula: Grados Farenheit a Grados Celcius
# celcius = (fahrenheit - 32.0) * 5.0 / 9.0

fahrenheit = int(input('Introduce los grados fahrenheit: '))

float_celsius = (fahrenheit - 32) * 5 / 9

print(f'{fahrenheit} ºF', f'es igual a: {float_celsius}', 'ºC' )
