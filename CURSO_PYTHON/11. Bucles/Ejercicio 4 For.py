# Pedir al usuario que ingrese 2 numeros, después, 
#  se debe mostrar el rango de esos 2 números, pero,
# solo imprimiendo los números que sean impares

num1 = int(input('Ingresa el primer número: '))
num2 = int(input('Ingresa el segundo valor: '))


for i in range(num1, num2+1):
    if i % 2 != 0:
        print(i)
 
#COMO LO HA HECHO EL PROFE:

for j in range(num1, num2+1):
    if j % 2 == 0:
        continue
        print(j)

    

