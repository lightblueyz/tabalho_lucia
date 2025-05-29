from insert_planes import voos
import os




def planes_list():
    
    os.system("cls")
    print('-'*50)
    print('1-Cidade de Origem')
    print('2-Cidade Destino')
    print('3-Voo com menos escalas')
    listagem = input('Escolha a opção que deseja procurar:')

    os.system("cls")

    if listagem == '1':
        escolhaorigem=input('Defina a cidade de origem:')
        os.system("cls")
        i=0
        while i < len(voos):
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
        os.system("cls")
        i = 0
        while i < len(voos):
            if voos[i]["city_destino" ]== escolhadestino:
                print("ID do VOO:", voos[i]["plane_id"])
                print("Cidade de Origem:", voos[i]["city_origem"])
                print("Cidade Destino", voos[i]["city_destino"])
                print("Número de escalas:", voos[i]["n_escalas"])
                print("Quantidade de lugares:", voos[i]["qtd_lugares"])
                print("Status do Voo:", voos[i]["plane_status"])
                print("Passageiros:", voos[i]["passageiros"])
                print("-" * 50)  
            i += 1
    elif listagem == '3':
        os.system("cls")
        i = 0
        menor_escala = voos[0]["n_escalas"]
        voo_menor_escala = voos[0]

        while i < len(voos):
            if voos[i]["n_escalas"] < menor_escala:
                menor_escala = voos[i]["n_escalas"]
                voo_menor_escala = voos[i]
            i += 1

        print("ID do VOO:", voo_menor_escala["plane_id"])
        print("Cidade de Origem:", voo_menor_escala["city_origem"])
        print("Cidade Destino:", voo_menor_escala["city_destino"])
        print("Número de escalas:", voo_menor_escala["n_escalas"])
        print("Quantidade de lugares:", voo_menor_escala["qtd_lugares"])
        print("Status do Voo:", voo_menor_escala["plane_status"])
        print("Passageiros:", voo_menor_escala["passageiros"])
        print("-" * 50)

    else:
        print("Opção Inválida")
        