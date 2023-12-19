# Hacer un programa que muestre las peliculas que hay con sus respectivos horarios.
# 1: "De qué pelicula quiere info? (Aladdin/One Piece)". Si no es ninguna de estas salir.
#   Si es una de estas, se mostrará su info tal que así:
#       Nombre: Aladdin
#       Precio: 5.70€
#       Horarios: 16:00, 19:00, 22:00
# 2: Preguntar si quiere comprar un tickets
#     Si -> Mostrar mensaje "Ticket comprado." Ir al paso 3 
#     No -> Volver al paso 1
# 3: Preguntar "Quieres palomitas?"
#     Si -> "De qué tamaño? (S: 2€, M: 3€, L: 4€)". Ir al paso 4
#     No -> "Gracias por su comprar". Finalizar programa
# 4: "Aquí tiene sus palomitas tamaño X, son Y€. Gracias!" Finalizar programa
data = {
   "movies":[
      {
         "name":"Aladdin",
         "price": 5.70,
         "hours":[
            "16:00",
            "19:00",
            "22:00"
         ]
      },
      {
         "name":"One Piece",
         "price":12.70,
         "hours":[
            "12:00",
            "16:00",
            "20:00",
            "23:00"
         ]
      }
   ]
}


def info_peliculas():
    elegir_info = input('¿De qué pelicula quiere la info? (Aladdin / One Piece): ')
    elegir_info = elegir_info.lower()
    elegir_info = elegir_info.replace(" ", "")

    if elegir_info == 'aladdin':
        
        data_movie = data["movies"]
        print('Nombre: ', data_movie[0]['name'])
        print('Precio: ', data_movie[0]['price'], '€')
        coma = ','
        espacio = ''
        for time in data_movie[0]['hours']:
            espacio = espacio + time + coma
        print('Horarios:',espacio.removesuffix(','))
      
    elif elegir_info == 'onepiece':
      data_movie = data["movies"]
      print('Nombre: ', data_movie[1]['name'])
      print('Precio: ', data_movie[1]['price'], '€')
      coma = ','
      espacio = ''
      for time in data_movie[1]['hours']:
            espacio = espacio + time + coma
      print('Horarios:',espacio.removesuffix(',')) # removesuffix te quita lo ultimo que le pongas entre comillas (en este caso la última coma)
      
      
    #   for time in data_movie[1]['hours']:
    #     linea = ','
    #     time += linea
      
         
    else:
        print('Esa pelicula no está en este cine')
        info_peliculas()

    question_ticket = input('¿Quieres comprar un ticket? (Si / No): ')
    question_ticket = question_ticket.capitalize()

    if question_ticket == 'Si':        
        print('Ticket comprado')


    else:
        info_peliculas()

    question_palomitas = input('¿Quieres palomitas (Si / No): ')
    question_palomitas = question_palomitas.capitalize()

    if question_palomitas == 'Si':
        tamaño_palomitas = {'S' : 2, 'M' : 3, 'L' : 4}
        tamaño = input('¿De qué tamaño (S / M / L): ?')
        tamaño = tamaño.capitalize()
        importe_total_aladdin = data_movie[0]['price']
        importe_total_onepiece = data_movie[1]['price']
        if tamaño == 'S':
               if elegir_info == 'aladdin':
                   print('El importe total es: ',importe_total_aladdin + tamaño_palomitas['S'], '€')
                   print('Gracias por su compra')
               else:
                   print('El importe total es: ',importe_total_onepiece + tamaño_palomitas['S'], '€')
                   print('Gracias por su compra')
        elif tamaño == 'M':
              if elegir_info == 'aladdin':
                   print('El importe total es: ',importe_total_aladdin + tamaño_palomitas['M'], '€')
                   print('Gracias por su compra')
              else:
                   print('El importe total es: ',importe_total_onepiece + tamaño_palomitas['M'], '€')
                   print('Gracias por su compra')
        else:
               if elegir_info == 'aladdin':
                   print('El importe total es: ',importe_total_aladdin + tamaño_palomitas['L'], '€')
                   print('Gracias por su compra')
               else:
                   print('El importe total es: ',importe_total_onepiece + tamaño_palomitas['L'], '€')
                   print('Gracias por su compra')
      
    else:
        if elegir_info == 'aladdin':
            total_aladdin = data_movie[0]['price']
            print('El importe total es: ',total_aladdin, '€')
            print('Gracias por su compra')
        else:
            total_onepiece = data_movie[1]['price']
            print('El importe total es: ',total_onepiece, '€')
            print('Gracias por su compra')

        
    



info_peliculas()

#   if elegir_info == 'aladdin':
#             importe_total += data_movie[0]['price']
#             print(importe_total)