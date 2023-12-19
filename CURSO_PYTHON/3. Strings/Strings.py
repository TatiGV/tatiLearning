# Es importante escribir las cadenas con comillas dobles o simples. No hay que confundir un numero entre comillas y uno sin comillas. Ej: num1 = '1' (esto es string), num2 = 3 (esto es un interer)

print('Hola Mundo') # Hola Mundo

cadena = 'Esto es un \'ejemplo\'de cadena de texto' # poner \\ entre una palabra se llama string literal o escapar caracteres lo que hace es que muestra el mensaje bien sin el error que tiene de las comillas en 'ejemplo'
cadena1 = 'Esto es un \nejemplo de \ncadena de texto' # poner \n es un salto de linea
cadena2 = 'Esto es un \tejemplo de cadena de texto' # la \t hace una tabulación
cadena3 = 'Esto es un \bejemplo de cadena de texto' # la \b quita espacios


print(cadena)  # Esto es un \'ejemplo' \de cadena de texto
print(cadena1) # # Esto es un 
                #ejemplo de 
                #cadena de texto
print(cadena2) # Esto es un      ejemplo de cadena de texto

print(cadena3) # Esto es unejemplo de cadena de texto

