lista = []
for i in range(10):
    n = int(input("digite um valor: "))
    lista.append(n)
pares = []
maior = lista[0]
menor = lista[0]
soma = 0
maior_media = 0
for j in lista:
    if j % 2 == 0:
        pares.append(j)
    if j > maior:
        maior = j

    if j < menor:
        menor = j

    soma = (soma + j)
media = soma/10
for j in lista:
    if j > media:
        maior_media += 1
print(f"números pares: {pares}")
print(f"maior e menor número: {maior}  {menor}")
print(f"quantidade de números maiores que a média: {maior_media}")



