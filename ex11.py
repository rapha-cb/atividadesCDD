lista = []
for i in range(5):
    nomes = input("Digite um nome: ")
    lista.append(nomes)
print(f"lista de nomes: {lista}")
print("lista inversa(1 nome por linha): ")
for j in range(len(lista)-1,-1,-1):
    print(lista[j])