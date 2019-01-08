from functools import reduce

def doble(x): #Esta función es lo mismo que el map.
    return x*x

lista = [1, 2, -1, 8, 9]

listaDobles =map(lambda x: x*2, lista)
listaDobles1 = map(doble, lista)

def esPar(x): #Esta función es lo mismo que el filter.
    return x%2 == 0

listaPares = filter(lambda x: x%2 == 0, lista)
#Cuando los valores de la lista cumplan la condición, te va a devolver el valor. Si no lo cumple, no te lo devuelve
listaPares1 = filter(esPar, lista)

sumatorio = reduce (lambda x, y:x+y, lista) #Me reduce todo a un valor, a la operación según la función.

suma100 = reduce (lambda x,y: x+y, range(101))

print(list(listaPares))
print(list(listaPares1))

print(list(listaDobles))
print(list(listaDobles1))

print(list (sumatorio))
print(list (suma100))

