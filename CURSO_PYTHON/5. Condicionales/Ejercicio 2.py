num1 = int(input('Inserta un número entero: '))


'''if num1 >= 0:
    print('El valor absoluto de {} es igual a {}'.format(num1, num1))

else:
    print('El valor absoluto del {} es:'.format(num1), num1 * -1)'''

# ESTA ES LA SEGUNDA FORMA DE HACERLO:
# SE UTILIZA LA FORMA ABS QUE DIRECTAMENTE DA EL NÚMERO ABSOLUTO EN POSITIVO AUNQUE METAS UN NEGATIVO

if num1 >= 0:
    print('El valor absoluto de {} es igual a {}'.format(num1, num1))

else:
    print('El valor absoluto del {} es: {}'.format(num1, abs(num1)))





