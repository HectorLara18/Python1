pesos = input("Ingrese el valor en pesos:" )
pesosFloat = float(pesos)
valor_dolar = 20
dolares = pesosFloat/valor_dolar
dolares = round(dolares,1)
strDolares = str(dolares)
print("Tienes $" + strDolares + " dolares")