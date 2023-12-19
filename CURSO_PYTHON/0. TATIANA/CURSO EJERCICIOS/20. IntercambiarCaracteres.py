# Escriba un programa para cambiar una cadena dada a una nueva cadena, 
# en la que se hayan intercambiado el primer y el último carácter.
# ► Entrada:
# strInicial ='abcdefghijklmnopqrstuvwxyz'
# ► Salida:
# zbcdefghijklmnopqrstuvwxya

strInicial ='abcdefghijklmnopqrstuvwxyz'
firstLetter = strInicial [0]
lastLetter = strInicial [-1]
strMiddle = strInicial[:-1]
strMiddle = strMiddle[1:]
strFinal = lastLetter + strMiddle + firstLetter


# new_string = strInicial.translate({ord('a'):ord('z'), ord('z'):ord('a')})

print(strFinal)

