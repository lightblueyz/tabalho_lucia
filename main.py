from plane_functions.search_plane import planes_list
from plane_functions.insert_planes import insert_plane


i = 0

while i < 1:
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
            planes_list()
        elif opcao == 3:
            print("Opção 3 ainda em desenvolvimento.")
        elif opcao == 4:
            print("Opção 4 ainda em desenvolvimento.")
        elif opcao == 5:
            print("Opção 5 ainda em desenvolvimento.")
        elif opcao == 6:
            print("Opção 6 ainda em desenvolvimento.")
        else:
            print("Opção inválida. Digite um número de 0 a 6.")
    else:
        print("Entrada inválida. Digite apenas números.")

    input("\nPressione Enter para continuar...")
