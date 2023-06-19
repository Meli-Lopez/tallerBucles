numeroNotas = 4

notas = []

for i in range(numeroNotas):
    nota = float(input("Ingrese la nota {}:".format(i + 1)))
    notas.append(nota)

notaMasAlta = max(notas)
notaMasBaja = min(notas)
promedioNotas = sum(notas) / numeroNotas

print("La nota mas alta del estudiante es: ", notaMasAlta)
print("La nota mas baja del estudiante es: ", notaMasBaja)
print("El promedio de las notas del estudiante es: ", promedioNotas)
