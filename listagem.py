
from insert_planes import voos
from insert_planes import insert_plane



insert_plane()
def planes_list():
    print('-'*50)

    print('1-Cidade de Origem')
    print('2-Cidade Destino')
    print('3-Voo com menos escalas')

    listagem=input('Escolha a opção que deseja procurar:')

    if listagem=='1':
        escolhaorigem=input('Defina a cidade de origem:')
        voo_encontrado=[voo for voo in voos if voo["Cidade de Origem"]==escolhaorigem]
    elif listagem=='2':
        escolhadestino=input('Defina o seu destino:')
        voo_encontrado=[voo for voo in voos if voo["Cidade Destino"]==escolhadestino]
    elif listagem=='3':
        menorescala=input("Quantas escalas deseja:")
        voo_encontrado=[voo for voo in voos if voo["Número de Escalas"]==menorescala]
    else:
        print("Opção Inválida")
        voo_encontrado=[]

    if voo_encontrado:
        for i in voo_encontrado:
            print(i)
    else:
        print("Nenhum voo encontrado")
planes_list()        