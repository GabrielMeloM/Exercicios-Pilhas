'''
EXERCICIO 5
    Fazer uma função "menos_o_d". Ela recebe uma string e vai colocando as
    letras uma a uma em uma pilha. Porém, quando ela vê uma letra d, ao invés
    de colocar o d, ela faz um pop() na pilha, tirando a ultima letra logo antes
    do d.

    Observe que se a primeira letra for d, ela talvez tente tirar uma coisa de
    uma pilha vazia.
    Nesse caso, faça o seguinte: se a pilha está vazia e veio um "d",
    simplesmente não tire nada da pilha. Ela continuará vazia.

    Sua função deve retornar a ultima pilha
'''


def menos_o_d(texto):
    pilha = []
    for letra in texto:
        if letra == "d" or letra == "D":
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha = []
        else:
            pilha.append(letra)
    return pilha
