numeroTemperaturas = int(input("Ingrese la cantidad de temperaturas que hay: "))

temperaturas = []
cantidad = 0
sumaTemperaturas = 0

while cantidad < numeroTemperaturas:
    temperatura = float(input("Ingrese la temperatura {}: ".format(cantidad + 1)))
    temperaturas.append(temperatura)
    sumaTemperaturas += temperatura
    cantidad += 1

temperaturaMasAlta = max(temperaturas)
temperaturaMasBaja = min(temperaturas)
temperaturaPromedio = sumaTemperaturas / numeroTemperaturas
print("La temperatura mas alta es:", temperaturaMasAlta)
print("La temperatura mas baja es:", temperaturaMasBaja)
print("La temperatura promedio es:", temperaturaPromedio)
