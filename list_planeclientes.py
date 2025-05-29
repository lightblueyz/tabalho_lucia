from insert_planes import voos


def list_planeclients():
    i = 0
    inserir_id_voo = int(input("Insira o ID do Voo que deseja:"))
    while i < len(voos):
        if voos[i]["plane_id"] == inserir_id_voo:
            print(voos[i]["passageiros"])
        else:
            print("Esse Voo não existe!")
        i += 1


