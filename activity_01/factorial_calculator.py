import math
numero = int(input("Digite um número entre 1 e 10: "))
fatorial = math.factorial(numero)

if 0 <= numero <= 10:
    print(f"O fatorial de {numero} é {fatorial}")
else:
    print(f"Número inválido!")