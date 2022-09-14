##argumentos
##i = 0

##Funciones

def FizzBuzz(arg):
    res = "Null"
    if arg % 3 == 0 and arg % 5 != 0:
        res = "Fizz"
    elif arg % 3 != 0 and arg % 5 == 0:
        res = "Buzz"
    elif arg % 3 == 0 and arg % 5 == 0:
        res = "FizzBuzz"
    else:
        res = str(arg)
    return res

def valorIncremental(valor):
    i = 0
    while i < valor:
        valorActual = i
        i += 1
        resultado = FizzBuzz(i)
        print("Valor Actual: " + str(valorActual) + " Resultado: " + str(resultado))

def valorIncremetalFor(valor):
    for x in range(valor):
        valorActual = str(x)
        resultado = str(FizzBuzz(x))
        print("Valor Actual: " + str(valorActual) + " Resultado: " + str(resultado))



entrada = int(input("Ingrese valor: "))

valorIncremetalFor(entrada)