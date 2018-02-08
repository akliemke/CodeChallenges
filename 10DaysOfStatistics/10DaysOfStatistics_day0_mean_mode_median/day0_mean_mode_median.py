import sys

def media(lista, n):

    media = sum(lista)/n

    return print( '%.1f' % media)

def mediana(lista, n):

    if len(lista) % 2 != 0:
        lista.sort()
        mediana  = int(lista[int((len(lista) - 1) / 2)])
    else:
        lista.sort()
        posicao_meio = int(len(lista) / 2) - 1
        val1 = lista[posicao_meio]
        val2 = lista[posicao_meio + 1]
        mediana = ( val1 + val2 ) / 2

    return print('%.1f' % mediana)

def moda(lista, n):

    lista.sort()
    lista_cont = []

    for item in lista:
        x = 0
        for i in range(n):
            if lista[i] == item:
                x = x + 1
        lista_cont.append(x)

    if sum(lista_cont) == n:
        return print(lista[0])
    else:
        maior = 0

        for y in range(n):
            if lista[y] > maior:
                maior = lista[y]
                pos = y

    return print (lista[lista_cont.index(max(lista_cont))])

n = int(input())

lista = list(map(int, input().strip().split(' ')))
media(lista, n)
mediana(lista, n)
moda(lista, n)
