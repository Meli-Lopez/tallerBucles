numeroEstudiantes = int(input("Ingrese la cantidad de estudiantes: "))

cantidad = 0
while cantidad < numeroEstudiantes:
    print("Estudiante", cantidad+1)
    nota1 = float(input("Ingrese la primera nota del estudiante: "))
    nota2 = float(input("Ingrese la segunda nota del estudiante: "))
    nota3 = float(input("Ingrese la tercera nota del estudiante: "))

    notaMasAlta = nota1
    if nota2 > notaMasAlta:
        notaMasAlta = nota2
    if nota3 > notaMasAlta:
        notaMasAlta = nota3

    notaMasBaja= nota1
    if nota2 < notaMasBaja:
        notaMasBaja = nota2
    if nota3 < notaMasBaja:
        notaMasBaja = nota3

    promedio = (nota1 + nota2 + nota3) / 3

    print("La nota mas alta es: ", notaMasAlta)
    print("la nota mas baja es: ", notaMasBaja)
    print("el promedio de las tres notas es: ", promedio)
    print("-" * 20)

    cantidad += 1