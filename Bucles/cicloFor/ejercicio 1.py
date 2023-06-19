numero = int(input("Ingrese la cantidad de números que quiere sumar: "))

if numero <= 0:
    print("El número debe ser positivo.")
else:
    suma = 0
    for i in range(1, numero + 1):
        suma += i

    print("La suma de los primeros números es:", suma)