from grafo import Grafo
from algoritmosDeOrdenacao import *
from utils import *

'''
Implemente o algoritmo de ordenação no arquivo algoritmosDeOrdenacao.py
Instruções básicas de como fazer a implementação estão no arquivo algoritmosDeOrdenacao.py
'''

if __name__ == "__main__":
    print('[1] 7 vertices\n[2] 100 vertices\n[3] 1000 vertices\n[4] 10000 vertices\n[5] 100000 vertices')
    ver = int(input('Digite a quantidade de vertices q vc deseja ordenar: '))
    while ver < 1 or ver > 5:
        ver = int(input('Digite a quantidade de vertices q vc deseja ordenar: '))

    if ver == 1:
        arquivoJson = '../grafos/7vertices.json'
        tam = int(7)

    elif ver == 2:
        arquivoJson = '../grafos/100vertices.json'
        tam = int(100)

    elif ver == 3:
        arquivoJson = '../grafos/1000vertices.json'
        tam = int(1000)

    elif ver == 4:
        arquivoJson = '../grafos/10000vertices.json'
        tam = int(10000)

    else:
        arquivoJson = '../grafos/100000vertices.json'
        tam = int(100000)

    print("[1] QuickSort\n[2] MergeSort\n[3] InsertSort\n[4] Quicksort + InsertSort Parcial\n"
                "[5] Quicksort + InsertSort Final\n[6] MergeSort + InsertSort Parcial\n[7] MergeSort + InsertSort Final\n")

    alg = int(input('Digite qual algoritmo de ordenção usar: '))
    while alg < 1 or alg > 7:
        alg = int(input('Digite qual algoritmo de ordenção usar: '))

    if alg == 1:
        algoritimoDeOrdenacao = QuickSort()

    elif alg == 2:
        algoritimoDeOrdenacao = MergeSort()

    elif alg == 3:
        algoritimoDeOrdenacao = InsertSort()

    elif alg == 4:
        algoritimoDeOrdenacao = QuicksortInsertSortP()

    elif alg == 5:
        algoritimoDeOrdenacao = QuicksortInsertSortF()

    elif alg == 6:
        algoritimoDeOrdenacao = MergeSortInsertSortP()

    else:
        algoritimoDeOrdenacao = MergeSortInsertSortF()

    arquivoDeSaida = '../arvores_geradas/mst7Vertices.txt'

    grafo = Grafo()
    grafo.estabelecerAlgoritmoDeOrdencao(algoritimoDeOrdenacao)
    grafo.carregarGrafo(arquivoJson)

    print(grafo)

    arvoreGeradoraMinima = grafo.executarKruskal()
    SalvarArvoreGeradoraMinimaEmArquivo(arquivoDeSaida, arvoreGeradoraMinima)

