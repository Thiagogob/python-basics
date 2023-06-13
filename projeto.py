def main():
    print("Menu")
    escolha = input("1- Cadastro\n2- Consulta\n3- Reparo\n4- Sair\nDigite uma opção: ")
    while(escolha!="4"):

        if(escolha=="1"):
            print("Cadastro")
            #cadastro()

        elif(escolha=="2"):
            print("Consulta")
            #consulta()

        elif(escolha=="3"):
            print("Reparo")
            #reparo()

        else:
            print("Opção inválida")

        escolha = input("1- Cadastro\n2- Consulta\n3- Reparo\n4- Sair\nDigite uma opção: ")

if __name__ == "__main__":
    main()