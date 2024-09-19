# LISTA DICIONARIO

# 1.
def adultos():
    agenda = {}
    agendamaior = {}
    for i in range(4):
        nome = str(input("Digite o nome: "))
        idade = int(input("Digite a idade: "))
        telefone = str(input("Digite o telefone: "))
        agenda[nome] = [idade, telefone]

    for nome in agenda:
        if agenda[nome][0] >= 18:
            agendamaior[nome] = agenda[nome]

    return agendamaior

# 2.
import os
def LimpaTela():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def CadastrarTelefone(lista):
    x = 1
    while x == 1:
        print("Vamos lá!")
        nome = str(input("Digite o nome: "))
        idade = int(input("Digite a idade: "))
        telefone = str(input("Digite o telefone: "))
    
        lista[nome] = [idade, telefone]
        LimpaTela()
        print("Deseja cadastrar outro contato?")
        x = int(input("Se sim, digite 1. Caso contrário, digite 0: "))
        LimpaTela()

    return lista


def agenda():
    menu = '''
1) Cadastrar telefone
2) Visualizar agenda
3) Sair
'''
    print(menu)
    x = int(input("Digite aqui: "))
    
    lista = {}

    while x == 1 or x == 2:
        LimpaTela()
        if x == 1:
            CadastrarTelefone(lista)
        elif x == 2:
            for nome in lista:
                print(f"O telefone de {nome} é: {lista[nome][1]}", end="    ")
                print(f"Atualmente, {nome} tem {lista[nome][0]} anos.")
        print()
        print(menu)
        x = int(input("Digite aqui: "))
    
    print("Tchau!")

# 4.
def MaisVelho(a, b, c, d):
    diaa = a[0]+a[1]
    mesa = a[3]+a[4]
    anoa = a[6]+a[7]+a[8]+a[9]
    diab = b[0]+b[1]
    mesb = b[3]+b[4]
    anob = b[6]+b[7]+b[8]+b[9]
    if anoa>anob:
        return d
    elif anoa<anob:
        return c
    elif mesa>mesb:
        return d
    elif mesa<mesb:
        return c
    elif diaa>diab:
        return d
    else:
        return c

def Concurso(candidatos, areas, codigo):
    #candidato = inscricao, nome, data ded nascimento, nota1 e nota2.
    # area = codigo, nome e lista com numero de inscricao dos inscritos
    # a)
    print('a)')
    for codigo in areas:
        for inscricao in areas[codigo][1]:
            if candidatos[inscricao][2]>=60:
                print(inscricao, '=', candidatos[inscricao][0])

    # b)
    print('b)')
    for area in areas:
        maiornota = 0
        aprovado = 0
        for inscricao in areas[area][1]:
            notafinal = candidatos[inscricao][2] + candidatos[inscricao][3]
            if notafinal > maiornota:
                maiornota = notafinal
                aprovado = inscricao
                nome = candidatos[inscricao][0]
            elif notafinal == maiornota:
                if candidatos[inscricao][0] == MaisVelho(candidatos[aprovado][1], candidatos[inscricao][1], candidatos[aprovado][0], candidatos[inscricao][0]):
                    maiornota = notafinal
                    aprovado = inscricao
                    nome = candidatos[inscricao][0]

        
        print(f"O aprovado de {area} foi {nome}({aprovado})")
            




    #candidatos = {123 : ['Joao', '20/10/2005', 60, 60], 456 : ['Maria', '10/10/2005', 60, 60]}
    #areas = {'Quimica' : ['tecnologia', [123, 456]]}
    #codigo = 'Quimica'
    #Concurso(candidatos, areas, codigo)

# 5.
def anterior(atual, outra):
    dia1, mes1, ano1 = atual
    dia2, mes2, ano2 = outra
    if ano1 < ano2:
        return True
    if ano1 > ano2:
        return False
    if mes1 < mes2:
        return True
    if mes1 > mes2:
        return False
    if dia1 < dia2:
        return True
    if dia1 > dia2:
        return False
    return False

def recentes(infracoes, data):
    dia, mes, ano = data
    ano = ano-1
    lista = []
    for i in range(len(infracoes)):
        if anterior((dia, mes, ano), infracoes[i][1]):
            lista.append(infracoes[i])
    return lista

def pontosCNH(cnh, infracoes, naturezas, veiculos):
    pontos = 0
    for placa in veiculos:
        if veiculos[placa][0] == cnh:
            for infracao in infracoes:
                if infracao[2] == placa:
                    pontos += naturezas[infracao[3]]
    return pontos


def blitz(cnh, placa, data, infracoes, motoristas, veiculos, naturezas):

    if placa not in veiculos:
        print(f"A placa {placa} não está cadastrada!")
    elif not anterior(data, motoristas[cnh][1]):
        print(f"A cnh '{cnh}' está vencida.")
    elif pontosCNH(cnh, infracoes, naturezas, veiculos) >= 20:
        print(f"O motorista possui {pontosCNH(cnh, infracoes, naturezas, veiculos)} pontos na cnh.")
    else:
        print(f"{veiculos[placa][1], veiculos[placa][2]}")
        print(f"Nome do proprietário: {motoristas[veiculos[placa][0]][0]}", end="   ")
        print(f"Pontuação do proprietário: {pontosCNH(veiculos[placa][0], infracoes, naturezas, veiculos)}")
        print(f"Nome do motorista: {motoristas[cnh][0]}", end="    ")
        print(f"Pontos do motorista: {pontosCNH(cnh, infracoes, naturezas, veiculos)}")

    


    #motoristas = {"01234567": ("SeuMadruga", (15, 10, 2019)), 
                # "12345678": ("DonaFlorinda", (14, 10, 2019))}

    #veiculos = {"FLA1981": ("12345678","Fusca","Preto"), 
            #"ALE2014": ("12345678","Brasilia","Prata"), 
            #"BRU0071": ("01234567","Chevette","Branco")}

    #infracoes = [("I0001",(15 ,10 ,2018) ,"BRU0071","Gravissima"), 
             #("I0002",(16 ,10 ,2018) ,"BRU0071","Gravissima"), 
             #("I0003",(17 ,10 ,2018) ,"ALE2014","Leve") ]

    #naturezas = {"Leve": 3,
             #"Media": 4,
             #"Grave": 5,
             #"Gravissima": 7}

    #data = (14,10,2019)

    #blitz('01234567', "ALE2014", data, recentes(infracoes,data), motoristas, veiculos, naturezas)