# Exercıcios da Aula 1 (Listas)

# 1.Regressiva: Faca uma funcao que crie e retorne uma lista com todos os numeros pares de 1 a 100, porem na ordem regressiva
def regressiva():
    l = []
    for i in range(2,101,2):
        l.append(i)
    l.reverse()
    return l

# 2.Metade: Faca um procedimento que leia 10 numeros digitados pelo usuario, armazene a metade de cada um deles numa lista, e depois imprima esta lista.
def metade():
    l = []
    i = 0
    a = int(input())
    while i < 10:
        a = a/2
        l.append(a)
        i += 1
        a = int(input())
    return l

# 3.Leitura: Dado um numero n, faca uma funcao que leia n numeros inteiros, e retorne uma lista com esses numeros.
def leitura():
    l = []
    n = int(input())
    i = 0
    while i<n:
        z = int(input())
        l.append(z)
        i+=1
    return l

# 4.Ocorrencias: Dada uma lista e um elemento, retorne o numero de ocorrencias do elemento na lista.
def ocorrencias(l,n):
    n_ocorrencias = 0
    for i in l:
        if i==n:
            n_ocorrencias += 1
    return n_ocorrencias


# Maximo: Dada uma lista de numeros, faca uma funcao que encontre e retorne o maior deles.
def maximo(l):
    maior = l[0]
    for i in l:
        if i>maior:
            maior = i
    return maior

# 6.Posicao do Maximo: Dada uma lista de numeros, faca uma funcao que encontre e retorne o ́ındice do maior deles.
def p_maximo(l):
    maior = l[0]
    posicao = 0
    for i in range(len(l)):
        if l[i]>maior:
            maior = l[i]
            posicao = i
    return posicao

# 7.Inverter: Dada uma lista, faca um procedimento que inverta a ordem de seus elementos.
def inverter(l):
    l = l[::-1]
    return l



# Exercıcios da Aula 2 (Listas)
# 8.Fibonacci: Dado um numero n, retorne uma lista com os n primeiros elementos da sequencia de Fibonacci. Obs.: Cada elemento da sequencia ́e obtido atraves da
# soma dos dois elementos anteriores:
def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        l = [1,1]
        x = 0
        for i in range(1,n-1):
            x = l[i]+l[i-1]
            l.append(x)
        return l

# 9.Ordenadas e abscissas: Defina um procedimento que receba duas listas com a mesma quantidade de numeros inteiros. A primeira lista contem as abscissas de um conjunto de pontos,
#  e a segunda contem as ordenadas desses mesmos pontos.Calcule o numero a de abscissas que sao pares e o numero b de ordenadas que sao
# ımpares. Se a≥b, imprima a soma de todas as abscissas. Caso contrario, imprima o produto de todas as ordenadas.
def ord_abs(l1,l2):
    a = 0
    b = 0
    x = 0
    y = 1
    for i in l1:
        if i%2==0:
            a+=1
    for i in l2:
        if i%2==1:
            b+=1
    
    if a>=b:
        for i in l1:
            x+=i
        return x
    else:
        for i in l2:
            y*=i
        return y 

# 10.k Multiplos: Dados dois numeros k e n como parametros, retorne uma lista com todos os k primeiros multiplos de n
def k_multiplos(k, n):
    l = []
    for i in range(1,k+1):
        l.append(n*i)
    return l

# 11.Media: Faca um procedimento que leia um numero n e depois a notas de n alunos(0≤n≤100). Em seguida, calcule e imprima a media da turma, e o numero de
# alunos que ficaram com nota acima de 60.
def media():
    l = []
    nota_turma = 0
    n = int(input())
    reprovado = 0
    for i in range(n):
        nota_aluno = int(input())
        if nota_aluno<60:
            reprovado+=1
        nota_turma += nota_aluno
    nota_turma = nota_turma/n
    l.append(nota_turma)
    l.append(reprovado)
    print(l)

# 12.Temperaturas: Faca um procedimento que leia um numero n e a temperatura de n dias do ano. Em seguida, calcule a media de temperatura anual e imprima o
# numero de dias em que a temperatura ficou abaixo da media.
def temperaturas():
    l = []
    l2 = []
    media = 0
    n = int(input())
    for i in range(n):
        t = float(input())
        l.append(t)
    media = sum(l)/n
    for i in l:
        if i<media:
            l2.append(i)
    print(media, l2)

# 13.Iguais: Dadas duas listas l1 e l2 com a mesma quantidade de numeros, imprima quantos elementos aparecem exatamente na mesma posicao em ambas as listas.
def iguais(l1,l2):
    count = 0
    for i in range(len(l1)):
        if l1[i]==l2[i]:
            count+=1
    return count

# 14.Salarios: Dado um numero n, faca um procedimento que leia o nome e o salario de n funcionarios de uma empresa e imprima o nome de todos os funcionarios que
# ganham mais que a media dos demais.
def salarios():
    n = int(input())
    l = []
    l1 = []
    rico = []
    media = 0
    for i in range(n):
        nome = str(input())
        l1.append(nome)
        salario = int(input())
        l1.append(salario)
        l.append(l1)
        media += salario
        l1 = []
    media = media/n

    for i in l:
        if i[1]>media:
            rico.append(i[0])
    print(rico)

# 15.Sublista: Dada uma lista ordenada l e dois inteiros x e y(x < y), retorne uma sublista contendo todos os elementos de l que estiverem entre x e y
def sublista(l, x, y):
    slista = []
    for i in l:
        if i>x and i<y:
            slista.append(i)
    return slista

# 16.Troca de Cartas
def sem_repeticao(l):
    l.sort()
    l.count()
    

def troca_de_cartas(l1, l2):
    troca = []
    for i in l1:
        if i not in l2:
            troca.append(i)
    for j in l2:
        if j not in l1:
            troca.append(j)
    troca = sem_repeticao(troca)
