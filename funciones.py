def valorSumado(n):
    return n + 10

def whilePrint(n):
    i = 0
    while i < n:
        valorActual = i
        valorSuma = valorSumado(i)
        i += 1
        print("Valor Actual: " + str(valorActual) + " Valor Sumado: " + str(valorSuma))

entrada = int(input("Ingresa un valor: "))

whilePrint(entrada)

