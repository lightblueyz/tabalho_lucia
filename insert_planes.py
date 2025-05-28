# insert_planes.py
voos = []

def insert_plane():
    import random
    import os

    os.system("cls")  # ou "clear" se estiver no Linux/Mac
    id_voo = random.randrange(10, 99)
    print(id_voo)

    city_origem = input("Digite a cidade de origem: ")
    city_destino = input("Digite seu destino: ")
    n_escalas = int(input("Digite o número de escalas: "))
    preco = input("Digite o valor: ")
    qtd_lugares = input("Digite a quantidade de lugares: ")
    plane_status = True
    passageiros = []

    voo = {
        "plane_id": id_voo,
        "city_origem": city_origem,
        "city_destino": city_destino,
        "n_escalas": n_escalas,
        "preco": preco,
        "qtd_lugares": qtd_lugares,
        "plane_status": plane_status,
        "passageiros": passageiros,
    }

    voos.append(voo)
