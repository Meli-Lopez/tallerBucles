numero = int(input("Ingrese un numero: "))
sum = 0
impares = 0

for i in range(1, numero + 1, 2):
    sum += i
    impares += 1

print("La suma de los numeros impares es: ", sum)
print("La cantidad de números impares que hay es:", impares)
