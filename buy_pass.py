from insert_clients import clientes 
from insert_planes import voos
from insert_clients import insert_client
from insert_planes import insert_plane
import os

num_c = int(input("Digite a quantidade de clientes que deseja adicioanar: "))


insert_client(num_c)
insert_plane()



def buy_pass(): 
    os.system("cls")

    i = 0
    j = 0


    search_voo = int(input("Digite o número do voo: "))
    while j < len(voos):
        plane_verify = 0 
        if voos[j]["plane_id"] == search_voo:
            plane_verify = j
            print("Voo com origem a : ", voos[j]["city_origem"])
            break

        elif search_voo not in search_voo:
            j += 1 

        if j == len(voos):
         print ("Voo não encontrado!")
         print ("Digite novamente: ")
        else:
           continue 


    search_cpf = input("Digite o cpf do comprador: ")
    while i < len(clientes):
        cpf_verify = 0
        if clientes[i]["cpf"] == search_cpf:
            cpf_verify = i  
            print("nome do cliente : ", clientes[i]["nome"])
            break
        elif search_cpf not in clientes:
            i += 1
        if j == len(clientes):
         print ("Cliente não encontrado!")
         break


    qtd = int(input("Digite a quantidade de passagens: "))

    
    

    
         
        

    
    
buy_pass()        
