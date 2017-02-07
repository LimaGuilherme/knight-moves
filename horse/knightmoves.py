def input_origem():
    origem = raw_input("Entre com a posicao inicial do cavalo: ")
    origem = eval(origem)
    return origem


def input_saida():
    destino = raw_input("Entre com a posicao final do cavalo: ")
    destino = eval(destino)
    return destino


def movimentos_cavalo():
    return [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]


def go_horse(origem, destino):
    casas_testadas = [[False] * 8 for i in range(8)]
    passos = [origem + [[]]]

    while True:
        proximos_passos = []
        for passo in passos:
            for movimento in movimentos_cavalo():
                x, y = passo[0] + movimento[0], passo[1] + movimento[1]
                if [x, y] == destino:
                    return passo[2] + [[x, y]]
                if 0 <= x < 8 and 0 <= y < 8:
                    if not casas_testadas[x][y]:
                        proximos_passos.append([x, y, passo[2] + [[x, y]]])
                        casas_testadas[x][y] = True
            passos = proximos_passos


if __name__ == '__main__':
    origem = input_origem()
    destino = input_saida()
    print "Caminho: \n", go_horse(origem, destino)

