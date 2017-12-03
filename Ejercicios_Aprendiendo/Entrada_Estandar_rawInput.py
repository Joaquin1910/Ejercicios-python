##x = input()


try:
    x = input("Introduce un numero")
    x = int(x)
except:
    print("Eso no es un numero")
else:
    print(x)