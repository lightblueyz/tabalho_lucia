
from insert_planes import voos
from insert_planes import insert_plane
import os


insert_plane()
def planes_list():
    print('-'*50)

    print('1-Cidade de Origem')
    print('2-Cidade Destino')
    print('3-Voo com menos escalas')

    listagem=input('Escolha a opção que deseja procurar:')

    if listagem=='1':
        escolhaorigem=input('Defina a cidade de origem:')
        i=0
        while i<len(voos):
            if voos[i]["city_origem"] == escolhaorigem:
                print("ID do VOO:", voos[i]["plane_id"])
                print("Cidade de Origem:", voos[i]["city_origem"])
                print("Cidade Destino", voos[i]["city_destino"])
                print("Número de escalas:", voos[i]["n_escalas"])
                print("Preço:", voos[i]["preco"])
                print("Quantidade de lugares:", voos[i]["qtd_lugares"])
                print("Status do Voo:", voos[i]["plane_status"])
                print("Passageiros:", voos[i]["passageiros"])
                print("-" * 50)  
            i += 1
   
    elif listagem=='2':
        escolhadestino=input('Defina o seu destino:')
        i=0
        while i<len(voos):
            if voos[i]["city_destino"]== escolhadestino:
                print("ID do VOO:", voos[i]["id_voo"])
                print("Cidade de Origem:", voos[i]["city_origem"])
                print("Cidade Destino", voos[i]["city_destino"])
                print("Número de escalas:", voos[i]["n_escalas"])
                print("Quantidade de lugares:", voos[i]["qtd_lugares"])
                print("Status do Voo:", voos[i]["plane_status"])
                print("Passageiros:", voos[i]["passageiros"])
                print("-" * 50)  
            i += 1
    elif listagem=='3':
        menorescala=input("Quantas escalas deseja:")
        i=0
        while i<len(voos):
            if voos[i]["n_escalas"] == menorescala:
                print("ID do VOO:", voos[i]["id_voo"])
                print("Cidade de Origem:", voos[i]["city_origem"])
                print("Cidade Destino", voos[i]["city_destino"])
                print("Número de escalas:", voos[i]["n_escalas"])
                print("Quantidade de lugares:", voos[i]["qtd_lugares"])
                print("Status do Voo:", voos[i]["plane_status"])
                print("Passageiros:", voos[i]["passageiros"])
                print("-" * 50)  
            i += 1
    else:
        print("Opção Inválida")
planes_list()        

