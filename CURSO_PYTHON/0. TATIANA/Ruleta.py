# hacer un programa que pregunte 5 nombres y al final te devuelva si están vivos o muertos cada uno. 
# Ejemplo de resultado:
# A: Estás vivo
# E: Estás vivo
# I: Estás vivo
# O: Estás muerto
# U: Estás vivo
# el numero que salga en random es el que estará muerto. Tengo que hacer que cuente a las personas y diga si está vivo o merto.
# ahora pregunta el nombre tantas veces como se diga que si y cuando se diga que no sale la lista de vivos y muerto
import random

nombres =[] 
def ruleta():
    pregunta_nombres = input('Deseas introducir un nombre? Si / No: ')
    pregunta_nombres = pregunta_nombres.capitalize()

    if pregunta_nombres == 'Si':
        nombre_introducido = input('Introduce un nombre: ')
        nombres.append(nombre_introducido)
        print(nombres)
        ruleta()
    else:
        dead = random.randint(1, len(nombres))
        dead = dead -1
        counter = 0
        for nombre in nombres:
            if counter == dead:
                print(nombre, " ha muerto")
            else:
                print(nombre, " está vivo")
            counter += 1  


ruleta()
