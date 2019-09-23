import math
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
class InsertionSort(object):
    def ordenar(self, colecao):
        print(colecao)
        for i in range(1, len(colecao)):
            chave = colecao[i]
            k = i
            while k > 0 and int(chave['weight']) < int(colecao[k - 1]['weight']):
                colecao[k] = colecao[k - 1]
                k -= 1
            colecao[k] = chave
        print(colecao)
        return colecao

class SelectionSort(object):
    def ordenar(self, colecao):
        for i in range(len(colecao) - 1):
            idx_min = i
            for j in range(i + 1, len(colecao)):
                if int(colecao[idx_min]['weight']) > int(colecao[j]['weight']):  # !!!
                    idx_min = j;
            if idx_min != i:
                vaux = colecao[idx_min]
                colecao[idx_min] = colecao[i]
                colecao[i] = vaux
        return colecao

class ShellSort(object):
    def ordenar(self, colecao):
        print("Escolha entre os dois metodos:\n")
        escolha = input("1 - H\n2 - GAP\n")
        if int(escolha) == 1:
            h = 1
            for h in range(h, len(colecao), (3 * h) - 1):
                h = int(h)
            while h > 0:
                h = math.ceil((h - 1) / 3)
                for i in range(h, len(colecao)):
                    aux = colecao[i]
                    j = i
                    while j >= h and int(colecao[j - h]['weight']) > int(aux['weight']):
                        colecao[j] = colecao[j - h]
                        j = j - h
                        if j < h:
                            break
                    colecao[j] = aux
            return colecao
        elif int(escolha) == 2:
            # caso seja escolhido o GAP o usuario escolhe uma distancia que será descrementada
            distancia = input("Indique a distancia inicial:\n")
            if int(distancia) > len(colecao):
                print("distancia maior que o tamanho da coleção\n")
                print("Neste caso distancia por padrão será metade do tamanho da coleção\n")
                distancia = len(colecao) / 2
            gap = int(distancia)
            while gap > 0:
                for i in range(gap, len(colecao)):
                    aux = colecao[i]
                    j = i
                    while j >= gap and int(colecao[j - gap]['weight']) > int(aux['weight']):
                        colecao[j] = colecao[j - gap]
                        j -= gap

                    colecao[j] = aux
                gap -= 1
            return colecao
        else:
            print("Nenhum metodo selecionado")
            return None

class QuickSort(object):
    def particaoR(self, colecao, ini, fin):
        i = int(ini)
        k = int(fin) - 1
        pivo = colecao[fin]
        concluido = False  # muda de estado quando i e f (k) se cruzam
        while not concluido:
            while i < k and int(colecao[i]['weight']) <= int(pivo['weight']):
                i += 1
            while int(colecao[k]['weight']) >= int(pivo['weight']) and k >= i:
                k -= 1
            if k < i:
                concluido = True
            else:
                temp = colecao[i]
                colecao[i] = colecao[k]
                colecao[k] = temp
                k -= 1
                i += 1
        temp = colecao[fin]
        colecao[fin] = colecao[i]
        colecao[i] = temp
        return i

    def particaoL(self, colecao, ini, fin):
        i = int(ini) + 1
        k = int(fin)
        pivo = colecao[ini]
        concluido = False
        while not concluido:
            while i < k and int(colecao[i]['weight']) <= int(pivo['weight']):
                i += 1
            while int(colecao[k]['weight']) >= int(pivo['weight']) and k >= i:
                k -= 1
            if k < i:
                concluido = True
            else:
                temp = colecao[i]
                colecao[i] = colecao[k]
                colecao[k] = temp
                k -= 1
                i += 1
        temp = colecao[ini]
        colecao[ini] = colecao[k]
        colecao[k] = temp
        return k

    def particaoM(self, colecao, ini, fin):
        meio = int((fin + ini)/2)
        i = int(colecao[ini]['weight'])
        m = int(colecao[meio]['weight'])
        f = int(colecao[fin]['weight'])

        idxm = 0 # indice do mediano
        if i < m:
            if m < f:
                idxm = meio
            else:
                if i < f:
                    idxm = fin
                else:
                    idxm = ini
        else:
            if f < m:
                idxm = meio
            else:
                if f < i:
                    idxm = fin
                else:
                    idxm = ini
        aux = colecao[idxm]
        colecao[idxm] = colecao[fin]
        colecao[fin] = aux
        return self.particaoR(colecao, ini, fin)

    def quickSortR(self, colecao, ini, fin):
        if int(ini) < int(fin):
            par = self.particaoR(colecao, ini, fin)
            self.quickSortR(colecao, ini, par - 1)
            self.quickSortR(colecao, par + 1, fin)
            return colecao

    def quickSortL(self, colecao, ini, fin):
        if int(ini) < int(fin):
            par = self.particaoL(colecao, ini, fin)
            self.quickSortL(colecao, ini, par - 1)
            self.quickSortL(colecao, par + 1, fin)
            return colecao

    def quickSortM(self, colecao, ini, fin):
        if int(ini) < int(fin):
            par = self.particaoM(colecao, ini, fin)
            self.quickSortM(colecao, ini, par - 1)
            self.quickSortM(colecao, par + 1, fin)
            return colecao

    def ordenar(self, colecao):
        print(colecao)
        print("Escolha o pivô:")
        escolha = input("1 - pivô a direita\n2 - pivô a esquerda\n3 - pivô mediano\n")
        if int(escolha) == 1:
            self.quickSortR(colecao, 0, len(colecao) - 1)
            print(colecao)
            return colecao
        if int(escolha) == 2:
            self.quickSortL(colecao, 0, len(colecao) - 1)
            print(colecao)
            return colecao
        if int(escolha) == 3:
            self.quickSortM(colecao, 0, len(colecao) - 1)
            print(colecao)
            return colecao

class MergesortInsertionSortParcial(object):

    def insertion(self, colecao):
        for i in range(1, len(colecao)):
            chave = colecao[i]
            k = i
            while k > 0 and int(chave['weight']) < int(colecao[k - 1]['weight']):
                colecao[k] = colecao[k - 1]
                k -= 1
            colecao[k] = chave

    def merge_sort(self, colecao, L):
        if len(colecao) > L:
            meio = int(len(colecao) / 2)
            esqpart = colecao[:meio]  # cortando colecao no meio e atribuindo a primeira metada a esqpart
            dirpart = colecao[meio:]  # segunda metade a dirpart
            self.merge_sort(esqpart, L)
            self.merge_sort(dirpart, L)
            i = 0  # indice inicial esqpart
            j = 0  # indice inicial dirpart
            k = 0  # indice inicial da colecao

            while i < len(esqpart) and j < len(dirpart):
                if int(esqpart[i]['weight']) < int(dirpart[j]['weight']):
                    colecao[k] = esqpart[i]
                    i += 1
                else:
                    colecao[k] = dirpart[j]
                    j += 1
                k += 1
            while i < len(esqpart):
                colecao[k] = esqpart[i]
                i += 1
                k += 1
            while j < len(dirpart):
                colecao[k] = dirpart[j]
                j += 1
                k += 1
        else:
            self.insertion(colecao)

        return colecao

    def ordenar(self, colecao):
        print(f'{colecao}')
        L = int(input('Digite L: '))
        self.merge_sort(colecao, L)
        print(f'{colecao}')
        return colecao

class Mergesort(object):
    def merge_sort(self, colecao):
        if len(colecao) > 1:
            meio = int(len(colecao) / 2)
            esqpart = colecao[:meio] # cortando colecao no meio e atribuindo a primeira metada a esqpart
            dirpart = colecao[meio:] # segunda metade a dirpart
            self.merge_sort(esqpart)
            self.merge_sort(dirpart)
            i = 0 # indice inicial esqpart
            j = 0 # indice inicial dirpart
            k = 0 # indice inicial da colecao

            while i < len(esqpart) and j < len(dirpart):
                if int(esqpart[i]['weight']) < int(dirpart[j]['weight']):
                    colecao[k] = esqpart[i]
                    i += 1
                else:
                    colecao[k] = dirpart[j]
                    j += 1
                k += 1
            while i < len(esqpart):
                colecao[k] = esqpart[i]
                i += 1
                k += 1
            while j < len(dirpart):
                colecao[k] = dirpart[j]
                j += 1
                k += 1
        return colecao

    def ordenar(self, colecao):
        print(colecao)
        self.merge_sort(colecao)
        print(colecao)
        return colecao

class HeapSort(object):
    def heapfy(self, colecao, n, r):
        maior = r
        esq = 2 * r + 1
        dir = 2 * r + 2
        if esq < n and int(colecao[r]['weight']) < int(colecao[esq]['weight']):
            maior = esq
        if dir < n and int(colecao[maior]['weight']) < int(colecao[dir]['weight']):
            maior = dir
        if maior != r:
            colecao[r], colecao[maior] = colecao[maior], colecao[r]
            self.heapfy(colecao, n, maior)

    def heapsort(self, colecao):
        n = len(colecao)
        for i in range(n, -1, -1):
            self.heapfy(colecao, n, i)
        for i in range(n-1, 0, -1):
            colecao[i], colecao[0] = colecao[0], colecao[i]
            self.heapfy(colecao, i, 0)
        return colecao

    def ordenar(self, colecao):
        return self.heapsort(colecao)

class CountSort(object):
    def maxval(self, colecao):
        max = colecao[0]
        for i in range(len(colecao) - 1):
            if int(colecao[i]['weight']) > int(max['weight']):
                max = colecao[i]
        return max

    def ordenar(self, colecao):
        max = self.maxval(colecao)
        maxvalue = int(max['weight']) + 1
        count = [0] * maxvalue
        result = [None] * len(colecao)
        i = 0
        while i < len(colecao) - 1:
            count[int(colecao[i]['weight'])] = count[int(colecao[i]['weight'])] + 1
            i += 1
        for j in range(1, int(maxvalue)):
            count[j] = count[j] + count[j - 1]
        k = len(colecao) - 1
        while k > 0:
            result[count[int(colecao[k]['weight'])]] = colecao[k]
            count[int(colecao[k]['weight'])] -= 1
            k -= 1
        outcome = []
        for a in range(len(result) - 1):
            if result[a] != None:
                outcome.append(result[a])
        return outcome

class MergesortInsertionSortFinal(object):

    def insertion(self, colecao):
        for i in range(1, len(colecao)):
            chave = colecao[i]
            k = i
            while k > 0 and int(chave['weight']) < int(colecao[k - 1]['weight']):
                colecao[k] = colecao[k - 1]
                k -= 1
            colecao[k] = chave

    def merge_sort(self, colecao, L):
        if len(colecao) > L:
            meio = int(len(colecao) / 2)
            esqpart = colecao[:meio]  # cortando colecao no meio e atribuindo a primeira metada a esqpart
            dirpart = colecao[meio:]  # segunda metade a dirpart
            self.merge_sort(esqpart, L)
            self.merge_sort(dirpart, L)
            i = 0  # indice inicial esqpart
            j = 0  # indice inicial dirpart
            k = 0  # indice inicial da colecao

            while i < len(esqpart) and j < len(dirpart):
                if int(esqpart[i]['weight']) < int(dirpart[j]['weight']):
                    colecao[k] = esqpart[i]
                    i += 1
                else:
                    colecao[k] = dirpart[j]
                    j += 1
                k += 1
            while i < len(esqpart):
                colecao[k] = esqpart[i]
                i += 1
                k += 1
            while j < len(dirpart):
                colecao[k] = dirpart[j]
                j += 1
                k += 1
        return colecao

    def ordenar(self, colecao):
        print(f'{colecao}')
        L = int(input('Digite L: '))
        self.merge_sort(colecao, L)
        print(f'{colecao}')
        self.insertion(colecao)
        print(f'{colecao}')
        return colecao