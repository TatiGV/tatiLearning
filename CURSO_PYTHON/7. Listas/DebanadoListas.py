lista = [10, 20, 3.14, 'Water', 'Coto', 7, 'Estudiante', 'Cuaderno']

print(lista[5]) # esto va a printar el 7
print(lista[0 : 5]) # esto va a printar [10, 20, 3.14, 'Water' Coto] (recordar que no imprime 5 si no que imprime uno menos)
print(lista[ : 2]) # esto muestra el 10 y el 20 ya que el de la derecha no lo coge
print(lista[1 : ]) # esto empieza desde el 20 hasta el final [20, 3.14, 'Water', 'Coto', 7, 'Estudiante', 'Cuaderno']
print(lista[-1]) # mostrará la palabra cuaderno porque si empieza desde atrás si que cuenta todos los numeros
print(lista[-5 : -2])# esto printa ['Water', 'Coto', 7]
