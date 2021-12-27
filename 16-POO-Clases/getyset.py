class Coche:
    #atributos o propiedades
    #caracteristicas del coche
    color="rojo"
    marca="Ferrari"
    modelo="Aventador"
    velocidad=0
    maxVelocidad=300
    caballaje=300
    plazas=2

    #Métodos, son acciones que hace el objeto (coche) (funciones)
    def acelerar(self):#self hago referencia al objeto
        if self.getVelocidad()<=self.getMaxVelocidad():
            self.velocidad+=1
    def frenar(self):
        if self.velocidad >= 1:
            self.velocidad-=1
    
    #get y set
    def setColor(self, pcolor):
        self.color=pcolor
    def getColor(self):
        return self.color

    def setModelo(self, pmodelo):
        self.modelo=pmodelo
    def getModelo(self):
        return self.modelo
    
    def setMarca(self, pmarca):
        self.marca=pmarca
    def getMarca(self):
        return self.marca
    
    def setVelocidad(self,pvelocidad):
        self.velocidad=pvelocidad
    def getVelocidad(self):
        return self.velocidad

    def getMaxVelocidad(self):
        return self.maxVelocidad
    def setMaxVelocidad(self,pmaxVelocidad):
        self.maxVelocidad=pmaxVelocidad
    
    def getCaballaje(self):
        return self.caballaje
    def setCaballaje(self,pcaballaje):
        self.caballaje=pcaballaje
    
    def getPlazas(self):
        return self.plazas
    def setPlazas(self, pplazas):
        self.plazas=pplazas

#Fin de la clase

coche1=Coche()
coche2=Coche()
coche3=Coche()
coche3.setColor("Amarillo")
coche2.setColor("Blanco")
# print(f"Coche 1 color : {coche1.getColor()}")
# print(f"Coche 2 color : {coche2.getColor()}")
# print(f"Coche 3 color : {coche3.getColor()}")
# print("\n")
# print(f"Velocidad coche 1 : {coche1.getVelocidad()}")
# coche1.acelerar()
# coche1.acelerar()
# coche1.acelerar()
# coche1.acelerar()
# print(f"Velocidad coche 1 : {coche1.getVelocidad()}")

# print("\n")
# print(f"Velocidad coche 2 : {coche2.getVelocidad()}")
# coche2.acelerar()
# coche2.acelerar()
# coche2.frenar()
# coche2.frenar()
# print(f"Velocidad coche 2 : {coche2.getVelocidad()}")

print("\n")

print(f"Velocidad coche 3 : {coche3.getVelocidad()}")

i=0
while i<coche3.getMaxVelocidad():
    coche3.acelerar()
    print(f"Velocidad coche 3 : {coche3.getVelocidad()}")
    i+=1
print(f"Velocidad coche 3 : {coche3.getVelocidad()}")







