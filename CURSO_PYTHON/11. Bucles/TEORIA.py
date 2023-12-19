'''
Los bucles reciben múltiples nombres, bucles, estructuras repetitivas, iterador, iteraciones.
Un bucle, tal como su palabra lo indica, es algo que se va a repetir.
Una parte fundamental de los bucles son los iteradores.
Los iteradores son aquellos que podemos recorrer usando un ciclo, entre ellos, las cadenas de texto
o estructuras de datos como las listas, las tuplas o los diccionarios. Permite recorrer una colección y devolver un valor al terminar.
sin un iterador el bucle seria infinito.

Los bucles son estructuras, que poseen un segmento de código que se repite tantas veces como se cumpla una condición. cuando la condición
se deje de cumplir el bucle finaliza.

Break es una forma de tener un bucle al llegar a una condición ya definida. Sirve para terminar un bucle en un punto especifico.

Hay dos bucles principales:

- WHILE: que significa 'Mientras'. Mientras la condición que hayamos puesto se cumpla se va a ir ejecutando.

n = 5
while n > o:
   print(n)
   n = n -1

print(¡DESPEGUE!) 

Tenemos el while, la condición y las instrucciones. Y por último el contador o.
primero hay que asignar una variable que en este caso es N que va a ser 5.
luego ponemos la condicion del while mientras N sea mayor a cero, va a imprimir n.
Si queremos que sea una cuenta de mayor a menor hay que poner la variable (dentro de while), diciendo que N va a ser igual a N-1,
va a ir iterando (dando vueltas) de 5 a 0 y cuando llegue a 0 va a aparecer el mensaje de spam.
--------------------------------------------------------------------------------------------------------------------

- FOR: se utiliza para iterar sobre un objeto iterable y ejecutar un bloque de código para cada elemento en la secuencia de dicho objeto que puede ser una lista.
Donde elemento es la variable que toma el valor de cada elemento en la secuencia. Iterable es un objeto iterable.
La instrucción for permite repetir una instrucción o una instrucción compuesta un número especificado de veces. 
El cuerpo de una instrucción for se ejecuta cero o más veces hasta que una condición opcional sea false.

lista = [1, 2, 3, 4]

for i (iterador que es una variable) in lista:
    print(i)

Aquí el For va recorriendo los elementos de la lista, donde I va a ir cambiando su valor segun vaya iterando(dando vueltas) y cuando termine de recorrerlos terminará la ejecución del programa.

Hay varios tipos de For.

- for i in range(1, 5): este recorre en un rango de 1 a 5. ejemplo:
for i in range(1, 5):
    print(i)
result:
1
2
3
4
recorre siempre uno menos del máximo. Si queremos que llegue a 5 habria que poner en el range(1, 5+1)

- for i in variable: este recorre los elementos de la variable (como el ejemplo de arriba) se puede leer, por cada <valor> en la <lista_de_valores>. ejemplo:
lista = [1, 2, 3, 4]
for i in lista:
    print(i)

result:
1
2
3
4
NOTA: Para ponerlos en horizontal hay una funcion que se llama end, que hay que ponerla al final del print  ejemplo end=(',')

lista = [1, 2, 3, 4]

for i in lista:
    print(i, end=',')
print(' ')

- for key in diccionario: esto va a recorrer el diccionario sobre las claves

fruta_a_color = {"manzana": "roja", "lima": "verde", "naranja": "naranja"}

for fruta in fruta_a_color:
    print(fruta, fruta_a_color[fruta])

result:

manzana roja
lima verde
naranja naranja

- for x, i, in zip(variable1, variable2): Itera sobre dos listas del mismo tamaño en un solo bucle con la función zip(). ejemplo:

A = ["a", "b", "c"]
B = ["a", "d", "e"]

for a, b in zip(A, B):
  print(a, b, a == b) 

result:
a a True
b d False
c e False


'''
