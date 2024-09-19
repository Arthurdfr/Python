#INTEGRANTES DO TRABALHO
#PEDRO VITOR SANTIAGO ZUQUI - 20231BSI0210
#ARTHUR DE FRANÇA ROCHA - 20231BSI0066



import pickle
import time

seconds = time.time()

with open("backupmilhao.bin", "rb") as arq:
    usuarios = pickle.load(arq)         #dicionario
    conexoes = pickle.load(arq)         #dicionario
    historico = pickle.load(arq)        #lista

    for x,y in historico:
        if y not in conexoes[x][1] and y not in conexoes[x][2]:
            if y not in conexoes[x][0]:
                conexoes[x][0].append(y)
            if x not in conexoes[y][1]:
                conexoes[y][1].append(x)     #coloca x em gostou de y
        else:
            if y in conexoes[x][1]:
                conexoes[x][2].append(y)   #coloca y em mutuo de x
                if y in conexoes[x][0]:
                    conexoes[x][0].remove(y)   #remove y de gostei de x
                if x in conexoes[y][1]:
                    conexoes[y][1].remove(x)   #remove x de gostou de y



with open("dados.bin", "wb") as arq:    #novo arquivo atualizado
    pickle.dump(usuarios, arq)
    pickle.dump(conexoes, arq)

seconds1 = time.time()

print(seconds1-seconds)