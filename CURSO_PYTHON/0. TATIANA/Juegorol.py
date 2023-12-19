userLife = 0
userDamage = 0
goblinLife = 0
goblinDamage = 0
import random


def chooseClass():
    selectedClass = input('Elige si quieres ser Guerrero or Mago (G/M) :')
    selectedClass = selectedClass.upper()
    if "G" == selectedClass:
        print('Eres un Guerrero')
        return selectedClass
    elif "M" == selectedClass:
        print('Eres un Mago')
        return selectedClass
    else:
        print('No has introducido tu clase')
        chooseClass()

def character(): 
   name = input('Nombre: ')
   greeting = 'Saludos ' + name + '!'
   return greeting

def fight():
   question1 = input('Qué quieres hacer? Pelear o Huir (P/H)?')
   question1 = question1.upper()
    

   if "P" == question1:
        name1 = 'El goblin'
        name2 = 'Tú'
        print('Tirar un dado de 20 para ver iniciativas')
        for goblin in range(1):
           print(name1,'saca un: ',random.randint(1,20))
           for tu in range(1):
               print(name2,'sacas un: ',random.randint(1,20))
        if name1 > name2:
           print(name1, 'ataca primero')
        else:
            print(name2, 'atacas primero') 
   
   # goblinLife = 15
   # userLife = 10
   # goblinDamage = 15
   # contador = 0

   # while goblinLife > 0 or userLife > 0:
   #    contador += 1



       
        
   else:
    print('Has huido del combate')



print(character())
myClass = chooseClass()
if myClass == 'G':
   userLife = 10
   userDamage = 6
else:
   userLife = 7
   userDamage = 10

print('Daño:',userDamage,'Vida:', userLife)
print('Te has encontrado un Goblin!!!')

fight()






    




