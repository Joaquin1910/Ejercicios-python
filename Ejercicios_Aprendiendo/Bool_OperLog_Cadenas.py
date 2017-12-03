#comillas simples
cads = 'Texto entre comillas simples'
cadd = "Texto entre comillas dobles"
print (type(cads)) #Nos arroja que la variable cads es de tipo string
cadslinea = 'Texto entre \ncomillas simples' #salto de linea
print(cadslinea)
caddtab = "Texto entre \n \t comillas dobles" #tabulacion
print(caddtab)
"""comentarios
con
varias
lineas"""
text_comillas = """Texto 1
2
3
4"""
print(text_comillas)

# Repeticion y concatenacion

cad = "cadena 1 "* 3 #repetir cadena 3 veces
print(cad)
cad2 = "cadena 2"
print(cad+cad2)

#booleanos

bT = True
bF = False

#operadores logicos

bAnda = True and False
bOr = True or False
bNot = not True
print(bAnda)
print(bOr)
print(bNot)



