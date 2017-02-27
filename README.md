# DFA-1D

Command | Arguments description
------------ | -------------
-dI | Diretório de Entrada dos dados
-dO | Diretório de Saída dos dados
-dt | Delimitador dos arquivos de entrada (use "\n" para cada dado em uma linha do arquivo)
-f  | Nome do arquivo de saída, que contém as informações : nome do arquivo, valor do alpha, tempo de processamento

O DFA-1D também gera o arquivo com extensão "flutuacao_.txt" para cada arquivo processado. A primeira coluna do arquivo refere-se ao log10(s) e a segunda, ao log10(F(s))


####Example
	python DFA_1D/main.py -dI Data/ruidos/ -dO Data/ruidos -dt "\n" -f marrom.txt
