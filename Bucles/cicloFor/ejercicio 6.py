num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 >= num2:
    print("El primer número debe ser menor que el segundo numero.")
else:
    for i in range(num1, num2 + 1):
        print(i)