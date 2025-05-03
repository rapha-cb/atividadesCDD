nomes = []
senhas = []


for i in range(2):
    nome_login = input("Digite o nome de usuário: ")
    nomes.append(nome_login)
    senha_login =(input("Digite a senha do usuário: "))
    senhas.append(senha_login)

login = input("digite sua senha: ")
login_efetuado = False

for j in range(len(senhas)):
    if login == senhas[j]:
        pos = j
        print(f"{nomes[pos]}, login bem sucedido!")
        login_efetuado= True
        break

if not login_efetuado:
    print("senha inválida ou usuario não cadastrado")




