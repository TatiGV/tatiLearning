diccionario = {'Nombre' : 'Tatiana', 'Apellido' : 'Garcia', 'Estatura' : 1.63}

print(diccionario) # Muestra todo el diccionario {'Nombre': 'Tatiana', 'Apellido': 'Garcia', 'Estatura': 1.63}
print(diccionario.keys()) # Muestra solo las CLAVES {'Nombre', 'Apellido', 'Estatura'}
print(diccionario.values()) #Muestra solo los VALORES {'Tatiana', 'Garcia', 1.63}

print(diccionario['Apellido']) # Muestra el VALOR de la clave que pongas entre [] Garcia

diccionario['Peso'] = 58  # Esto agrega un nuevo valor a la cadena
print(diccionario)

diccionario['Nombre'] = 'Alberto' # con esto cambias un valor ya existente por otro valor
print(diccionario)