
'''for i in range(10):

    print(i)
______________________________________________

for x in range(100, 200):
    print(x)
_________________________________________________
for y in range(5, 20, 3):
    print(y)
__________________________________________________
numero = int(input('Ingresa un número: '))

for i in range(numero, numero*2):

    print(i)
________________________________________________________
cantidad = int(input('Ingresa una cantidad de números: '))

total = 0

for i in range(cantidad):
    numero = int(input('numero: '))

    total += numero  # total = total + numero (es igual)

print('El total es: ', total) #fuera del bucle
__________________________________________

frase = input('Frase: ')
print('vocales en la frase: ')

for x in 'aeiou':
    if x in frase:
        print(x) 
___________________________________________ 


frase = input('Frase: ')

cantidad = 0

for i in frase:
    if i in 'aeiou':
        cantidad += 1

print('Cantidad de vocales: ', cantidad)



palabra = input('Escribe una palabra: ')

for i in range(10):
     print(palabra)
________________________________________________________________

num1 = int(input('Escribe un numero: '))
num2 = int(input('Escribe un numero: '))

for i in range(num1, num2+1, 1):
    if i %2 == 0:
        print(f'El número {i} es par') # la f es como si hiciera el .format
   
    else:
        print(f'El número {i} es impar')
___________________________________________________________________________________________________

ages = [20, 1, 3, 56]
nums = [4, 7, 32]
nums2 = ages + nums #esto suma las dos listas(las almacena en una sola variable)
nums2.sort() # ordena de menor a mayor

print(nums2)
print(sum(nums2))
print(max(nums2))
print(min(nums2))
print(len(nums2))
print(nums2.count(20)) # count cuenta el número de veces que está repetido el item que se ponga entre parentesis
print(20 in nums2) # esto te devuelve un tre o false dependiendo si está en la lista o no
nums2.reverse() # ordena de mayor a menor
print(nums2)
______________________________________________________________________________________________

def mylist():
    lista1 = [1, 5, 9]
    lista2 = ['a', 'b', 'c']
    lista3 = lista1 + lista2

    print(lista3)

mylist()

___________________________________________________________________________________________
'''





















