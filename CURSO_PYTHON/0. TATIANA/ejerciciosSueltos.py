'''
datos = int(input('Ingresa un número: '))
total = datos ** 2

print('El área del cuadrado es: ',total)

------------------------------------------------------------------------------------------

for fila in range(1,5+1):
    for columna in range(1, 5 + 1):
        print(fila*columna, end='')
    print('')

-------------------------------------------------------------------------------------------------------

sueldo = int(input('Introduce tu sueldo: '))
#sueldo = sueldo%2

if sueldo%2 == 0:
    print('es par')

else:
    print('es impar')


-----------------------------------------------------------------------------------------------------------

peso1 = float(input('Introduce el primer peso molecular: '))
peso2 = float(input('Introduce el segundo peso molecular: '))
atomo1 = float(input('Introduce el primer Atomo: '))
atomo2 = float(input('Introduce el segundo Atomo: '))

pesoMolecuar = (peso1 * atomo1) + (peso2 * atomo2)

print('El peso molecular es:', pesoMolecuar)

-------------------------------------------------------------------------------------------------------------

hours = ['12:00', '14:00', '16:00']
space = ''
line = ','

for time in hours:
    space = space + time + line
print(space.removesuffix(','))

-----------------------------------------------------------------------------------------------------------

my_number = 19

guess = 0

max_guess = 3

while guess < max_guess:

    number = int(input('Inserte un numero: '))
    guess += 1
    
    if number == my_number:
        print('Lo conseguiste!!!')
        break
    elif guess == 3:
        print('No lo has conseguido!')
        break
    else:
        print('Prueba de nuevo!!')

SEGUNDA FORMA DE HACERLO:      

while guess < max_guess:

    number = int(input('Inserte un numero: '))
    guess += 1

    if guess == 3 :
        print('No lo has conseguido!')
        break

    if number != my_number:

        print('Prueba de nuevo!!')
    
    else:
        print('Lo conseguiste!!!')
        break
        
----------------------------------------------------------------------------------------------------------    

NO ES NECESARIO CREAR UNA LISTA EN UNA VARIABLE, SE PUEDE PONER DIRECTAMENTE EN EL FOR:

for char in ['yo', 'amo', 'programar']:
    print(char)

------------------------------------------------------------------------------------------------------------

'''