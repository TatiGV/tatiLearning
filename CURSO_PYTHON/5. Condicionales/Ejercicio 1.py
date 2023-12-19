letra = input('Escribe una letra: ').lower()

# ASI ES COMO YO LO HE HECHO:

'''if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('Es vocal')

else:
    print('No es una vocal')'''

#ASÍ ES COMO LO HA HECHO EL PROFE:

if letra in 'aeiou': # IN devuelve True si un elemento se encuentra dentro de otro (en este caso dentro de las '').
    print('Es vocal')

else:
    print('No es una vocal')

