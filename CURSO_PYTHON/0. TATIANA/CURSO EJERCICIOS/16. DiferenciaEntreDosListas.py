# Escriba un programa para obtener la diferencia entre las dos listas.

# ► Entrada:
# list1 = [1, 2, 3, 4]
# list2 = [1, 2]

# ► Salida:
# [3,4]

list1 = [1, 2, 3, 4]
list2 = [1, 2]

print(list(set(list1) - set(list2)))

