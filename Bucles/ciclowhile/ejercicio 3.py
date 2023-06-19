numero = int(input("Ingrese un numero: "))

sumaImpares = 0
cantidadImpares = 0
i = 1

while i <= numero :
    sumaImpares += i
    cantidadImpares += 1
    i += 2

print("La suma de todos los numeros impares desde 1 hasta", numero, "es: ", sumaImpares)
print("En total hay", cantidadImpares, "numeros impares en la cantidad de numeros que usted digito.")
