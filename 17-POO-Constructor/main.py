from Coche import Coche


carro1=Coche("Amarillo","Porche","911",250,200,3)
carro2=Coche("Rojo","Lamborghini","Diablo",350,400,3)
carro3=Coche()

#print(f"Carro1: {carro1.getColor()}, {carro1.getMarca()}, {carro1.getMaxVelocidad()}, {carro1.getVelocidad()}")

print("\n Carro 1")
print(carro1.showInfoCoche())
# carro1.acelerar()
# carro1.acelerar()
# carro1.acelerar()
# carro1.acelerar()
# print(carro1.getVelocidad())


print("\n Carro 2")
print(carro2.showInfoCoche())

# print("****")
# print(carro1.count)
# print("\n")
# print(carro2.count)

print("\n Carro 3")
carro3.setColor("morado")
print(carro3.showInfoCoche())



#Detectar tipado
if type(carro3)==Coche:
    print("Si es de tipo coche")

print(carro3.getAtributoPrivado())

#visibilidad de los atributos y métodos

