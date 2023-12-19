#Con el siguiente diccionario, debes crear un programa que pregunte al usuario por un número; 
# el programa debe imprimir el jugador al que hace referencia ese número

jugadores = {1 : "Casillas", 15 : "Ramos", 3 : "Pique", 5 : "Puyol", 11 : "Capdevila", 14 : "Xabi Alonso", 16 : "Busquets", 8 : "Xavi Hernandez", 18 : "Pedrito", 6 : "Iniesta", 7 : "Villa"}

numeroJugador = int(input('Indica el número de tu jugador: '))

numero2 = numeroJugador in jugadores

if numero2:
    print(jugadores[numeroJugador])

else:

    print('No existe ese número en la lista')

    
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
ASI LO HE HECHO MESES DESPUES:


jugadores = {

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}

numero = int(input('Inserte un numero: '))

if numero in jugadores.keys():
    print(jugadores[numero])
else:
    print('ese jugador no existe en la base de datos')

'''



