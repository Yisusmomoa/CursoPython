import clases

persona=clases.Persona() 

persona.setNombre("Brandon")
persona.setApellidos("Loera silva")
persona.setEdad(24)
persona.setAltura("175")


#print(f"La persona: {persona.getNombre()} {persona.getApellidos()}, su edad es: {persona.getEdad()} y su altura es: {persona.getAltura()} cm")


programador=clases.Programador("Brando", "Silva",24,"175")

programador.aprenderLenguaje("Html")
programador.aprenderLenguaje("Css")
programador.aprenderLenguaje("JS")
programador.aprenderLenguaje("Python")
programador.aprenderLenguaje("C++")

print(programador.getLenguajes())

for i in range(10):
    programador.tomaCafe()

print(f"Numero de tasas tomadas: {programador.getTasasCafe()}")







