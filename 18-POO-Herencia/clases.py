#la herencia es la forma en la que una
#clase padre pueda compartir atributos y metodos con otras clases
#y que diferentes clases hereden de otra


class Persona:
    """
    nombre,
    apellidos,
    edad,
    altura
    """
#metodos
    def hablar():
        return "estoy hablando"
    def caminar():
        return "estoy caminando"
    def dormir():
        return "estoy durmieno"

#get y set
    def getNombre(self):
        return self.nombre
    def setNombre(self,pnombre):
        self.nombre=pnombre

    def getApellidos(self):
        return self.apellidos
    def setApellidos(self,papellidos):
        self.apellidos=papellidos

    def getAltura(self):
        return self.altura
    def setAltura(self, paltura):
        self.altura=paltura

    def getEdad(self):
        return self.edad
    def setEdad(self,pedad):
        self.edad=pedad

#fin clase persona


class Programador(Persona):
    __tasasCafe=0
    __experiencia=0
    __lenguajes=[]
    def __init__(self,pnombre="",papellidos="",pedad=0,paltura="") :
        self.nombre=pnombre
        self.apellidos=papellidos
        self.edad=pedad
        self.altura=paltura
        self.__experiencia=0

    def getLenguajes(self):
        return self.__lenguajes
    def aprenderLenguaje(self, _lenguaje):
        self.__lenguajes.append(_lenguaje)

    def setExperiencia(self, pexperiencia):
        self.__experiencia=pexperiencia
    def getExperiencia(self):
        return self.__experiencia

    def getTasasCafe(self):
        return self.__tasasCafe
    def setTasasCafe(self,pTasasCafe):
        self.__tasasCafe=pTasasCafe
    
    def tomaCafe(self):
        self.__tasasCafe+=1

#fin clase Programador


