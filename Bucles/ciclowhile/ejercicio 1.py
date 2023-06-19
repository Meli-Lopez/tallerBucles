num = int(input("Ingrese un numero: "))

if num >= 10:
    resultado = 1
    numero = 1
    while numero <= 10:
        resultado *= numero
        numero += 1
    print("la multiplicación de los 10 primeros numeros que usted digito es: ", resultado)
else:
    resultado = 0
    nume = 1
    while nume <= num:
        resultado += nume
        nume += 1
    print("El resultado de la suma de los numeros del 1 al", num, "es:", resultado)