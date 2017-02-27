import numpy as np
from scipy import stats
import robustLastSquare as fit
import time

########################DFA 2D####################################################################
def dfa2d(mat, grau):
    inicio = time.time()
    [l, c] = np.shape(mat)
    tam = np.minimum(l, c)
    mat = np.reshape(mat, (tam, tam))
    escalas = int(tam/4)
    vetoutput = np.zeros(shape=(escalas - 5, 2))
    k=0
    s = 6
    while (s < escalas + 1):
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
        fs = np.sqrt(np.mean(vetvar))
        vetoutput[k, 0] = s
        vetoutput[k,1] = fs
        k = k + 1
        s = s + 1
    vetoutput = np.log10(vetoutput)
    x = vetoutput[:, 0]
    y = vetoutput[:, 1]
    slope, _, _, _, _ = stats.linregress(x, y)
    fim = time.time()
    print(slope)
    return (slope, fim-inicio, y.reshape(1,-1))
