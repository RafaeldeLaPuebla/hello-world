#Creamos una clase "Termómetro" que convierte de C a F y al revés.

class Termometro():
    def __init__(self):
        self.unidadM = 'C'
        self.temperatura = 0
    
    def __conversor(self, temperatura, unidadM):
        if unidadM == 'C':
            return "{}º F".format(temperatura * 9/5 + 32)
        elif unidadM == 'F':
            return "{}º C".format((temperatura - 32) * 5/9)
        else:
            return "unidad incorrecta"
    
    def __str__(self): #Hacemos la impresión.
        return "{}º {}".format(self.__temperatura, self.__unidad)
    
    def unidadMedida(self, uniM=None):
        if uniM == None:
            return self.__unidadM
        else:
            if uniM == 'F' or uniM == 'C':
                self.__unidadM = uniM
    
    def temp(self, temperatura=None):
        if temperatura == None:
            return self.temperatura
        else:
            self.__temperatura = temperatura
    
    def mide(self, uniM=None):
        if uniM == None or uniM == self.__unidadM:
            return self.__str__()
        else:
            if uniM == 'F' or uniM == 'C':
                return self.__conversor(self.__temperatura, self.__unidadM)
            else:
                return self.__str__()
            
        
                        
                        