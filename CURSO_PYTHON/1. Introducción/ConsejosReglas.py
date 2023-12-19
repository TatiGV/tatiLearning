
#REGLAS:
#Una variable no puede tener un nombre de palabra reservada, ej. print = 200. si utilizamos esta palabra da un error.
#palabras reservadas:
#para verlas hay que importarlas (import keyword)

import keyword

print(keyword.kwlist)

#No pueden iniciar con numero, ej. 30años  = 30.
#no pueden llevar caracteres especiales ej. , @ - ell@s = 'laura'
#no pueden llevar espacios ej. edad jovenes = 30
#CONSEJOS:
#Colocar variables descriptivas, ponerles nombres a lo que hace referencia ej. edad = 30
#Si quieres poner una variable con espacios en vez de eso puedes ponerlo con camel case o snake ej. edadJovenes o edad_jovenes