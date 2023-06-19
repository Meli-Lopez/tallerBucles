numero = int(input("Ingrese un numero entero mayor a 0: "))

while numero <= 0:
    print("¡¡ERROR!!. El numero que ingrese debe de ser mayor que 0.")
    numero = int(input("Ingrese un numero entero mayor que 0: "))

divisores = []

i = 1
while i <= numero:
    if numero % i == 0:
        divisores.append(i)
    i += 1
print("Los divisores del numero", numero, "son:", divisores)