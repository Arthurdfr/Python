# 1.
def bonus():
    l = [("Valentina", 4, 1500), ("Enzo",33,1200), ("Anna Julia", 22, 3000), ("Simaria", 33, 1400)]
    maiortempo = 0
    for nome, meses, salario in l:
        if meses>maiortempo:
            maiortempo = meses
    for nome, meses, salario in l:
        if meses==maiortempo:
            print(nome,"=","{:.2f}".format(1.1*salario))

# 2.
def lucro(l):
    qntd_20 = 0
    percent = 0
    for preco, venda in l:
        if venda<1.2*preco:
            qntd_20 += 1
        if venda>1.25*preco:
            percent += 1
    return qntd_20, "{:.2f}%".format(100*percent/len(l))

# 3. determinante

# 4.
def agencia_turismo(l, a, b):
    x = 0
    y = 0
    for numero, companhia, escala in l:
        if escala[0]==a and escala[-1]==b:
            print("a)", end="")
            print(f"Voos que saem de {a} com destino em {b}: ", end="")
            print(numero, companhia)
    for numero, companhia, escala in l:
        if escala[0]==a and b in escala and b not in escala[-1]:
            print("b)", end="")
            print(f"Voos com origem em {a} com escala em {b}: ", end="")
            print(numero, companhia)
    for numero, companhia, escala in l:
        if a in escala and b in escala:
            for i in range(len(escala)):
                if escala[i]==a:
                    x = i
                elif escala[i]==b:
                    y = i
            if x==y-1:
                print("c)", end="")
                print(f"Voo(s) direto(s) de {a} para {b}: ", end="")
                print(numero, companhia)
#   voos = [(1024, "TAM", ["ES", "RJ", "SP", "NY"]), (1025, "GOL", ["ES", "NY", "SP"]), (1026, "AZUL", ["ES", "RJ", "NY", "SP"])]
#   a = "ES"
#   b = "NY"
#   agencia_turismo(voos, a, b)


# 5.
'''
def empates(jogos, classificacao):
    # jogos == empates + vitorias
    # v == jogos - empates
    # total == 2*e + 3*v
    # total == 2*e + 3*jogos -3*empates
    # empates == 3*jogos - total
    total = 0
    empate = 0
    j = jogos[0]
    for _, pontos in classificacao:
        total += pontos
    empate = 3*j - total
    return empate
    
def copa_do_mundo():
    jogos = [3]
    classificacao = [("Brasil", 5), ("Australia", 1), ("Croacia", 1)]
    print(empates(jogos, classificacao))
copa_do_mundo()
'''

def soma_pontos(classificacao):
    soma = 0 
    for _, pontos in classificacao:
        soma += pontos
    return soma
def copa_do_mundo(jogos, classificacao):
    return 3*jogos - soma_pontos(classificacao)
# copa_do_mundo(3, [("Brasil", 5), ("Australia", 1), ("Japao", 1)])



# 
import os
def limpaTela():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

from random import randint
def genius():
    sorteado = randint(1,4)
    correta = str(sorteado)
    print("O primeiro número sorteado foi:", sorteado)
    x = input("Digite a sequência: ")
    while x == correta:
        limpaTela()
        sorteado = randint(1,4)
        correta = correta + str(sorteado)
        print("O primeiro número sorteado foi:", sorteado)
        x = input("Digite a sequência: ")

    print(f"Você acertou {len(correta)-1} número(s).")
