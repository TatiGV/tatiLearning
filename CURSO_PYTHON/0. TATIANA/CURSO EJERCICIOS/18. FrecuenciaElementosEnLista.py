# Escriba un programa para obtener la frecuencia de los elementos en una lista.

# ► Entrada:

# lista = ['A','A','A','B','B','B','C','C']

# ► Salida:

# Lista Original: ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C']
# Frecuencia de Elementos: Counter({'A': 3, 'B': 3, 'C': 2})
import collections

lista = ['A','A','A','B','B','B','C','C']

frecuencia = collections.Counter(lista) #para utilizar collection primero hay que importarlo.
# El punto Counter(C mayuscula) sirve para contar cuantos elementos de la isma clase hay en una lista.

print('Frecuencia de los elementos: ', frecuencia)
