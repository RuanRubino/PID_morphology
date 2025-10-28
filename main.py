from erosao import erosao_binaria
from dilatacao import dilatacao_binaria
from printer import printer_dilatacao, printer_erosao,printer_aberta, printer_fechamento
import cv2

def main():
    caminho = "paisagem2.jpg"
    imagem = cv2.imread(caminho)
        # === 1. Leitura da imagem ===

    if imagem is None:
        raise FileNotFoundError("Não foi possível abrir a imagem.")

    # === 2. Conversão para escala de cinza ===
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # === 3. Conversão para binário (threshold automático de Otsu) ===
    _, binaria = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Converte a imagem binária (matriz NumPy) para lista de listas Python
    binaria_lista = binaria.tolist()


    kernel = [
    [0,1,0],
    [1,1,1],
    [0,1,0]
    ]
    
    kernel_quadrado = [
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1]
    ]
    while True:

        a = int(input('ESCOLHA O NUMERO DA SUA OPERACAO : 1.EROSAO, 2.DILATACAO, 3. ABERTURA, 4.FECHAMENTO 5.SAIR \n'))
        match a :
            case 1:
                erodida_lista = erosao_binaria(binaria_lista, kernel, iteracoes=1)
                printer_erosao( imagem, binaria, erodida_lista)
            case 2:
                dilatada_lista = dilatacao_binaria(binaria_lista, kernel, iteracoes=1)
                printer_dilatacao(imagem, binaria, dilatada_lista)
            case 3:
                erodida = erosao_binaria(binaria_lista, kernel, iteracoes=1)
                aberta_lista = dilatacao_binaria(erodida, kernel, iteracoes=1)
                printer_aberta(imagem, binaria, aberta_lista)
            case 4:
                dilatada = dilatacao_binaria(binaria_lista, kernel, iteracoes=1)
                fechada_lista = erosao_binaria(dilatada, kernel, iteracoes=1)
                printer_fechamento(imagem, binaria, fechada_lista)
            case 5:
                break

if __name__ == "__main__":
    main()