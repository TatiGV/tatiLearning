

def valores():
    global num1 # con la palabra global puedes reutilizar fuera de la función la variable
    global num2
    num1 = 110
    num2 = 40
    resultado = num1 + num2
    return resultado

print(valores())

resta = num1 - num2 # coge los datos de dentro de la función gracias a la palabra global
print(resta)

