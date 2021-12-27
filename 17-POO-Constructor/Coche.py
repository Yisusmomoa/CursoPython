class Coche:
    #atributos o propiedades
    #caracteristicas del coche
    __color="rojo"
    __marca="Ferrari"
    __modelo="Aventador"
    __velocidad=0
    __maxVelocidad=300
    __caballaje=300
    __plazas=2
    __count = 0 

    __AtributoPrivado="Soy un atributo privado"

    #Constructor 1
    def __init__(self,_color="",_marca="",_modelo="",_maxVelocidad=0,_caballaje=0,_plazas=0):
        Coche.__count+=1
        self.color=_color
        self.marca=_marca
        self.modelo=_modelo
        self.maxVelocidad=_maxVelocidad
        self.caballaje=_caballaje
        self.plazas=_plazas
    #Constructor 1

    




    #Métodos, son acciones que hace el objeto (coche) (funciones)
    def acelerar(self):#self hago referencia al objeto
        if self.getVelocidad()<=self.getMaxVelocidad():
            self.velocidad+=1
    def frenar(self):
        if self.velocidad >= 1:
            self.velocidad-=1
    def showInfoCoche(self):
        cadena="***Información Coche***"
        cadena+=f"\n Modelo: {self.getModelo()}"
        cadena+=f"\n Marca: {self.getMarca()}"
        cadena+=f"\n Color: {self.getColor()}"
        cadena+=f"\n Maxima velocidad: {self.getMaxVelocidad()} "
        return cadena

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
    
    def getAtributoPrivado(self):
        return self.__AtributoPrivado
    def setAtributoPrivado(self,pAtributoPrivado):
        self.__AtributoPrivado=pAtributoPrivado

#Fin de la clase