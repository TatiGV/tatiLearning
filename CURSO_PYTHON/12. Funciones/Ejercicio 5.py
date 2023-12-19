# Crear un programa que tenga dos funciones,
# una que contenga el area de un cuadrado con argumentos de base y altura;
# y la otra el area de un circulo con argumento de radio.

def cuadrado(base, altura):
    return base * altura

def circulo(radio):
    area = 3.14 * (radio**2)
    return area

print(cuadrado(7,5))
print(circulo(5))




