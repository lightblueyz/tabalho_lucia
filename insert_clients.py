clientes = []
import os

def insert_client(num):     

    i = 0
    os.system("cls")

    while i != num:
         
        os.system("cls")
        cpf = ""
        name = ""
        phone = ""
        qtd_passagens = 0 
        voos = []

        cpf = input("Digite o cpf:")
        name = input("Digite o nome:")
        phone = input("Digite o telefone(com DDD):")
        os.system("cls")

        cliente = {
                "cpf": cpf,
                "nome": name,
                "telefone": phone,
                "qtd_compras": qtd_passagens,
                "voos": voos
            }
        clientes.append(cliente)
        i+= 1
        