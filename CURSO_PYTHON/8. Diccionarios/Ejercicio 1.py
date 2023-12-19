# En el siguiente diccionario se encuentran capitales de los paises en el mundo,
# debes realizar un programa que pida un pais al usuario, 
# y muestre la capital de ese pais,en dado caso el pais no este en el diccionario, 
# se debe mostrar un mensaje diciendo que ese pais no se encuentra.

diccionario = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais = input('Inserte un pais: ')
countryExists =  pais.title() in diccionario


if countryExists:
    print(diccionario[pais.title()])
else:
    print('Este pais no se encuentra')

   # -------------------------------------------------------------------------------------------------------

'''
   
ASI LO HE HECHO MESES DESPUÉS:

capitales = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais = input('ingresa un pais: ')
pais = pais.capitalize()


if pais in capitales.keys():
    print(capitales[pais])
else:
    print('pais no se encuentra')


'''






