#Recursividad con un ejemplo de sumatorio.

def factorial(n):

    if n > 0:
        return n * factorial(n-1)
    else:
        return 1 #Cuando sea factorial (0), me tiene que devolver un uno, que es el neutro en la multiplicación. Así paramos la función recursiva, dándole un valor.
        
print(factorial (4))