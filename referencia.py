import os  


alunos = []


qtdA = int(input("Digite a quantidade de alunos: "))
os.system('cls')
for i in range(qtdA):
    print(f"\nAluno {i + 1}")
    nome = str(input("Digite o nome do aluno: "))

    t1 = float(input("Digite a nota da prova teÃ³rica 1: "))
    t2 = float(input("Digite a nota da prova teÃ³rica 2: "))

    p1 = float(input("Digite a nota do projeto 1: "))
    p2 = float(input("Digite a nota do projeto 2: "))

    mt = round(t1 * 0.4 + t2 * 0.6, 2)
    mp = round((p1 + p2) / 2, 2)

    if mt >= 5 or mp >= 5:
        mf = round(mp * 0.3 + mt * 0.7, 2)
    else:
        mf = min(mt, mp)

    aluno = {
        "nome": nome,
        "mt": mt,
        "mp": mp,
        "mf": mf
    }

    alunos.append(aluno)
    
os.system('cls')

j = 0
while j < 1:
    print("\n" + "=" * 28)
    print("       MENU DE OPÃ‡Ã•ES       ")
    print("=" * 28)

    print("\n1 - Um boletim com o nome de cada aluno, sua MÃ©dia TeÃ³rica (MT), MÃ©dia PrÃ¡tica (MP) e MÃ©dia Final (MF)")
    print("\n2 - Permitir que o usuÃ¡rio digite o nome do aluno e imprima todas as informaÃ§Ãµes sobre ele")
    print("\n3 - O nome do aluno com maior MÃ©dia Final (MF)")
    print("\n4 - O nome do aluno com menor MÃ©dia Final (MF)")
    print("\n5 - Percentual dos alunos com MÃ©dia Final (MF) superior a 5.0")

    digito = int(input("\nDIGITE A OPÃ‡ÃƒO QUE DESEJA: "))
    os.system('cls')
    if digito == 1 or digito == 2 or digito == 3 or digito == 4 or digito == 5:
        if digito == 1:
            print("\nLista de Alunos:")
            for aluno in alunos:
                print(f"{aluno['nome']} : MT: {aluno['mt']:.2f} | MP: {aluno['mp']:.2f} | MF: {aluno['mf']:.2f}")

        elif digito == 2:
            nome_busca = input("Digite o nome que deseja buscar: ")
            i = 0
            while i < len(alunos):
                if nome_busca.lower() == alunos[i]["nome"].lower():
                    print(f"\nAluno encontrado: {alunos[i]}")
                    break
                i += 1
            else:
                print("Aluno nÃ£o encontrado.")

        elif digito == 3:
            if alunos:
                maior = alunos[0]
                for aluno in alunos:
                    if aluno['mf'] > maior['mf']:
                        maior = aluno
                print(f"\nAluno com maior MÃ©dia Final (MF): {maior['nome']} - {maior['mf']:.2f}")
            else:
                print("NÃ£o hÃ¡ alunos cadastrados.")

        elif digito == 4:
            if alunos:
                menor = alunos[0]
                for aluno in alunos:
                    if aluno['mf'] < menor['mf']:
                        menor = aluno
                print(f"\nAluno com menor MÃ©dia Final (MF): {menor['nome']} - {menor['mf']:.2f}")
            else:
                print("NÃ£o hÃ¡ alunos cadastrados.")

        elif digito == 5:
            total = len(alunos)
            acima5 = 0

            for aluno in alunos:
                if aluno['mf'] > 5.0:
                    acima5 += 1

            percentual = acima5 / total * 100

            print("O percentual de alunos com a mÃ©dia acima de 5 Ã© de: ", percentual)

        print("SIM ( s )   NÃƒO ( n )")
        denovo = input("DESEJA ALGO MAIS? ")
        if denovo.lower() == "s":
            j = 0
            os.system('cls')
        elif denovo.lower() == "n":
            j += 1
        else:
            print("Entrada incorreta, digite apenas (s) ou (n)")
            denovo = input("DESEJA ALGO MAIS? ")
            os.system('cls')

    else:
        print("NÃšMERO INVÃLIDO!!")
        j = 0
        