# Escriba un programa para generar todas las permutaciones de una lista.
# ► Entrada:
# numList = [1,2,3]
# ► Salida:
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

#AYUDA:
# El módulo itertools proporcionado por Python, sirve para crear iteradores para un bucle eficiente. 
# Para generar una permutación de elementos, nos enfocaremos en los iteradores combinatorios 
# con itertools.permutations(). La sintaxis es la siguiente:
# permutations(iterador, longitud)
# La función permutations() toma dos argumentos:
# iterador: Elementos a permutar.
# longitud (opcional): Extensión o longitud de la permutación. Se asume la longitud predeterminada del iterador, si no se coloca este argumento, devuelve todas las posibles permutaciones según la cantidad de elementos.
# from itertools import permutations   
      
# PERMUTACIONES PARA UNA LISTA:  
# print(list(permutations([1, 'geeks'], 2)))   
   
# PERMUTACIONES PARA CADENAS:  
# print(list(permutations('AB')))   
      
# PARA UN RANGO DE NÚMEROS:  
# print(list(permutations(range(3), 2)))

from itertools import permutations

lista = ('abc')
numList = [1,2,3]

print(list(permutations(lista))) # en este caso permutamos la variable lista.
print(list(permutations(numList))) # en este caso permutamos la variable numlist

print(list(permutations([1, 'geeks', 7, 'hola'], 4))) # el número que hay después de la coma significa la cantidad de items
# que quieres permutar. En este caso hay 4 items y permutaremos los 4. En este caso no hace falta que haya una variable hecha.


