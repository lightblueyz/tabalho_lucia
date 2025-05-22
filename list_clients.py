from insert_clients import clientes
from insert_clients import insert_client
import os 


os.system("cls")
num = int(input("Digite a quantidade de clientes que deseja adicioanar: "))

insert_client(num)

filtro = input("Digite o nome que procura: ")

i = 0 



while i < len(clientes):
    if clientes[i]["nome"] == filtro:
        print("CPF:", clientes[i]["cpf"])
        print("Nome:", clientes[i]["nome"])
        print("Telefone:", clientes[i]["telefone"])
        print("Qtd de compras:", clientes[i]["qtd_compras"])
        print("Voos:", clientes[i]["voos"])
        print("-" * 50)  
    i += 1
