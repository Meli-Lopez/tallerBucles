numeroTemperaturas = int(input("Ingrese el numero de temperaturas: "))

if numeroTemperaturas <= 0:
    print("¡ERROR! ingrese al menos una temperatura.")
    numeroTemperaturas = int(input("Ingrese la cantidad de temperaturas: "))

temperaturas = []
sumaTemperaturas = 0

for i in range(numeroTemperaturas):
    temperatura = float(input("Ingrese la temperatura{}: ".format(i + 1)))
    temperaturas.append(temperatura)
    sumaTemperaturas += temperatura

temperaturaMasAlta = max(temperaturas)
temperaturaMasBaja = min(temperaturas)
temperaturaPromedio = sumaTemperaturas / numeroTemperaturas

print("La temperatura mas alta de todas es: ", temperaturaMasAlta)
print("La temperatura mas baja de todas es: ", temperaturaMasBaja)
print("La temperatura promedio de todas es:", temperaturaPromedio)
