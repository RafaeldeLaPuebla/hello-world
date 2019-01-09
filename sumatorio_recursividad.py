#Recursividad con un ejemplo de sumatorio.

def sumatorio(n):

    if n > 0:
        return n + sumatorio(n-1)
    else:
        return 0 #Cuando sea sumatorio (0), me tiene que devolver un cero, que es el neutro en la suma. Así paramos la función recursiva, dándole un valor.
        

print(sumatorio (4))