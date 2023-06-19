numero = int(input("ingrese la cantidad de numeros que quiere sumar (teniendo en cuenta que solo suma los numeros pares): "))

sumaPares = 0
i = 0
while i <= numero:
    sumaPares += i
    i += 2

print("La suma de los numeros pares desde el 0 hasta el", numero, "es: ", sumaPares)
