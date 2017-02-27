# DFA-2D

Command | Arguments description
------------ | -------------
-dI | Diretório de Entrada dos dados
-dO | Diretório de Saída dos dados
-dt | Delimitador dos arquivos de entrada (use "\n" para cada dado em uma linha do arquivo)
-f  | Nome do arquivo de saída, que contém as informações : nome do arquivo, valor do alpha, tempo de processamento

O DFA-2D gera um arquivo de saída que contém as informações : nome do arquivo, valor do alpha, tempo de processamento de cada arquivo do diretório de entrada.
Também gerado o arquivo com extensão "flutuacao_.txt", onde cada linha refere-se a flutuação log10(F(s)) de cada arquivo processado. O valor de s varia de 6 a n/4.

####Example
	python DFA_2D/main.py -dI Data/ruidos/ -dO Data/ruidos -dt "\n" -f marrom.txt
