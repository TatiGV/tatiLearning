# Pedir al usuario el dia de la semana
# Según el dia de la semana que ponga decir los animes que hay o no.
# lunes = Masamune-kun no revenge, Lvl1 Maou to one room Yuusha
# Martes = No hay
# Miercoles =Niehime to kemono no ou, Watashi no shiwase na kekkon
# Jueves = Jujutsu Kaisen, Hataraku Maou-Sama!, Lst Tame, Ruroni Kenshing
# Viernes = Kanojo Okarishimasu, Sugar apple Fairy Tail
# Sabado = Bleach, Horimiya, Jidou hanbaiki ni Umarekawatta ore wa meikyuu wo samayou
# Domingo = No hay

dia = input('Introduce el dia de la semana: (Lunes / Martes / Miercoles / Jueves / Viernes / Sabado / Domingo): ')
dia = dia.capitalize()
animes_semana = {
    'Lunes' : ['Masamune-kun no revenge', 'Lvl1 Maou to one room Yuusha'], 
    'Martes' : ['No hay anime'], 
    'Miercoles' : ['Niehime to kemono no ou' , 'Watashi no shiwase na kekkon'], 
    'Jueves' : ['Jujutsu Kaisen' , 'Hataraku Maou-Sama!', 'Last Tame' , 'Ruroni Kenshing'],
     'Viernes' : ['Kanojo Okarishimasu' , 'Sugar apple Fairy Tail'], 
     'Sabado' : ['Bleach', 'Horimiya', 'Jidou hanbaiki ni Umarekawatta ore wa meikyuu wo samayou'],
     'Domingo' : 'No hay anime'}
animes = animes_semana[dia]

if dia == 'Lunes' or dia == 'Martes' or dia == 'Miercoles' or dia == 'Jueves' or dia == 'Viernes' or dia == 'Sabado' or dia == 'Domingo':
    
    for anime in animes:
        print(anime)

else:
    print('no existe el dia')




    