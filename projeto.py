##############################################    FUNÇÃO DE CADASTRO     ######################################################

def cadastro(cadastros):
    while True:
        status = "em funcionamento"
        codigo = input("Código: ")
        nome = input("Nome: ")
        nome = nome.lower()
        cadastros[codigo] = {"nome": nome, "status": status}
        print("Cadastro realizado!",codigo, ":", [cadastros[codigo]["nome"], cadastros[codigo]["status"]])
        flag = input("Deseja realizar novo cadastro (s/n)? ")
        if flag == "n" or flag == "N":
            break


###########################################    FUNÇÃO DE CONSULTA     ####################################################

def consulta(cadastros, filename):
    busca = input("Busca: ")
    busca = busca.lower()
    encontrou = False

    linha_escrita = []

    for codigo, info in cadastros.items():
        if busca in [codigo, info["nome"], info["status"]]:
            print(codigo, ":", [info["nome"], info["status"]])
            linha_escrita.append(f"{codigo} : [{info['nome']} , {info['status']}]\n")
            encontrou = True

    if not encontrou:
        print("Nenhum resultado encontrado.\n")
        linha_escrita.append("Nenhum resultado encontrado.\n")
    
    with open(filename, "a") as file:
        file.write("".join(linha_escrita))

#####################################    FUNÇÃO DE REPARO     ###################################################

def reparo(cadastros, filename):
    busca = input("Busca: ")
    busca = busca.lower()
    encontrou = False

    linha_escrita = []

    for codigo, info in cadastros.items():
        if busca in [codigo, info["nome"], info["status"]]:
            if info["status"]=="em funcionamento":
                print("Deseja solicitar reparo para o item ",codigo, ":", [info["nome"], info["status"]], " (s/n)? ", end="")
                reparo = input()
                if reparo=="s" or reparo =="S":
                    info["status"]="em reparo"
                    print("Solicitação concluída para o item: ", codigo, ":", [info["nome"], info["status"]])
                    linha_escrita.append(f"Solicitação concluída para o item: {codigo} : [{info['nome']} , {info['status']}]\n")
                if reparo=="n" or reparo=="N":
                    break
            else:
                print("Item: ", codigo, ":", [info["nome"], info["status"]], ", já está em reparo.")
                linha_escrita.append(f"Item: {codigo} : [{info['nome']} , {info['status']}] já está em reparo.\n")
            encontrou = True

    if not encontrou:
        print("Nenhum resultado encontrado.\n")
        linha_escrita.append("Nenhum resultado encontrado.\n")
    
    with open(filename, "a") as file:
        file.write("".join(linha_escrita))


#######################################    MAIN     #########################################################

def main():
    cadastros = {}
    filename = "resultados.txt"
    
    escolha = input("Menu:\n1- Cadastro\n2- Consulta\n3- Reparo\n4- Sair\nDigite uma opção: ")
    while(escolha!="4"):

        if(escolha=="1"):
            cadastro(cadastros)

        elif(escolha=="2"):
            consulta(cadastros, filename)

        elif(escolha=="3"):
            reparo(cadastros, filename)

        else:
            print("Opção inválida!")

        escolha = input("1- Cadastro\n2- Consulta\n3- Reparo\n4- Sair\nDigite uma opção: ")

#####################################################################################################################

if __name__ == "__main__":
    main()

