# Escriba un programa para eliminar elementos duplicados de una lista.

# ► Entrada:

# numList = [10,20,30,20,10,50,60,40,80,50,40]

# ► Salida:

# [10, 20, 30, 50, 60, 40, 80]

items_numericos = [10,20,30,20,10,50,60,40,80,50,40]

items_unicos = []
items_duplicados = set()
 
for elemento in items_numericos:
 
    if elemento not in items_duplicados:
        items_unicos.append(elemento)
        items_duplicados.add(elemento)
 
print(items_unicos)
