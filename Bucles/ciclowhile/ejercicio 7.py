numero = int(input("Ingrese un numero entero. Con el 0 puede finalizar: "))
suma = 0

while numero != 0:
    suma += numero
    numero = int(input("Ingrese un numero entero. Con el 0 puede finalizar: "))

print("La suma de los numeros ingresados es: ", suma)