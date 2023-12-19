# Escriba un programa que acepte un número entero (n) 
# y calcule el valor de este número de la siguiente manera: n + nn + nnn
# ► Ejemplo:

# Valor de Entrada: 5
# Operación: 5 + 55 + 555
# Resultado: 615

numero = int(input('Ingresa un número: '))

numero_1 = int(numero * 11)
numero_2 = int(numero * 111)

# SU FORMA DE HACERLO:
# numero_1 = int("%s" %(numero))
# numero_2 = int("%s%s" %(numero,numero))
# numero_3 = int("%s%s%s" %(numero,numero,numero))


print('El total es: ',numero + numero_1 + numero_2)
