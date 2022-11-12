AGENDA = {}

def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print(">>>>>Agenda vazia")

def buscar_contato(contato):
    try:
        print("Nome:", contato)
        print("telefone:", AGENDA[contato]['telefone'])
        print("Email:", AGENDA[contato]['email'])
        print("Endereço:", AGENDA[contato]["endereço"])
        print("--------------------------------------------")
    except KeyError:
        print(">>>>>contato inexistente")
    except Exception as error:
        print(">>>> Um erro inesperado ocorreu")
        print(error)

def ler_detalhes_contato():
    telefone = input("Digite o nome do telefone: ")
    email = input("Digite o nome do email: ")
    endereço = input("Digite o nome do  endereço: ")
    return telefone, email, endereço

def incluir_editar_contato(contato, telefone, email, endereço): 

    AGENDA[contato] = {
        "telefone": telefone,
        "email": email,
        "endereço": endereço, }
    salvar()
    print("--------------------------------------------")
    print(">>> Contato {} adicionado/editado com sucesso".format(contato))
  
def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print("--------------------------------------------")
        print(">>>> contato {} excluido com sucesso".format(contato))
    except KeyError:
        print(">>>> contato inexistente")
    except Exception as error:
        print(">>>> Um erro inesperado ocorreu")
        print(error)

def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "w") as arquivo:
            for contato in AGENDA:
                telefone = AGENDA [contato]['telefone']
                email = AGENDA [contato]['email']
                endereço = AGENDA [contato]['endereço']
                arquivo.write("{};{};{};{}\n".format(contato, telefone, email, endereço))

        print(">>> Agenda exportada com sucesso")
    except Exception as error:
        print(">>>>> algum erro ao exportar contatos")
        print(error)

def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(",")

                nome = detalhes [0]
                telefone = detalhes [1]
                email = detalhes [2]
                endereço = detalhes [3]
               
                incluir_editar_contato(nome, telefone, email, endereço)

    except FileNotFoundError:
        print(">>>> arquivo não encontrado")
    except Exception as error:
        print(">>>> algum erro inesperado ocorreu")
        print(error)

def salvar():
    exportar_contatos("database.CSV")

def carregar():
    try:
        with open("database", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(",")
                
                nome = detalhes [0]
                telefone = detalhes [1]
                email = detalhes [2]
                endereço = detalhes [3]

                AGENDA[nome] = {
                "telefone": telefone,
                "email": email,
                "endereço": endereço, }



        print(">>>>>>>>Database carregado com sucesso")
        print(">>>>> {} contatos carregados".format(len(AGENDA)))
        #length = tamanho
    except FileNotFoundError:
        print(">>>> arquivo não encontrado")
    except Exception as error:
        print(">>> algum erro inesperado ocorreu")
        print(error)

def imprimir_menu():
    print("--------------------------------------------")
    print("1 - Mostrar todos os contatos da agenda")
    print("2 - buscar contato")
    print("3 - incluir contato")
    print("4 - editar contato")
    print("5 - excluir contato")
    print("6 - exportar contatos para CSV ")
    print("7 - importar contato CSV")
    print("0 - fechar agenda")
    print("--------------------------------------------")

#INICIO DO PROGRAMA

carregar()
while True:
    imprimir_menu()

    opção = input("Escolha uma opção: ")
    if opção == "1":
        mostrar_contatos()

    elif opção == "2":
        contato = input("Digite o nome do contato: ")
        buscar_contato(contato)

    elif opção == "3":
        contato = input("Digite o nome do contato: ")
        try:
            AGENDA[contato]
            print(">>>> contato já existente")
        except KeyError:
            telefone, email, endereço = ler_detalhes_contato()
            incluir_editar_contato(contato,telefone, email, endereço)

    elif opção == "4":
        contato = input("Digite o nome do contato: ")
        try:
            AGENDA[contato]
            print(">>>>>>> Editando contato:", contato)
            telefone, email, endereço = ler_detalhes_contato()
            incluir_editar_contato(contato,telefone, email, endereço)
        except KeyError:
            print(">>>>>> Contato inexistente")

    elif opção == "5":
        contato = input("Digite o nome do contato: ")
        excluir_contato(contato)

    elif opção == "6":
         nome_do_arquivo =input("Digite o nome do arquivo a ser exportado: ")
         exportar_contatos(nome_do_arquivo)

    elif opção == "7":
        nome_do_arquivo =input("Digite o nome do arquivo a ser importado: ")
        importar_contatos(nome_do_arquivo)


    elif opção == "0":
        print(">>>>>>> fechando o programa")

        break
else:
    print(">>>>>>> opção inválida")



    #split: dividi em palavras falando com caracetere ("é")
    #strip tira o \n no final
    #len < conta o tamanho do objeto que tenha itens la dentro, inclusive na agenda.