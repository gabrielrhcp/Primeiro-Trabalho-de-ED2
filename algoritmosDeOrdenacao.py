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
            idx_min = i
            for j in range(i + 1, len(colecao)):
                if int(colecao[idx_min]['weight']) > int(colecao[j]['weight']):  # !!!
                    idx_min = j;
            if idx_min != i:
                vaux = colecao[idx_min]
                colecao[idx_min] = colecao[i]
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
        self.merge_sort(colecao, L, x)
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
            idx_min = i
            for j in range(i + 1, len(colecao)):
                if int(colecao[idx_min]['weight']) > int(colecao[j]['weight']):  # !!!
                    idx_min = j;
            if idx_min != i:
                vaux = colecao[idx_min]
                colecao[idx_min] = colecao[i]
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
        self.merge_sort(colecao, L)
        print(colecao)
        x = int(input('[1] Insertion\n[2] Selection\n[3] Shell\nDigite por qual ordenar: '))
        if x == 1:
            self.insertion(colecao)
        elif x == 2:
            self.select(colecao)
        else:
            self.shell(colecao)
        print(colecao)
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
            idx_min = i
            for j in range(i + 1, len(colecao)):
                if int(colecao[idx_min]['weight']) > int(colecao[j]['weight']):  # !!!
                    idx_min = j;
            if idx_min != i:
                vaux = colecao[idx_min]
                colecao[idx_min] = colecao[i]
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
        while i <= j:
            while int(colecao[i]['weight']) < int(p['weight']) :
                i += 1
            while int(colecao[j]['weight']) > int(p['weight']) :
                j -= 1

            if i <= j:
                colecao[i], colecao[j] = colecao[j], colecao[i]
                i += 1
                j -= 1

        if L < j-l+1:  # sort left list
            self.quick(colecao, l, j, L, x)
        else:
            if x == 1:
                self.insertion(colecao)
            elif x == 2:
                self.select(colecao)
            else:
                self.shell(colecao)

        if L < r-i+1:  # sort right list
            self.quick(colecao, i, r, L, x)
        else:
            if x == 1:
                self.insertion(colecao)
            elif x == 2:
                self.select(colecao)
            else:
                self.shell(colecao)
        return colecao

    def ordenar(self, colecao):
        print(colecao)
        L = int(input('Digite L: '))
        x = int(input('[1] Insertion\n[2] Selection\n[3] Shell\nDigite por qual ordenar: '))
        self.quick(colecao, 0, len(colecao)-1, L, x)
        print(colecao)
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
            idx_min = i
            for j in range(i + 1, len(colecao)):
                if int(colecao[idx_min]['weight']) > int(colecao[j]['weight']):  # !!!
                    idx_min = j;
            if idx_min != i:
                vaux = colecao[idx_min]
                colecao[idx_min] = colecao[i]
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
        while i <= j:
            while int(colecao[i]['weight']) < int(p['weight']):
                i += 1
            while int(colecao[j]['weight']) > int(p['weight']):
                j -= 1

            if i <= j:
                colecao[i], colecao[j] = colecao[j], colecao[i]
                i += 1
                j -= 1

        if L < j - l + 1:  # sort left list
            self.quick(colecao, l, j, L)

        if L < r - i + 1:  # sort right list
            self.quick(colecao, i, r, L)

        return colecao

    def ordenar(self, colecao):
        print(colecao)
        L = int(input('Digite L: '))
        self.quick(colecao, 0, len(colecao) - 1, L)
        print(colecao)
        x = int(input('[1] Insertion\n[2] Selection\n[3] Shell\nDigite por qual ordenar: '))
        if x == 1:
            self.insertion(colecao)
        elif x == 2:
            self.select(colecao)
        else:
            self.shell(colecao)
        print(colecao)
        return colecao