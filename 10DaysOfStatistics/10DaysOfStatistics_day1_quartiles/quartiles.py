import math
quartils = [0, 0, 0]

#3 4 4 4 7 10  12 12 14 16 17 18
#[3, 4, 4, 4, 7] 10 12 [ 12, 14, 16, 17, 18]
def Quartils(lista, n, call):

    lista.sort()
    if call == 0:

        if len(lista) % 2 != 0:
            q1 = int((len(lista) - 1) / 2)
            quartils[0] = Quartils(lista[:q1], len(lista[:q1]), 1)

            q2 = int((len(lista) - 1) / 2)
            quartils[2] = Quartils(lista[q2+1:q2 * q2], int((len(lista) - 1) / 2), 1)

            quartils[1]  = int(lista[int((len(lista) - 1) / 2)])

        else:
            posicao_meio = int(len(lista) / 2) - 1
            val1 = lista[posicao_meio]
            val2 = lista[posicao_meio + 1]
            quartils[1] = int(( val1 + val2 ) / 2)

            q1 = int(len(lista) / 2)
            quartils[0] = Quartils(lista[:q1], len(lista[:q1]), 1)

            q2 = int((len(lista) / 2))
            quartils[2] = Quartils(lista[q2:], int(len(lista) / 2), 1)


        return quartils

    else:

        if len(lista) % 2 != 0:
            lista.sort()
            mediana  = int(lista[int((len(lista) - 1) / 2)])

        else:
            lista.sort()
            posicao_meio = int(len(lista) / 2) - 1
            val1 = lista[posicao_meio]
            val2 = lista[posicao_meio + 1]
            mediana = ( val1 + val2 ) / 2


        return math.ceil(mediana)

n = int(input())

lista = list(map(int, input().strip().split(' ')))

result = Quartils(lista, n, 0)

for resultado in result:
    print (resultado)
