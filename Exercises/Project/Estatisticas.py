#INTEGRANTES DO TRABALHO
#PEDRO VITOR SANTIAGO ZUQUI - 20231BSI0210
#ARTHUR DE FRANÇA ROCHA - 20231BSI0066



import pickle
import time
seconds = time.time()

def main():
    with open("dados.bin", "rb") as arq:
        usuarios = pickle.load(arq)
        conexoes = pickle.load(arq)
        logins = []
        for login in usuarios:
            logins.append(login)
    
    with open("top.txt", "w") as arq:
        logins = mergeSort(logins, usuarios, conexoes)
        arq.write(cidadeNome(logins[0]))
        for i in range(1, len(logins)-1):
            if usuarios[logins[i]][1] != usuarios[logins[i-1]][1]:
                arq.write(f"\n{cidadeNome(logins[i])}")



def cidadeNome(x):
    with open("dados.bin", "rb") as arq:
        usuarios = pickle.load(arq)
    return f"{usuarios[x][1]} {usuarios[x][0]}"




def mergeSort(logins, usuarios, conexoes):
    l = []
    if len(logins) > 1:
        meio = len(logins) // 2
        lEsq = logins[:meio]
        lDir = logins[meio:]
        mergeSort(lEsq, usuarios, conexoes)
        mergeSort(lDir, usuarios, conexoes)

        l = merge(logins, lEsq, lDir, usuarios, conexoes)
    return l

def merge(l, lEsq, lDir, usuarios, conexoes):
    i, j, k = 0,0,0

    while i < len(lEsq) and j < len(lDir):
        if anterior(lEsq[i],lDir[j], usuarios, conexoes):
            l[k] = lEsq[i]
            i += 1
        else:
            l[k] = lDir[j]
            j += 1
        k += 1

    while i < len(lEsq):
        l[k] = lEsq[i]
        i += 1
        k += 1
    
    while j < len(lDir):
        l[k] = lDir[j]
        j += 1
        k += 1
    return l

def anterior(lEsq, lDir, usuarios, conexoes):
    if usuarios[lEsq][1] < usuarios[lDir][1]: return True
    if usuarios[lEsq][1] > usuarios[lDir][1]: return False

    if (len(conexoes[lEsq][1]) + len(conexoes[lEsq][2])) > (len(conexoes[lDir][1]) + len(conexoes[lDir][2])): return True
    if (len(conexoes[lEsq][1]) + len(conexoes[lEsq][2])) < (len(conexoes[lDir][1]) + len(conexoes[lDir][2])): return False

    if lEsq < lDir: return True
    return False

    
if __name__ == '__main__':
    main()

seconds1 = time.time()
print(seconds1-seconds)