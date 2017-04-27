import numpy as np
import codecs
import os
import DFA2D as dfa
import MF_DFA2D as mdfa
import argparse


def main(dirEntrada, dirSaida, delimiter, arq):
    flutuacao = dirSaida + 'flutuacao_.txt'
    s = ""
    a = [dirSaida, arq[:-1] + '.txt']
    arqSaida = s.join(a)
    arqs = os.listdir(dirEntrada)
    #arqs = sorted(arqs, key=lambda x: int((x.split('.')[0])))
    for file in arqs:
        if file.endswith('.txt'):
            print(file)
            with codecs.open(dirEntrada + file, encoding='utf-8-sig') as f:
                m = np.loadtxt(f, delimiter= delimiter)
            mdfa.mfdfa2d(m, 1, dirSaida, file)
            # alfa, tempo, F = dfa.dfa2d(m, 1)
            # with open(flutuacao, 'ab') as f:
            #     np.savetxt(f, F, fmt='%0.4f', delimiter='\t')
            # dt = np.dtype(str, 10)
            # b = np.array([file, alfa, tempo], dtype=dt)
            # b = np.reshape(b, newshape=(1, 3))
            # with open(arqSaida, 'ab') as f:
            #     np.savetxt(f, b, fmt='%10s')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DFA 2D')
    parser.add_argument('-dI','--InputDirectory', type=str, help='Dataset Directory', required=True)
    parser.add_argument('-dO', '--OutputDirectory', type=str, help='Dataset Directory', required=True)
    parser.add_argument('-dt','--Delimiter', type=str, help='String that delimiter the values in file', required=True)
    parser.add_argument('-f','--File', type=str, help='name of the output file', required=False)
    args = parser.parse_args()
    main(args.InputDirectory, args.OutputDirectory, args.Delimiter, args.File)
