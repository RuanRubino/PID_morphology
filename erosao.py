def erosao_binaria(imagem_binaria, kernel, iteracoes=1):
    altura = len(imagem_binaria)
    largura = len(imagem_binaria[0])
    kh = len(kernel)
    kw = len(kernel[0])
    offset_y = kh // 2
    offset_x = kw // 2

    for _ in range(iteracoes):
        nova_imagem = [[0 for _ in range(largura)] for _ in range(altura)]
        for y in range(offset_y, altura - offset_y):
            for x in range(offset_x, largura - offset_x):
                # Verifica apenas onde kernel == 1
                todos_brancos = True
                for ky in range(kh):
                    for kx in range(kw):
                        if kernel[ky][kx] == 1:
                            ny = y + ky - offset_y
                            nx = x + kx - offset_x
                            if imagem_binaria[ny][nx] == 0:
                                todos_brancos = False
                                break
                    if not todos_brancos:
                        break
                nova_imagem[y][x] = 255 if todos_brancos else 0
        imagem_binaria = nova_imagem
    return imagem_binaria




