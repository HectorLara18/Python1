from asyncio.windows_events import NULL


menu = """
Bienvenidos al convrsor de monedas 🪙

1 - Peso colombiano
2 - Peso argentino
3 - Peso mexicano

Elige una opcion: 
"""
strDolares = NULL

##funciones
def ConvertirMoneda(valorRef):
    valorLocal = NULL
    pesos = input("Ingrese el valor en pesos:" )
    pesosFloat = float(pesos)
    valor_dolar = valorRef
    dolares = pesosFloat/valor_dolar
    dolares = round(dolares,1)
    valorLocal = str(dolares)
    return valorLocal

opcion = input(menu)

if opcion == "1":
    strDolares = ConvertirMoneda(60)
elif opcion == "2":
    strDolares = ConvertirMoneda(100)
else:
    strDolares = ConvertirMoneda(20)



print("Tienes $" + strDolares + " dolares")