numero = int(input("Ingrese un número entero mayor a cero: "))

if numero <= 0:
    print("¡EROR! El número debe ser mayor a cero.")

    numero = int(input("Ingrese otro número entero que sea mayor a cero: "))

print("Los divisores del numero", numero, "son: ")

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
