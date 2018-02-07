
def MediaPonderada(lista_superior, lista_inferior, n):
    resultado = 0

    for x in range(n):
        resultado += lista_superior[x] * lista_inferior[x]

    media_ponderada = resultado/sum(lista_inferior)
    return print( '%.1f' % media_ponderada)





n = int(input())

lista_superior = list(map(int, input().strip().split(' ')))

lista_inferior = list(map(int, input().strip().split(' ')))

MediaPonderada(lista_superior, lista_inferior, n)
