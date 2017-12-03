#las excepciones se generan cuando ocurre un error en la ejecucion del programa
print("Bienvenido")
n=1
try:
    print(n/5)
except (TypeError):
    print("error en tipo de dato")
except NameError:
    print("variable no existe")
except ZeroDivisionError:
    print("No se puede dividir entre 0")

else:
    print("No hubo error")