
voos = []
import random
import os

def insert_plane(num_p):
    i = 0
    while i != num_p:
       
        os.system("cls")  
        id_voo = random.randrange(10, 99)
        city_origem = input("Digite a cidade de origem: ")
        city_destino = input("Digite seu destino: ")
        n_escalas = int(input("Digite o número de escalas: "))
        preco = float(input("Digite o valor: "))
        qtd_lugares = int(input("Digite a quantidade de lugares: "))
        plane_status = "Disponível"
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
        print("Voo Cadastrado!")
        i+= 1

