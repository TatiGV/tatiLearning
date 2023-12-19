# Escriba un programa que calcule la longitud de una cadena sin usar la funcion len().
# ► Entrada:
# cadena ='abcdefghijklmnopqrstuvwxyz'
# ► Salida:
# Longitud de la cadena: 26 caracteres

cadena ='abcdefghijklmnopqrstuvwxyz'
contador = 0

for caracter in cadena:
    contador += 1

print('Longitud de la cadena:', contador, 'carateres')



