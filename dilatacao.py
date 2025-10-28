def dilatacao_binaria(imagem_binaria, kernel, iteracoes=1):

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
                # Se pelo menos um pixel do kernel sobrepõe um pixel branco (255), ativa o centro
                algum_branco = False
                for ky in range(kh):
                    for kx in range(kw):
                        if kernel[ky][kx] == 1:
                            ny = y + ky - offset_y
                            nx = x + kx - offset_x
                            if imagem_binaria[ny][nx] == 255:
                                algum_branco = True
                                break
                    if algum_branco:
                        break
                nova_imagem[y][x] = 255 if algum_branco else 0
        imagem_binaria = nova_imagem
    return imagem_binaria



