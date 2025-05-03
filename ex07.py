nomes = []
senhas = []


for i in range(5):
    nome_login = input("Digite o nome de usuário: ")
    nomes.append(nome_login)
    senha_login =(input("Digite a senha do usuário: "))
    senhas.append(senha_login)



for j in range(i+1):
    print(nomes[j], senhas[j], j)