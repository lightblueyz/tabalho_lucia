from insert_clients import clientes
from insert_clients import insert_client
import os 

def list_client():
    os.system("cls")
    

    filtro = input("Digite o cpf que procura: ")

    i = 0 



    while i < len(clientes):
        if clientes[i]["cpf"] == filtro:
            print("CPF:", clientes[i]["cpf"])
            print("Nome:", clientes[i]["nome"])
            print("Telefone:", clientes[i]["telefone"])
            print("Qtd de compras:", clientes[i]["qtd_compras"])
            print("Voos:", clientes[i]["voos"])
            print("-" * 50)  
        i += 1


