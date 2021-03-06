#Funciones de primer nivel: admite funciones como parámetros de entrada.

def normal(x):
    return x

def cuadrado(x):
    return x * x

def sumaTodos(limitTo, f): #f va a contener la referencia a la función que quiero realizar
    resultado = 0
    for i in range(limitTo+1):
        resultado += f(i)
    return resultado

print(sumaTodos(100, normal)) #normal=invoco el nombre de la función que quiero.
print(sumaTodos(3, cuadrado))