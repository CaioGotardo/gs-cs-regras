from itertools import product


def regra1(s, r, c):
    return int(s and (c or r))


def regra2(e, l, d):
    return int((not e) and ((not l) or (not d)))


def regra3(p, m):
    return int(p != m)


TABELA_MANUAL_1 = [0, 0, 0, 0, 0, 1, 1, 1]
TABELA_MANUAL_2 = [1, 1, 1, 0, 0, 0, 0, 0]
TABELA_MANUAL_3 = [0, 1, 1, 0]


def testar_regra(titulo, entradas, saida, funcao, tabela_manual):
    print(titulo)
    print(" ".join(entradas), "|", saida)
    todas_iguais = True
    combinacoes = product([0, 1], repeat=len(entradas))
    for combinacao, esperado in zip(combinacoes, tabela_manual):
        resultado = funcao(*combinacao)
        if resultado != esperado:
            todas_iguais = False
        print(" ".join(str(v) for v in combinacao), "|", resultado)
    print("Confere com a tabela-verdade manual:", "SIM" if todas_iguais else "NAO")
    print()


testar_regra("Regra 1 - Prioridade da ocorrencia",
             ["S", "R", "C"], "PR", regra1, TABELA_MANUAL_1)

testar_regra("Regra 2 - Pendencia de cadastro",
             ["E", "L", "D"], "PC", regra2, TABELA_MANUAL_2)

testar_regra("Regra 3 - Acompanhamento por divergencia",
             ["P", "M"], "A", regra3, TABELA_MANUAL_3)