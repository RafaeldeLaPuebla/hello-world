class Perro(): #Objeto. Vamos a crear nuestro primer objeto.
    def __init__(self, nombre, edad, peso): # Implementamos los atributos de mi objeto.
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def ladrar(self): #Implementamos el método ladrar.
        if self.peso >= 8:
            print("GUAU, GUAU")
        else:
            print("guau, guau")
            
    def __str__(self):
        return "Soy el perro {}".format(self.nombre, self.edad, self.peso)
    
class PerroAsistencia(Perro): #Es una subclase de Perro. Hereda de Perro.
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.trabajando =False #No hace faltar ponerlo en el paréntesis. Los ponemos por claridad.
    
    def __str__(self):
        return "Perro de asistencia de {}".format(self.amo)
    
    def pasear(self):
        print("{} ayudo a mi dueño, {} a pasear".format(self.nombre, self.amo))
        
#Vamos a sobreescribir el método ladrar:
        
    def ladrar(self):
        if self.trabajando:
            print("shhhh, no puedo ladrar")
        else:
            Perro.ladrar(self) #Invoco el método padre.
    
    def trabajando(self, valor=None): #Creado método getter que es trabajando() y trabajando (True) es método setter.
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor
            
        
        
    
    
    