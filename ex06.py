lista = []
for i in range(1,6):
    num= int(input("Digite um número: "))
    lista.append(num)
for j in range(len(lista)-1, -1, -1):
    print(lista[j], end= " ")