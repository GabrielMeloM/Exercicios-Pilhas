'''
EXERCICIO 6
    Implemente a função 'verificar_balanceamento', que recebe como entrada
    uma string representando uma expressão aritmética contendo parenteses
    e verifica se os parênteses estão balanceados.
    Deve ser utilizada uma estrutura de Pilha para resolver o problema.
    Se a expressão estiver balanceada, deve retornar True,
    caso contrário deve retornar False
'''


def verificar_balanceamento(string):
    pilha = []
    for elemento in string:
        if elemento == "(":
            pilha.append(elemento)
        elif elemento == ")":
            if len(pilha) == 0:
                return False
            else:
                pilha.pop()
    if len(pilha) == 0:
        return True
    return False
