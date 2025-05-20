voos = []
def insert_planes():
    import random
    import os
    

    id_voo= random.randrange(100000, 999999)
    
    
    id_voo= id_voo
    city_origem=input('Digite a cidade de origem:')
    city_destino=input('Digite seu destino:')
    n_escalas=int(input('Digite o número de escalas:'))
    preco=input('Digite o valor:')
    qtd_lugares=input('Digite a quantidade de lugares:')
    passageiros = []


    voo={ 
        "ID do Voo":id_voo,
        "Cidade de Origem":city_origem,
        "Cidade Destino":city_destino,
        "Número de Escalas":n_escalas,
        "Preço":preco,
        "Quantidade de Lugares":qtd_lugares,
    }
    
    voos.append(voo)
if __name__ == "__main__":
    insert_planes()
    print(voos)
    

    