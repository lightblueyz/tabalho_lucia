from insert_clients import clientes 
from insert_planes import voos
import os

def remove_pass(): 
    import os

    os.system("cls")

    j = 0
    search_voo = int(input("Digite o número do voo: "))
    id_plane = 0
    voo_encontrado = False

    while j < len(voos):
        if voos[j]["plane_id"] == search_voo:
            id_plane = voos[j]["plane_id"]
            print("ID do VOO:", voos[j]["plane_id"])
            print("Cidade de Origem:", voos[j]["city_origem"])
            print("Cidade Destino:", voos[j]["city_destino"])
            print("Número de escalas:", voos[j]["n_escalas"])
            print("Preço:", voos[j]["preco"])
            print("Quantidade de lugares:", voos[j]["qtd_lugares"])
            print("Status do Voo:", voos[j]["plane_status"])
            print("Passageiros:", voos[j]["passageiros"])
            print("-" * 50)
            voo_encontrado = True
            break
        j += 1

    if voo_encontrado == False:
        print("Voo não encontrado!")
        return

    search_cpf = input("Digite o CPF do comprador: ")
    i = 0
    cpf_encontrado = False

    while i < len(clientes):
        if clientes[i]["cpf"] == search_cpf:
            print("CPF:", clientes[i]["cpf"])
            print("Nome:", clientes[i]["nome"])
            print("Telefone:", clientes[i]["telefone"])
            print("Qtd de compras:", clientes[i]["qtd_compras"])
            print("Voos:", clientes[i]["voos"])
            print("-" * 50)
            cpf_encontrado = True
            break
        i += 1

    if cpf_encontrado == False:
        print("Cliente não encontrado!")
        return

    qtd = int(input("Digite a quantidade que deseja cancelar: "))

    clientes[i]["voos"].remove(id_plane)
    clientes[i]["qtd_compras"] -= qtd
    voos[j]["passageiros"].remove(search_cpf)
    voos[j]["qtd_lugares"] += qtd
    print("Passagens Canceladas!")
    
    if voos[j]["qtd_lugares"] == 0:
        voos[j]["plane_status"] = "Indisponível"
    else:
        voos[j]["plane_status"] = "Disponível"
