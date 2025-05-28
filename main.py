from search_plane import planes_list
from buy_pass import buy_pass
from insert_clients import insert_client
from list_clients import list_client
from insert_planes import insert_plane

 

# MENU
while True:
    print("-" * 50)
    print("BEM-VINDO AO MENU DA AGÊNCIA AVIÁRIA")
    print("1 - Cadastrar um Voo")
    print("2 - Consultar um Voo (EM DESENVOLVIMENTO)")
    print("3 - Informar o Voo com menor Escala")
    print("4 - Listar os Passageiros de um Voo")
    print("5 - Venda de Passagem")
    print("6 - Cancelamento de Passagem (EM DESENVOLVIMENTO)")
    print("0 - Sair")
    print("-" * 50)
    entrada = input("Digite a opção que deseja: ")

    if entrada.isdigit():
        opcao = int(entrada)

        if opcao == 0:
            print("Encerrando o sistema. Até logo!")
            break
        elif opcao == 1:
            insert_plane()  
        elif opcao == 2:
            print("Opção 2 ainda em desenvolvimento.")
        elif opcao == 3:
            planes_list()
        elif opcao == 4:
            list_client()
        elif opcao == 5:
            buy_pass()
        elif opcao == 6:
            print("Opção 6 ainda em desenvolvimento.")
        else:
            print("Opção inválida. Digite um número de 0 a 6.")
    else:
        print("Entrada inválida. Digite apenas números.")

    input("\nPressione Enter para continuar...")
