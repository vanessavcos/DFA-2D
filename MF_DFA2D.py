import numpy as np
from scipy import stats
import robustLastSquare as fit
import time

########################DFA 2D####################################################################
def mfdfa2d(mat, grau, dirSaida, file):
    inicio = time.time()
    [l, c] = np.shape(mat)
    tam = np.minimum(l, c)
    mat = np.reshape(mat, (tam, tam))
    escalas = int(tam/4)
    k=0
    s = 10
    vetQ = np.arange(-15, 15.2, 0.2)
    qtQ = len(vetQ)
    vetoutput = np.zeros(shape=(1, qtQ + 1))
    vetoutput[0, 1:] = vetQ
    while (s <= escalas):
        matAtual = mat
        tamAtual = tam
        if np.mod(tamAtual, s) != 0:
            tamAtual = s * int(np.trunc(tamAtual / s))
            matAtual = mat[0:tamAtual, 0:tamAtual]
        qt = int(np.power((tamAtual / s), 2))
        t = np.arange(s, tamAtual, s)
        aux = np.array(np.array_split(matAtual, t, axis=1))
        matAtual = np.reshape(aux, (qt, s, s))
        vetvar = [fit.fit2D(np.cumsum(m).reshape(s, s), s, grau) for m in matAtual]
        k = 1
        vetAux = np.zeros(shape=(1, qtQ + 1))
        vetAux[0, 0] = s
        for i in vetQ:
            if (i != 0):
                aux = np.power(vetvar, (i/2))
                fs = np.power(np.mean(aux), (1 / i))
                vetAux[0, k] = fs
            else:
                aux = np.log(vetvar)
                fs = (np.sum(aux) / (2 * l))
                vetAux[0, k] = np.exp(fs)
            k = k + 1
        vetoutput = np.vstack((vetoutput, vetAux))
        s = s + 1
    n = ""
    f = file.split('+')
    a = [dirSaida, f[0], '_flutuacaoMFDFA2D.txt']
    flutuacao = n.join(a)
    with open(flutuacao, 'wb') as f:
        np.savetxt(f, vetoutput, fmt='%0.4f', delimiter='\t')
    vetoutput[1:, :] = np.log10(vetoutput[1:, :])
    calculaHq(vetoutput, dirSaida)

def calculaHq(vet, dirSaida):
    [l, c] = np.shape(vet)
    vetQ = vet[0, 1:c]
    vetS = vet[1:, 0]
    vet = vet[1:, 1:]
    [l, c] = np.shape(vet)
    vetSaida = np.zeros(shape=(c,1))
    for i in np.arange(0, c):
        y = vet[:, i]
        slope, _, _, _, _ = stats.linregress(vetS, y)
        vetSaida[i, 0] = slope
    nome = dirSaida + '_SaidaHQ2D.txt'
    with open(nome, 'ab') as f:
        np.savetxt(f, vetSaida.reshape(1,-1), fmt='%0.4f', delimiter='\t')
    vetSaida[:, 0] = vetSaida[:,0] * vetQ - 2
    nome = dirSaida + '_TalQ2D.txt'
    with open(nome, 'ab') as f:
        np.savetxt(f, vetSaida.reshape(1,-1), fmt='%0.4f', delimiter='\t')