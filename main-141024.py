# Dada uma lista de numeros e um numero k, retorne se quaisquer dois numeros da lista somam k
# [10, 15, 3, 7]
# k = 17

lista = [10, 15, 3, 7]
k = 17

tamanhoLista = len(lista)

for indice in range(tamanhoLista):

    indiceInicial = indice

    for proximoIndice in range(indice + 1, tamanhoLista):

        listaValor = lista[indiceInicial] + lista[proximoIndice]

        if listaValor == 17:
            print(f'Soma de {lista[indiceInicial]} + {lista[proximoIndice]} é igual a 17: {True}')

        else:
            print(f'Soma de {lista[indiceInicial]} + {lista[proximoIndice]} é igual a 17: {False}')