#Ejemplo3 tablas de multiplicar con funciones

def muestraTablaMultiplicar(_numero):
    print(f"La tabla de multiplicación del {_numero}")
    for contador in range(1,11):
        print(f"{_numero} x {contador} = {_numero*contador}")

# muestraTablaMultiplicar(2)

for contador in range(1,11):
    muestraTablaMultiplicar(contador)
