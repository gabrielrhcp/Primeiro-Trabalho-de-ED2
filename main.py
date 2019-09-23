from grafo import Grafo
import time
from algoritmosDeOrdenacao import *
from utils import *
import datetime
'''
Implemente o algoritmo de ordenação no arquivo algoritmosDeOrdenacao.py
Instruções básicas de como fazer a implementação estão no arquivo algoritmosDeOrdenacao.py
'''

if __name__ == "__main__":

    ''' trecho original para definições
    algoritimoDeOrdenacao = InsertionSort()
    arquivoJson = '../grafos/7vertices.json'
    '''
    # trecho alterado para as definições

    '''Apresentção e escolha do numero de vertices - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Um arquivo de grafos foi definido como padrão para prevenir erros
    variaveis 'strini' e 'strfin' são usadas para gerar um nome para o arquivo de saida com base no arquivo de entrada
    elas serão concatenadas
    '''

    strini = ''
    strfin = '_Vertices_Output.txt'
    print("Escolha a quantidade de vertices:\n")
    ver = input("1 - 7 vertices\n2 - 100 vertices\n3 - 1000 vertices\n4 - 10000 vertices\n5 - 100000 vertices\n")

    if int(ver) == 1:
        arquivoJson = '../grafos/7vertices.json'
        strini = '7'

    elif int(ver) == 2:
        arquivoJson = '../grafos/100vertices.json'
        strini = '100'

    elif int(ver) == 3:
        arquivoJson = '../grafos/1000vertices.json'
        strini = '1000'

    elif int(ver) == 4:
        arquivoJson = '../grafos/10000vertices.json'
        strini = '10000'

    elif int(ver) == 5:
        arquivoJson = '../grafos/100000vertices.json'
        strini = '100000'

    else:
        # entrada padrão
        print("Nenhum tamanho de entrada apresentado foi selecionado")
        print("Neste caso o padrão será 100\n")
        arquivoJson = '../grafos/100vertices.json'
        strini = '100'

    '''
    Apresentação e escolha do algoritimo de ordenação - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Um algoritimo foi definido como padrão para não ocasionar erros
    '''

    print("Escolha o algoritmo de ordenação:\n")
    alg = input("1 - QuickSort\n2 - MergeSort\n3 - InsertionSort\n4 - QuickSort + InsertionSort Parcial\n"
                "5 - QuickSort + InsertionSort Final\n6 - MergeSort + InsertionSort Parcial\n7 - MergeSort + InsertionSort Final\n")

    if int(alg) == 1:
        algoritimoDeOrdenacao = QuickSort()
    elif int(alg) == 2:
        algoritimoDeOrdenacao = Mergesort()
    elif int(alg) == 3:
        algoritimoDeOrdenacao = InsertionSort()
    elif int(alg) == 4:
        algoritimoDeOrdenacao = QuickSortInsertionSortParcial()
    elif int(alg) == 5:
        algoritimoDeOrdenacao = QuickSortInsertionSortFinal()
    elif int(alg) == 6:
        algoritimoDeOrdenacao = MergesortInsertionSortParcial()
    elif int(alg) == 7:
        algoritimoDeOrdenacao = MergesortInsertionSortFinal()
        '''
        Shellsort tem duas implementações: uma com uma sequencia para 'h' 
        já definida e outra para um intervalo 'gap' definido pelo usuario
        '''

    # elif int(alg) == 4:

    else:
        # algoritimo padrão
        print("Nenhum algoritmo apresentado foi selecionado")
        print("Neste caso será usado o InsertionSort definido como padrão\n")
        algoritimoDeOrdenacao = InsertionSort()

    arquivoDeSaida = '../arvores_geradas/' + strini + strfin # concatenação das strings para gerar um nome para o arquivo de saida

    print("algoritmo iniciou em: ", datetime.datetime.now())
    # fim trecho alterado

    inicio = time.time()

    grafo = Grafo()
    grafo.estabelecerAlgoritmoDeOrdencao(algoritimoDeOrdenacao)
    grafo.carregarGrafo(arquivoJson)
    arvoreGeradoraMinima = grafo.executarKruskal()
    SalvarArvoreGeradoraMinimaEmArquivo(arquivoDeSaida, arvoreGeradoraMinima)

    fim = time.time()

    print(fim - inicio)
