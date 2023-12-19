# and = para que sea True se tienen que cumplir las dos condiciones, si una es falsa el resultado es False:

print(10 > 2 and 9 > 100) # False porque una de las dos es falsa
print(23 == 23 and 10 > 8 ) # True porque las dos son verdaderas
print(20 < 50 and 5 > 20) # False porque las dos son falsas

# != = Diferente

print(99 != 99) # False
print(30 != 89) # True

# or = al contrario que el 'and', si una de las condiciones es verdadera el resultado es True

print(50 > 20 or 90 < 30) # True, porque una de las dos es verdadera
print(50 >= 60 or 60 >= 90) # False porque las dos son falsas

# not = cambia el resultado

print(not 90 != 90) # da True, mientras que tendría que dar False
print(not 50 > 20) # da False, mientras que tendría que dar True
