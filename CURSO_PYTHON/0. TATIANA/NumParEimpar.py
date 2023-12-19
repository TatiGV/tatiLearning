
# EJERCICIO NUMEROS PARES E IMPARES
'''
si ponemos %2 == 0, esto sacará los numeros pares, si no ponemos nada o ponemos != 0, sacará los impares. EJEMPLO:
'''

numero = int(input('ingrese un numero: '))
numero2 = int(input('ingrese un numero: '))

for num in range(numero, numero2+1):
    if num%2 == 0: # este de aqui sacara los numeros pares
        print(num)
    
'''
for num in range(numero, numero2+1):
    if num%2:
        print(num)

ESTE FOR SACARA LOS IMPARES
'''
    




