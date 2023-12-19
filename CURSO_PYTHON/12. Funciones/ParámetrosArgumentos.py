


def suma(num1, num2):
    suma = num1 + num2
    return suma

def sumar():
    num1 = 20
    num2 = 30
    suma = num1 + num2
    return suma


# En el caso de que la función tenga parámetros no va hacer falta modificar nada dentro de ella
# ya que con solo poner como en este caso dos números se va a poder reutilizar sin modificar nada:

print(suma(20, 35))
print(suma(100, 50))

# FUNCIÓN ESTÁTICA:
# En este caso si quieres reutilizar la función siempre que la reutilizes el resultado será el mismo
# hasta que cambies los valores que hay en las variables de dentro de la función:

print(sumar())




