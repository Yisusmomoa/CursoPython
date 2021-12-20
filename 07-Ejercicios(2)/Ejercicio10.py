
contador=0
NumAprobados=0
NumReprobados=0

while contador<5:
    Calificacion=int(input(f"Captura la calificación del alumno {contador+1}: "))
    if Calificacion>=70:
        NumAprobados+=1
    else:
        NumReprobados+=1   
    contador+=1
else:
    print(f"Numero de aprobados: {NumAprobados}")
    print(f"Numero de reprobados: {NumReprobados}")
