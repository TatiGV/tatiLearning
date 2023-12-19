# Se dará cuatro opciones al usuario: 
#     Ver Catálogo(V) 
#     Añadir a la cesta (A) 
#     Eliminar de la cesta (E)
#     Finalizar compra (F)
# -------------------------------------------------------------------------------------------
# Ver Catálogo:
#     Muestra la lista de objetos y sus precios
#     Ejemplo:
#         Cebolla: 2€
#         Patata: 1€
#         Zanahoria: 3€
# ------------------------------------------------------------------------------------------------
# Añadir a la cesta:
#     Pregunta al usuario "¿Qué quieres añadir?
#         - Si lo que introduce el usuario existe en el catálogo, 
#    se lo guarda en la cesta y si ya existía en la cesta sumará 1 a la cantidad. 
#         Además volverá a mostrar las opciones
#         - Si no existe en el catálogo mostrará el mensaje "No existe en el catálogo" 
#         y volverá a mostrar las opciones.
# -------------------------------------------------------------------------------------------------
# Eliminar de la cesta:
#     Pregunta al usuario "¿Qué quieres Eliminar?
#         - Si lo que introduce el usuario existe en el cesta, 
#         lo elimina  y si ya existía en la cesta restará 1 a la cantidad. 
#         Además volverá a mostrar las opciones
#         - Si no existe en la cesta mostrará el mensaje "No existe en la cesta" 
#         y volverá a mostrar las opciones.qa.-
#  --------------------------------------------------------------------------------------------------
 # Finalizar compra:
#     - Si no tiene productos en la cesta mostrará "No has comprado nada" y finalizará el programa
#     - Si la cesta contiene productos mostrará el listado de estos, con sus cantidades,
#     precio unitario, precio por cantidad y precio total de la compra. Finalmente finalizará el programa.
#     Ejemplo:
#     2 Agua -> 0.5€ -> 1€
#     1 Cebolla -> 2€ -> 2€
#     5 Patata -> 1€ -> 5€
#     ---------------------
#     Total -> 8€


catalog = { 
     
    "Agua": 0.5,
    "Cebolla": 2,
    "Patata": 1,
    "Huevos": 2.75
}

cart = {}


def purchase():
    global purchase_options
    purchase_options = input('¿Qué desea hacer? : Ver Catálogo(V) / Añadir a la cesta (A) / Eliminar de la cesta (E) / Finalizar compra (F): ')
    purchase_options = purchase_options.upper()
    
    if purchase_options == 'V':
         see_catalog()
    elif purchase_options == 'A': 
         add_cart()
    elif purchase_options == 'E': 
         delete()
    elif purchase_options == 'F':
         exit_purchase()
    else:
         print("Opción incorrecta")
         purchase()

def see_catalog():
        for products in catalog:
            print(products,':', catalog[products],'€')
        purchase()

def add_cart():
        add_product = input('Añadir a la cesta: ')
        add_product = add_product.capitalize()
        
        if add_product in catalog.keys():
            if add_product in cart:
                cart[add_product] = cart[add_product] + 1
            else:
                cart[add_product] = 1
            print(cart)
            purchase()
        else:
            print('No existe en el catálogo')
            purchase()
           
def delete():
    delete_product = input('¿Que producto quieres eliminar?: ')
    delete_product = delete_product.capitalize()
    if delete_product in cart:
        cart[delete_product] = cart[delete_product] - 1
        if cart[delete_product]  <  1:
             cart[delete_product] = 0
             print('No queda más de ese producto')
             purchase()
    else:
         print('Este producto no existe en la cesta')
         purchase()
            
    print(cart)
    purchase()
        
def exit_purchase():
     if cart.items():
        total = 0
        for products, quantity in cart.items():
            price_product = catalog[products] * quantity
            print(quantity, products, '->', catalog[products],'€', '->', price_product ,'€')
            total += price_product
        print('TOTAL', total,'€')
     else:
          print('No has comprado nada')
          
     
     



purchase()



