# Escriba una función que tome una lista de palabras y devuelva la longitud de la más larga.
# ► Entrada:
# lista_inicial = ["C#","Python","Javascript"]
# ► Salida:
# Lista Ordenada: ['C#', 'Python', 'Javascript']
# Mayor Longitud: 10
# Cadena Mayor  : Javascript

def palabra_mas_larga(lista_inicial):
    palabra_longitud = []

    for i in lista_inicial:
        palabra_longitud.append((len(i), i))

    palabra_longitud.sort()
    print('lista ordenada: ',palabra_longitud)

    return palabra_longitud[-1][1]

lista_inicial = ["C#","Python","Javascript"]
print('Cadena mayor: ',palabra_mas_larga(lista_inicial))

# mayor = -1
# lista_inicial.sort(key=len)

# print(f'Lista Ordenada: {lista_inicial}')
# print(f'Mayor Longitud: {len(lista_inicial[mayor])}')
# print(f'Cadena Mayor  : {lista_inicial[mayor]}')
