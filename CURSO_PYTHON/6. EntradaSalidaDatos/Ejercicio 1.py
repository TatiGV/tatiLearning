from math import sqrt #equivalente a raiz cuadrada ej print(sqrt(100)) devuelve la raiz cuadrada de 100 que es 10

a = int(input('Ingresa el valor de a:'))
b = int(input('Ingresa el valor de b:'))
c = int(input('Ingresa el valor de c:'))
x1 = 0
x2 = 0

if ((b**2) - (4*a*c)) < 0:
    print('no se puede realizar esta operación')
else:
    x1 = (-b + sqrt((b**2) - (4 * a * c))) / (2 * a)
    x2 = (-b - sqrt((b**2) - (4 * a * c))) / (2 * a)
    print('La solución es: \nx1=', x1, '\nx2=', x2)

