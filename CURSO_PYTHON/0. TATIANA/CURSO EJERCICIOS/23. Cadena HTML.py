# Escriba una función para crear una cadena HTML con etiquetas alrededor de la(s) palabra(s).
# ► Entrada:
# add_tags('i', 'Python')
# add_tags('b', 'Tutorial de Python')
# ► Salida:
# <i>Python</i>
# <b>Tutorial de Python</b>

def add_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)

print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))
