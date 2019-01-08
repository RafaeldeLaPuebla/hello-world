
def maxi(*l): #coge todos los parámetros que meta y me los procesas como un array.
    if len(l) == 0: #gestiono que no sean cero los parámetros.
        return 0
    
    m = l[0]
    
    for ix in range(1, len(l)):
        if l[ix] > m:
            m = l[ix]
    
    return m

def mini(*l):
    if len(l) == 0: #gestiono que no sean cero los parámetros.
        return 0
    
    m = l[0]
    
    for ix in range(1, len(l)):
        if l[ix] < m:
            m = l[xi]
    
    return m

def media(*l):
    if len(l) == 0:
        return 0
    
    suma = 0
    for valor in l:
        suma +=valor
    return suma / len(l)

funciones = {
    'max': maxi,
    'min': mini,
    'med': media
    }

def returnF(nombre): #Es una función que me devuelve otra función
    nombre = nombre.lower()
    if nombre in funciones.keys():
        return funciones[nombre]
    
    return None




    
