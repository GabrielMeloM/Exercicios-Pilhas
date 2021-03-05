'''
EXERCICIO 4
    Faça uma função pilha_letras, que recebe uma string e vai colocando as
    letras da string uma a uma em uma pilha.
    Sua função deve retornar a pilha pronta.
'''


def pilha_letras(texto):
    pilha = []
    for letra in texto:
        pilha.append(letra)
    return pilha
