lista = []

for i in range(10):
    n= int(input("digite um número: "))
    lista.append(n)

encontrar_numero = int(input("Digite um número para saber quantas vezes ele aparece: "))
contador = 0
for j in range(len(lista)):
    if encontrar_numero == lista[j]:
        contador += 1

print(f"O número {encontrar_numero} foi encontrado {contador} vezes! ")

