# una cadena es tambien un objeto llamado secuencia
s = "Hola mundo"

print(len(s)) #obtiene tamaño de la cadena

print(s.count("o"))#cuenta cuantas veces encuentro una letra


print(s.count("o",0,3))# busca la o en Hola

print(s.count("o",5))

#cnvertir cadena a mayus o minus

print(s.lower())
print(s.upper())

#reemplazar valor
print(s.replace("o","x"))
print(s.replace("o","x",1))#reemplaza solo la primera
#split.Regresar una lista, genera una subcadena despues de dividir la cadena
print(s.split("a"))
print(s.split("o",1))
#find.Buscar una cadena o un caracter dentro de un objeto cadena
print(s.find("a"))#regresa la ubicacion de la primer ocurrencia
print(s.rfind("o"))# de atras para adelante

t = ("H","o","l","a")
s = ","
print(s.join(t))# junta los caracteres separados por ;
print (type(s.join(t)))