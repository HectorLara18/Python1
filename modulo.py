def Fizz(valor):
    if valor % 3 == 0:
        print("Fizz")
    else:
        print(valor)

entrada = int(input("ingrese numero: "))
Fizz(entrada)