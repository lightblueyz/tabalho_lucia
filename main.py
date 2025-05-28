from search_plane import planes_list
from insert_planes import insert_plane
from insert_clients import insert_client
from buy_pass import buy_pass
from insert_planes import voos
import os 

i = 0

while i < 1:
    print("-" * 50)
    print("BEM-VINDO AO MENU DA AGÊNCIA Preventi filho da puta")  
    print("1 - Cadastrar um Voo")
    print("2 - Consultar um Voo")
    print("3 - Cadastro de clientes")
    print("4 - Listar os Passageiros de um Voo")
    print("5 - Venda de Passagem")
    print("6 - Cancelamento de Passagem")
    print("0 - Sair")
    print("-" * 50)
    entrada = input("Digite a opção que deseja: ")

    if entrada.isdigit():
        opcao = int(entrada)

        if opcao == 0:
            print("Encerrando o sistema. Até logo!")
            break
        elif opcao == 1:
            os.system("cls")
            num_p = int(input("Digite a quantidade de voos que deseja adicioanar: "))
            insert_plane(num_p)
        elif opcao == 2:
            planes_list()
        elif opcao == 3:
            os.system("cls")
            num_c = int(input("Digite a quantidade de clientes que deseja adicioanar: "))
            insert_client(num_c)
        elif opcao == 4:
            print("Opção 4 ainda em desenvolvimento.")
        elif opcao == 5:
            buy_pass(voos)
        elif opcao == 6:
            print("Opção 6 ainda em desenvolvimento.")
        else:
            print("Opção inválida. Digite um número de 0 a 6.")
    else:
        print("Entrada inválida. Digite apenas números.")

    input("\nPressione Enter para continuar...")
