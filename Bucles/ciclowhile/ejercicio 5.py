totalFacturas = 0
montoFactura = float(input("Ingrese el monto de la factura (con el 0 finaliza): "))

while montoFactura != 0:
    totalFacturas += montoFactura
    montoFactura = float(input("Ingrese el monto de la factura (con el 0 finaliza): "))

if totalFacturas> 1000:
    descuento = totalFacturas * 0.1
    totalPagar = totalFacturas - descuento
else:
    descuento = 0
    totalPagar = totalFacturas

print("Total de las facturas: ", totalFacturas)
print("se le realiza un descuento del 10% que equivale a: ", descuento)
print("Total a pagar: ", totalPagar)
