# se juega con un solo dado que se lanza varias veces seguidas (cantidad decidida al principio del juego).
# La puntuación obtenida en cada tirada se va acumulando y se van obteniendo totales parciales. Tras cada tirada, 
#si el total es par, Cubitus gana un punto, pero si el total es impar, Humerus gana un punto. 
#El jugador que acaba teniendo más puntos, gana.

#Escriba un programa que muestre una partida de este juego, 
#detallando quién gana el punto y la puntuación de cada jugador tras cada tirada.

import random

numero_dados = int(input('¿Cuantos dados tirarás? '))
total = 0
contador1 = 0
contador2 = 0
name1 = "Cubitus"
name2 = "Humero"

if numero_dados > 0:
    for dados in range(numero_dados):
        tirada = random.randint(1,6)
        total = total + tirada
        print('Tirada', dados+1, ':', tirada)
        if total%2 == 0:
            contador1 += 1
            print('total = ',total, '---> punto para', name1)
            print('Puntuación acumulada:', name1, contador1, '-', name2, contador2)
           
        else:
            contador2 += 1
            print('total = ',total, '---> punto para', name2)
            print('Puntuación acumulada:', name1, contador1, '-', name2, contador2)
           
       
else:
     print('¡No se puede tirar menos de una vez el dado!')
     exit()

