def cadastro(cadastros):
    while True:
        status = "em funcionamento"
        codigo = input("Código: ")
        nome = input("Nome: ")
        cadastros[codigo] = {"nome": nome, "status": status}
        print("Cadastro realizado!",codigo, ":", [cadastros[codigo]["nome"], cadastros[codigo]["status"]])
        flag = input("Deseja realizar novo cadastro (s/n)? ")
        if flag == "n":
            break

def consulta(cadastros):
    busca = input("Busca: ")
    encontrou = False

    for codigo, info in cadastros.items():
        if busca in [codigo, info["nome"], info["status"]]:
            print(codigo, ":", [info["nome"], info["status"]])
            encontrou = True

    if not encontrou:
        print("Nenhum resultado encontrado.")


def main():
    cadastros = {}
    print("Menu")
    escolha = input("1- Cadastro\n2- Consulta\n3- Reparo\n4- Sair\nDigite uma opção: ")
    while(escolha!="4"):

        if(escolha=="1"):
            cadastro(cadastros)

        elif(escolha=="2"):
            consulta(cadastros)
            #consulta()

        elif(escolha=="3"):
            print("Reparo")
            #reparo()

        else:
            print("Opção inválida")

        escolha = input("1- Cadastro\n2- Consulta\n3- Reparo\n4- Sair\nDigite uma opção: ")

if __name__ == "__main__":
    main()

