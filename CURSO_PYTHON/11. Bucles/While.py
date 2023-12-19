i = 0

while i <= 10:
   
    print('estoy iterando, voy por el salto: {}'.format(i))
    i += 1 # esto es muy importante

# el siguiente iria de mayor a menor:
j = 10

while j > 0:
    j -= 1
    print('estoy iterando, voy por el salto: {}'.format(j))

'''
NOTA: SI EL ITERADOR LO COLOCAMOS ANTES DEL PRINT (i +=1), VA A EMPEZAR DESDE EL NUMERO MAS 1, PERO SI LO COLOCAMOS DESPUES DEL PRINT
EMPEZARÁ DESDE EL NÚMERO QUE SEA IGUAL A LA VARIABLE, ES DECIR:
i = 0

while i < 10:
    i += 1
    print('estoy iterando, voy por el salto: {}'.format(i))

RESULT:
estoy iterando, voy por el salto: 1
estoy iterando, voy por el salto: 2
estoy iterando, voy por el salto: 3
estoy iterando, voy por el salto: 4
estoy iterando, voy por el salto: 5
estoy iterando, voy por el salto: 6
estoy iterando, voy por el salto: 7
estoy iterando, voy por el salto: 8
estoy iterando, voy por el salto: 9

PERO SI LO PONEMOS AL FINAL DEL PRINT EMPEZARÁ DESDE 0:
i = 0

while i < 10:
    print('estoy iterando, voy por el salto: {}'.format(i))
    i += 1

RESULT:
estoy iterando, voy por el salto: 0
estoy iterando, voy por el salto: 1
estoy iterando, voy por el salto: 2
estoy iterando, voy por el salto: 3
estoy iterando, voy por el salto: 4
estoy iterando, voy por el salto: 5
estoy iterando, voy por el salto: 6
estoy iterando, voy por el salto: 7
estoy iterando, voy por el salto: 8
estoy iterando, voy por el salto: 9

'''