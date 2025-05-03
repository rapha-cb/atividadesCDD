tamanho_vetores = int(input("digite o tamanho dos vetores A e B: "))

A = []
B = []
for i in range(tamanho_vetores):
    A.append(int(input("preencha o vetor A: ")))
    B.append(int(input("preencha o vetor B: ")))

Soma =[]
for j in range(tamanho_vetores):
    somar = A[j] + B[j]
    Soma.append(somar)
print(f"Vetor com a soma dos elementos dos vetores A e B: {Soma}")