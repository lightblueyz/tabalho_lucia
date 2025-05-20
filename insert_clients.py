
clientes = []
def insert_client():     
    
    import os
    

    i = 0
    while i < 3:
        os.system("cls")
        cpf = ""
        name = ""
        phone = ""
        qtd_passagens = 0 
        voo = ""
        voos = []



        cpf = input(":")
        name = input(":")
        phone = input(":")
        qtd_passagens= int(input(":"))
    

        cliente = {
                "cpf": cpf,
                "nome": name,
                "telefone": phone,
                "qtd_compras": qtd_passagens,
                "voos": voos
            }
        clientes.append(cliente)
        os.system("cls")
        i+= 1
        
        
        
     

insert_client()
print (clientes)   