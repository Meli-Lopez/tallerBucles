numero = int(input("Ingrese un número: "))
suma = 0

for i in range(0, numero + 1, 2):
    suma += i

print("La suma de los números pares hasta el numero", numero, "es: ",suma)
