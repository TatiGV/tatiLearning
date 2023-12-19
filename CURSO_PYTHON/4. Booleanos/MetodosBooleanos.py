cadena = 'Estoy mostrando los metodos booleanos para las Strings'
cadena2 = 'estoy mostrando los metodos booleanos para las strings'

# metodo startwith = verifica si la cadena empieza por un dígito
# metodo endwith = verifica si la cadena termina por un dígito

print(cadena.startswith('E')) # True porque empieza por una 'E' mayuscula, si hubiesemos puesto minuscula hubiese printado False
print(cadena.endswith('g')) # False porque la cadena termina en 's'

# metodo isupper = verifica si la cadena está en mayusculas
# metodo islower = verifica si la cadena está en minusculas

print(cadena.isupper()) # False porque la cadena está en minusculas
print(cadena.islower()) # False porque la cadena está no está toda en minusculas
print(cadena2.islower()) # True porque toda la cadena está en minusculas 

