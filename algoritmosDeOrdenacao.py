import math
import time
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
    def quick(self, colecao, l, r):
        i = l
        j = r
        p = colecao[l + (r - l) // 2]
        while i <= j:
            while int(colecao[i]['weight']) < int(p['weight']):
                i += 1
            while int(colecao[j]['weight']) > int(p['weight']):
                j -= 1

            if i <= j:
                colecao[i], colecao[j] = colecao[j], colecao[i]
                i += 1
                j -= 1

        if l < j:
            self.quick(colecao, l, j)

        if i < r:
            self.quick(colecao, i, r)

        return colecao

    def ordenar(self, colecao):
        print(colecao)
        inicio = float(time.time())

        self.quick(colecao, 0, len(colecao) - 1)
        print(colecao)
        fim = float(time.time())

        print(fim - inicio)
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
        inicio = float(time.time())

        self.merge_sort(colecao)
        print(colecao)
        fim = float(time.time())

        print(fim - inicio)
        return colecao

class InsertionSort(object):
    def ordenar(self, colecao):
        inicio = float(time.time())

        print(colecao)
        for i in range(1, len(colecao)):
            chave = colecao[i]
            k = i
            while k > 0 and int(chave['weight']) < int(colecao[k - 1]['weight']):
                colecao[k] = colecao[k - 1]
                k -= 1
            colecao[k] = chave
        print(colecao)
        fim = float(time.time())

        print(fim-inicio)
        return colecao

class QuickSortInsertionSortParcial(object):

    def shell(self, colecao):
        h = 1
        n = len(colecao)
        while h > 0:
            for i in range(h, n):
                c = colecao[i]
                j = i
                while j >= h and int(c["weight"]) < int(colecao[j - h]["weight"]):
                    colecao[j] = colecao[j - h]
                    j = j - h
                    colecao[j] = c
            h = int(h / 2.2)
        return colecao

    def select(self, colecao):
        for i in range(len(colecao) - 1):
            menor = i
            for j in range(i + 1, len(colecao)):
                if int(colecao[menor]['weight']) > int(colecao[j]['weight']):  # !!!
                    menor = j
            if menor != i:
                vaux = colecao[menor]
                colecao[menor] = colecao[i]
                colecao[i] = vaux

        return colecao

    def insertion(self, colecao):
        for i in range(1, len(colecao)):
            chave = colecao[i]
            k = i
            while k > 0 and int(chave['weight']) < int(colecao[k - 1]['weight']):
                colecao[k] = colecao[k - 1]
                k -= 1
            colecao[k] = chave

    def quick(self, colecao, l, r, L, x):
        i = l
        j = r
        p = colecao[l + (r - l) // 2]
        if L < r-l+1:
            while i <= j:
                while int(colecao[i]['weight']) < int(p['weight']) :
                    i += 1
                while int(colecao[j]['weight']) > int(p['weight']) :
                    j -= 1

                if i <= j:
                    colecao[i], colecao[j] = colecao[j], colecao[i]
                    i += 1
                    j -= 1

            if l < j:
                self.quick(colecao, l, j, L, x)

            if i < r:
                self.quick(colecao, i, r, L, x)

        else:
            aux = colecao[l:r]
            if x == 1:
                self.insertion(aux)
            elif x == 2:
                self.select(aux)
            else:
                self.shell(aux)
            i = 0
            for x in range(l,r):
                colecao[x] = aux[i]
                i += 1

        return colecao


    def ordenar(self, colecao):
        print(colecao)
        L = int(input('Digite L: '))
        x = int(input('[1] Insertion\n[2] Selection\n[3] Shell\nDigite por qual ordenar: '))
        inicio = float(time.time())

        self.quick(colecao, 0, len(colecao)-1, L, x)
        print(colecao)
        fim = float(time.time())

        print(fim - inicio)
        return colecao


class QuickSortInsertionSortFinal(object):

    def shell(self, colecao):
        h = 1
        n = len(colecao)
        while h > 0:
            for i in range(h, n):
                c = colecao[i]
                j = i
                while j >= h and int(c["weight"]) < int(colecao[j - h]["weight"]):
                    colecao[j] = colecao[j - h]
                    j = j - h
                    colecao[j] = c
            h = int(h / 2.2)
        return colecao

    def select(self, colecao):
        for i in range(len(colecao) - 1):
            menor = i
            for j in range(i + 1, len(colecao)):
                if int(colecao[menor]['weight']) > int(colecao[j]['weight']):  # !!!
                    menor = j
            if menor != i:
                vaux = colecao[menor]
                colecao[menor] = colecao[i]
                colecao[i] = vaux
        return colecao

    def insertion(self, colecao):
        for i in range(1, len(colecao)):
            chave = colecao[i]
            k = i
            while k > 0 and int(chave['weight']) < int(colecao[k - 1]['weight']):
                colecao[k] = colecao[k - 1]
                k -= 1
            colecao[k] = chave

    def quick(self, colecao, l, r, L):
        i = l
        j = r
        p = colecao[l + (r - l) // 2]
        if L < r - l + 1:
            while i <= j:
                while int(colecao[i]['weight']) < int(p['weight']):
                    i += 1
                while int(colecao[j]['weight']) > int(p['weight']):
                    j -= 1

                if i <= j:
                    colecao[i], colecao[j] = colecao[j], colecao[i]
                    i += 1
                    j -= 1

            if l < j:
                self.quick(colecao, l, j, L)

            if i < r:
                self.quick(colecao, i, r, L)

        return colecao

    def ordenar(self, colecao):
        print(colecao)
        L = int(input('Digite L: '))
        x = int(input('[1] Insertion\n[2] Selection\n[3] Shell\nDigite por qual ordenar: '))
        inicio = float(time.time())

        self.quick(colecao, 0, len(colecao) - 1, L)
        print(colecao)
        if x == 1:
            self.insertion(colecao)
        elif x == 2:
            self.select(colecao)
        else:
            self.shell(colecao)
        print(colecao)
        fim = float(time.time())

        print(fim - inicio)
        return colecao

class MergesortInsertionSortParcial(object):

    def shell(self, colecao):
        h = 1
        n = len(colecao)
        while h > 0:
            for i in range(h, n):
                c = colecao[i]
                j = i
                while j >= h and int(c["weight"]) < int(colecao[j - h]["weight"]):
                    colecao[j] = colecao[j - h]
                    j = j - h
                    colecao[j] = c
            h = int(h / 2.2)
        return colecao

    def select(self, colecao):
        for i in range(len(colecao) - 1):
            menor = i
            for j in range(i + 1, len(colecao)):
                if int(colecao[menor]['weight']) > int(colecao[j]['weight']):  # !!!
                    menor = j;
            if menor != i:
                vaux = colecao[menor]
                colecao[menor] = colecao[i]
                colecao[i] = vaux
        return colecao

    def insertion(self, colecao):
        for i in range(1, len(colecao)):
            chave = colecao[i]
            k = i
            while k > 0 and int(chave['weight']) < int(colecao[k - 1]['weight']):
                colecao[k] = colecao[k - 1]
                k -= 1
            colecao[k] = chave

    def merge_sort(self, colecao, L, x):
        if len(colecao) > L:
            meio = int(len(colecao) / 2)
            esqpart = colecao[:meio]  # cortando colecao no meio e atribuindo a primeira metada a esqpart
            dirpart = colecao[meio:]  # segunda metade a dirpart
            self.merge_sort(esqpart, L, x)
            self.merge_sort(dirpart, L, x)
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
            if x == 1:
                self.insertion(colecao)
            elif x == 2:
                self.select(colecao)
            else:
                self.shell(colecao)

        return colecao

    def ordenar(self, colecao):
        print(f'{colecao}')
        L = int(input('Digite L: '))
        x = int(input('[1] Insertion\n[2] Selection\n[3] Shell\nDigite por qual ordenar: '))
        inicio = float(time.time())

        self.merge_sort(colecao, L, x)
        print(f'{colecao}')
        fim = float(time.time())

        print(fim - inicio)
        return colecao

class MergesortInsertionSortFinal(object):

    def shell(self, colecao):
        h = 1
        n = len(colecao)
        while h > 0:
            for i in range(h, n):
                c = colecao[i]
                j = i
                while j >= h and int(c["weight"]) < int(colecao[j - h]["weight"]):
                    colecao[j] = colecao[j - h]
                    j = j - h
                    colecao[j] = c
            h = int(h / 2.2)
        return colecao

    def select(self, colecao):
        for i in range(len(colecao) - 1):
            menor = i
            for j in range(i + 1, len(colecao)):
                if int(colecao[menor]['weight']) > int(colecao[j]['weight']):  # !!!
                    menor = j;
            if menor != i:
                vaux = colecao[menor]
                colecao[menor] = colecao[i]
                colecao[i] = vaux
        return colecao

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
        print(colecao)
        L = int(input('Digite L: '))
        x = int(input('[1] Insertion\n[2] Selection\n[3] Shell\nDigite por qual ordenar: '))
        inicio = float(time.time())

        self.merge_sort(colecao, L)
        print(colecao)
        if x == 1:
            self.insertion(colecao)
        elif x == 2:
            self.select(colecao)
        else:
            self.shell(colecao)
        print(colecao)
        fim = float(time.time())

        print(fim - inicio)
        return colecao