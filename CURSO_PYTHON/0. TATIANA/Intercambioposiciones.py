# Dado un diccionario del ranking del top manta, hacer un programa que te permita reordenarlos
# Ejemplo:
#     Ranking
#     --------
#     1. Mojinos
#     2. Manolo Escobar
#     3. Gigatron
#     4. Marisol
#     5. Chimo Bayo
#     "Elige la posición origen que quieres cambiar"
#         2
#     "Elige la posición destino que quieres cambiar""
#         5
#     Ranking
#     --------
#     1. Mojinos
#     2. Chimo Bayo
#     3. Gigatron
#     4. Marisol
#     5. Manolo Escobar

top_manta = {
    1 : "Mojinos",
    2 : "Manolo Escobar",
    3 : "Gigatron",
    4 : "Marisol",
    5 : "Chimo Bayo"
}

def change_position():
    print('Ranking:')
    for position, artist in top_manta.items():
        print(position,'.', artist)
    choose_position1 = int(input('Elige la posición origen que quieres cambiar: '))
    choose_position2 = int(input('Elige la posición destino que quieres cambiar: '))

    name1 = top_manta[choose_position1]
    name2 = top_manta[choose_position2]

    top_manta[choose_position1] = name2
    top_manta[choose_position2] = name1
    

    for position, artist in top_manta.items():
        print(position,'.', artist)

       
        
    


    



change_position()


