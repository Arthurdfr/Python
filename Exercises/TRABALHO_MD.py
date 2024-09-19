import time

def insertion_sort(l):
    comeco = time.time()
    for k in range(1, len(l)):
        elem = l[k]
        pos = k-1
        while pos>=0 and l[pos]>elem:
            l[pos+1] = l[pos]
            pos = pos-1
        l[pos+1] = elem
    fim = time.time()

    return l, fim-comeco

def insertion_sort_comparacoes_recorrente(n):
    if n > 1:
        return insertion_sort_comparacoes_recorrente(n-1) + (n//2)
    else:
        return 0

def insertion_sort_comparacoes(n):     # número de comparações
    return (n**2)//4 + n//4

# exemplo de uso
import random

lista_aleatoria = []

tamanho = int(input("Qual o tamanho da lista? "))

for i in range(tamanho):
    lista_aleatoria.append(random.randint(0,100))

print(f"Lista sem ordenação: {lista_aleatoria}")

lista_ordenada, tempo = insertion_sort(lista_aleatoria)

print(f"Lista com ordenação: {lista_ordenada}  |   Tempo gasto: {tempo}")
#print(f"Número de comparações f.recorrente: {insertion_sort_comparacoes_recorrente(tamanho)}")
print(f"Número de comparações f.fechada: {insertion_sort_comparacoes(tamanho)}")