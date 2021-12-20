"""

Ejercicio10 pedir la nota de 15 alumnos y sacar en pantalla cuantos han aprobado y cuantos han suspendido

"""
contador=0
NumAprobados=0
NumReprobados=0

while contador<5:
    calificacion=int(input("Captura la calificación del alumno "+str(contador+1)+" "))
    if calificacion>=70:
        NumAprobados+=1
    else:
        NumReprobados+=1
    contador+=1
print(f"El numero de aprobados es: {NumAprobados}, y el numero de reprobados es: {NumReprobados}")

