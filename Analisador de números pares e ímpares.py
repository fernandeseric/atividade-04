quantidade = int(input("Quantos números você vai digitar: "))

pares = 0
impares = 0

for i in range(quantidade):
    numero = int(input(f"Digite o número {i+1}: "))

    if numero % 2 == 0:
        pares = pares + 1
        print(numero, "é par")
    else:
        impares = impares + 1
        print(numero, "é ímpar")

print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)












