numeroDeNotas = int(input("Ingrese el numero de notas del estudiante: "))

calificacion = []
for i in range(numeroDeNotas):
    nota = float(input("Ingrese la nota {}: ".format(i + 1)))
    calificacion.append(nota)

promedio = sum(calificacion) / numeroDeNotas
print("El promedio de todas las notas del estudiante es: ", promedio)