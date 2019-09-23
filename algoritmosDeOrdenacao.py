'''
Introdução:
- Implementar algoritmo de ordenação que receba uma colecão
- A coleção é uma lista de arestas
- Para comparar o peso as arestas entre dois item da coleção basta usar a chave 'weight' (peso)

Exemplos:
- Modo convencional
colecao[i] operador de comparacao colecao[j]
colecao[i] < colecao[j]

- Modo que você vai usar
int(colecao[i]['weight']) operador de comparacao int(colecao[j]['weight'])
int(colecao[i]['weight']) < int(colecao[j]['weight'])

É nescessário converter o valor pra Interger no momento da comparação a fim de evitar erros
'''


# Sua classe algoritmo de ordenação precisar ter um método ordenar
class QuickSort(object):
    def ordenar(self, colecao):



        return colecao

class MergeSort(object):
    def ordenar(self, lista):


        return lista

class InsertSort(object):
    def ordenar(self, lista):
        print(lista)
        for i in range(1, len(lista)):
            key = lista[i]
            j = i - 1
            while j >= 0 and int(key['weight']) < int(lista[j]['weight']):
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = key
        print(lista)
        return lista

class QuicksortInsertSortP(object):
    def ordenar(self, colecao):

        return colecao

class QuicksortInsertSortF(object):
    def ordenar(self, colecao):



        return colecao

class MergeSortInsertSortP(object):
    def ordenar(self, colecao):



        return colecao

class MergeSortInsertSortF(object):
    def ordenar(self, colecao):



        return colecao