# El asterisco dentro del parámetro hace que puedas poner varios argumentos cuando llamas a la función

def argumento(*num):
    return type(num)

print(argumento(10, 20, 5, 30))

def argument(*num2):
    for i in num2: # este for recorre la lista de numeros que pongas como argumentos.
        print(i)


argument(10, 20, 30)
