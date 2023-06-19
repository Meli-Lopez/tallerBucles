cantidadNotas = int(input("Ingrese la cantidad de notas del estudiante: "))

notas = []
i = 0
suma = 0

while i < cantidadNotas:
    nota = float(input("Ingrese la nota {}: ".format(i + 1)))
    notas.append(nota)
    suma += nota
    i += 1
promedio = suma / cantidadNotas
print("El promedio de las notas del estudiante es: ", promedio)
