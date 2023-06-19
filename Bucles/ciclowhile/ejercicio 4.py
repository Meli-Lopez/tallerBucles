numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

while numero1 >= numero2:
    print("¡ERROR! el primer numero debe ser menor que el segundo numero.")
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))

print("los numeros que hay desde el ", numero1, "hasta el", numero2, "son:")
i = numero1
while i <= numero2:
    print(i)
    i += 1
