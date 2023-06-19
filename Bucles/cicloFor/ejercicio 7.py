tablas = int(input("Ingrese el número de la tabla de multiplicacion que quiere ver: "))

print("Tabla de multiplicar del numero ", tablas)

for i in range(11):
    resultado = tablas * i
    print(tablas, "x", i, "=", resultado)
