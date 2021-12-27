"""
POO
Clase: un molde para un objeto, con esa clase se crean más objetos de ese tipo
"""

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
        self.velocidad+=1
    def frenar(self):
        self.velocidad-=1

    def getVelocidad(self):
        return self.velocidad
    def getMaxVelocidad(self):
        return self.maxVelocidad
#Fin de la clase


#crear objetos
coche=Coche()
#print(coche)

print(coche.marca,coche.color)
print(f"Velocidad actual: {coche.velocidad}")

coche.acelerar()
coche.acelerar()
coche.acelerar()
print(f"Velocidad actual: {coche.velocidad}")

coche.frenar()
coche.frenar()
coche.frenar()
coche.frenar()
print(f"Velocidad actual: {coche.velocidad}")



