# Escribir una función que reciba un número entero positivo y devuelva su factorial. ejemplo: 5 = 1 * 2 * 3 * 4 * 5
 
'''
PRIMERA FORMA DE HACERLO:

def factorial():
    num = int(input('Inserta un numero entero positivo: '))
    if num > 0:
        factorial = 1
        for i in range(1 ,num + 1):
            factorial = factorial * i
        print(factorial)

    else:
        print('el numero es negativo y no es valido')

factorial()

'''
'''SEGUNDA FORMA DE HACERLO:'''

def factorial():
    from math import factorial
    num = int(input('Inserta un numero entero positivo: '))
    if num > 0:
       print(factorial(num))

    else:
        print('el numero es negativo y no es valido')

factorial()