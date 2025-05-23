from search_plane import planes_list
from buy_pass import buy_pass
from insert_clients import insert_client
from list_clients import list_client
from insert_planes import insert_plane
#MENU

print('-'*50)
print('BEM-VINDO AO MENU DA AGÊNCIA AVIÁRIA')
print('1-Cadastrar um Voo: permitir a inserção de um novo voo ao sistema.')
print('2-Consultar um Voo: a consulta poderá ser:')
print('3-Informar o Voo com menor Escala, dado a cidade Origem e Destino')
print('4-Listar os Passageiros de um Voo: Dados o código do Voo listar os passageiros que compraram passagem e a quantidade de lugares disponíveis do voo')
print('5-Venda de passagem : permitir que um cliente compre uma passagem para um voo disponível, solicitando suas informações. As informações da lista de passageiro e da capacidade disponível devem ser atualizadas.')
print('6-Cancelamento de Passagem : Através do cancelamento da passagem, a lista de passageiros do voo e a capacidade disponível são alteradas.')
opcao=int(input('Digite a opção que deseja:'))

if opcao=='1':
    insert_plane()
elif opcao=='2':
    #FALTA 2
#elif opcao=='3':
    planes_list
elif opcao=='4':
    list_client
elif opcao=='5':
    buy_pass()
elif opcao=='6':
    #FALTA 6
#else:
    print('Opção inválida')



# https://excalidraw.com/#json=9C_UYBGGq1wjSwRXrG5zE,0lNL9zpwWunMktIXb2M42w



