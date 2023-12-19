# - Añade un título con un print() para la pizzería, algo como -> Pizzería PF <-.
# - El usuario introducirá el dinero que quiera. Guárdalo en una variable.
# - Crea una lista donde ir añadiendo los ingredientes extra. Pista: métodos de adición en listas.
# - Habrá mínimo tres tipos de pizzas para elegir (pon las que quieras).
# - Cada pizza tendrá un coste diferente.
# - El usuario podrá elegir solo una pizza.
# - Una vez elegida la pizza, se le informará al usuario del total que lleva por el momento.
# - Se le debe solicitar, si quiere o no, añadir ingredientes extra (estos harán subir el precio final).
# - Añade al menos 3 ingredientes extra. El usuario podrá elegir ninguno, uno o varios de estos. No hay limite
# de ingredientes extra. Si se pasa del dinero que tiene, se le dirá que no le llega y que vuelva a realizar el
# pedido.
# - Las pizzas e ingredientes, tendrán sus precios almacenados en variables o constantes (piensa que los
# precios son los que son y no deben variar en todo el programa).
# - Con cada ingrediente extra, se le debe ir sumando el precio al total y mostrárselo al usuario con el 
# cambio que le queda.
# - Si el usuario no quiere ingredientes extra, puede pagar directamente sin añadir ninguno.
# - Finalmente, se le debe presentar el ticket (imprimido en la consola) con el total gastado, 
# el cambio y todos los elementos que se han añadido al pedido, pizza, ingredientes extra y precios.
 

print('PIZZERIA TATIANA')

pizza = input('Elige la pizza que quieres: ')
pizza = pizza.capitalize()
costes_Pizzas = [10, 12, 14]
coste_pizza_seleccionada = 0
ingredientes_Extras = []
precio_ingrediente_extra = {'Jamon' : 1, 'Bacon' : 1, 'Champiñones' : 0.50, 'Extra queso' : 2}

if pizza == 'Margarita':   
    print(f'La pizza Margarita tiene un coste de: {costes_Pizzas[0]}€')
    coste_pizza_seleccionada = costes_Pizzas[0]
    dinero =float(input('Inserte el importe: '))
elif pizza == 'Barbacoa':
    print(f'La pizza Barbacoa tiene un coste de: {costes_Pizzas[1]}€')
    coste_pizza_seleccionada = costes_Pizzas[1]
    dinero =float(input('Inserte el importe: '))
elif pizza == 'Cuatro quesos':
    print(f'La pizza Cuatro quesos tiene un coste de: {costes_Pizzas[2]}€')
    coste_pizza_seleccionada = costes_Pizzas[2]
    dinero =float(input('Inserte el importe: '))
else:
    print('la pizza no existe, pida una que tengamos en la carta')
    exit()

print(f'dinero: {dinero} €')
total_restante = dinero - coste_pizza_seleccionada
if dinero >= coste_pizza_seleccionada:
    print(f'Importe restante: {total_restante} €')
else:
    print('No tiene suficiente dinero para esa pizza')
    dinero =int(input('Inserte el importe para la pizza que desea: '))

def ingrediente_extra():
    global total_restante
    global ingrediente
    ingrediente = input('Desea algún ingrediente extra? ')
    ingrediente = ingrediente.capitalize()
    
    if ingrediente == 'Si':
        global nuevo_ingrediente
        nuevo_ingrediente = input('Inserte el nuevo ingrediente (Jamon / Bacon / Champiñones / Extra queso)')
        nuevo_ingrediente = nuevo_ingrediente.capitalize()

        if nuevo_ingrediente == 'Jamon' or  nuevo_ingrediente == 'Bacon' or  nuevo_ingrediente == 'Champiñones' or nuevo_ingrediente == 'Extra queso':
            
            if total_restante < precio_ingrediente_extra[nuevo_ingrediente]:
                print('No tiene suficiente dinero para este ingrediente extra')
            else:                
                ingredientes_Extras.append(nuevo_ingrediente)
                print(ingredientes_Extras)
                total_restante -= precio_ingrediente_extra[nuevo_ingrediente]
                
                print('Total Euros: ',total_restante, '€')
        else:
            print('No se encuentra ese ingrediente')

        ingrediente_extra()
    else:
        devolucion = dinero - coste_pizza_seleccionada
        print('El importe total es: ', coste_pizza_seleccionada, '€')
        print('Cambio: ',devolucion ,'€')

def montrar_ticket():

    print('Ticket PIZZERIA TATIANA')
    print(pizza, '.....=',coste_pizza_seleccionada,'€')
    total = coste_pizza_seleccionada

    for i in ingredientes_Extras:
        print(i, '.....=', precio_ingrediente_extra[i],'€')
        total += precio_ingrediente_extra[i]
          
    print('Total:',total,'€')
    print('Importe entregado:',dinero,'€')

    devolucion = dinero - total

    print('Su cambio: ',devolucion,'€')
    print('GRACIAS POR SU VISITA')
          
ingrediente_extra()
montrar_ticket()