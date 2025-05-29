from search_plane import planes_list
from insert_planes import insert_plane
from insert_clients import insert_client
from buy_pass import buy_pass
from insert_planes import voos
from list_clients import list_client
from list_planeclientes import list_planeclients
from remove_pass import remove_pass
import os

while True:
    os.system("cls")  
    print("-" * 50)
    print("BEM-VINDO AO MENU DA AGÊNCIA AÉREA")
    print("1 - Cadastrar um Voo")
    print("2 - Consultar um Voo")
    print("3 - Cadastro de clientes")
    print("4 - Listar os Passageiros de um Voo")
    print("5 - Venda de Passagem")
    print("6 - Cancelamento de Passagem")
    print("7 - Procurar cliente")
    print("0 - Sair")
    print("-" * 50)

    entrada = input("Digite a opção que deseja: ")

    if entrada.isdigit():
        opcao = int(entrada)

        if opcao == 0:
            print("\nEncerrando o sistema. Até logo!")
            break

        elif opcao == 1:
            os.system("cls")
            qtd = input("Digite a quantidade de voos que deseja adicionar: ")
            if qtd.isdigit():
                insert_plane(int(qtd))
            else:
                print("Quantidade inválida.")

        elif opcao == 2:
            os.system("cls")
            planes_list()

        elif opcao == 3:
            os.system("cls")
            qtd = input("Digite a quantidade de clientes que deseja adicionar: ")
            if qtd.isdigit():
                insert_client(int(qtd))
            else:
                print("Quantidade inválida.")

        elif opcao == 4:
            os.system("cls")
            list_planeclients()

        elif opcao == 5:
            os.system("cls")
            buy_pass()

        elif opcao == 6:
            os.system("cls")
            remove_pass()

        elif opcao == 7:
            os.system("cls")
            list_client()

        else:
            os.system("cls")
            print("Opção inválida. Digite um número de 0 a 7.")

    else:
        print("\nEntrada inválida. Digite apenas números de 0 a 7.")

    input("\nPressione Enter para continuar...")
