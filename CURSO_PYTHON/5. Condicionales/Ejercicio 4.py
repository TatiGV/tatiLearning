voto = input('Ingresa el voto de tu partido (A,B,C): ')

if voto.upper() == 'A':
    print('Tu voto es para el partido rojo')
elif voto.upper() == 'B':
    print('Tu voto es para el partido Azul')
elif voto.upper() == 'C':
    print('Tu voto es para el partido Verde')
else:
    print('Opcion erronea')
    