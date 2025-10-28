from dilatacao import dilatacao_binaria
import cv2
import numpy as np 

def printer_dilatacao(imagem, binaria, dilatada_lista):
    
    dilatada = np.array(dilatada_lista, dtype='uint8')

    cv2.imshow("Original", imagem)
    cv2.imshow("Binária", binaria)
    cv2.imshow("Dilatada (manual)", dilatada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # === 7. Salva resultado ===
    cv2.imwrite("imagem_dilatada_manual.jpg", dilatada)
    print("Imagem dilatada salva como 'imagem_dilatada_manual.jpg'")

def printer_erosao(imagem, binaria, erodida_lista):

    erodida = np.array(erodida_lista, dtype='uint8')  

    # === 5. Mostra resultados ===
    cv2.imshow("Original", imagem)
    cv2.imshow("Binária", binaria)
    cv2.imshow("Erodida (manual)", erodida)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # === 6. Salva o resultado ===
    cv2.imwrite("imagem_erodida_manual.jpg", erodida)
    print("Imagem erodida salva como 'imagem_erodida_manual.jpg'")

def printer_aberta(imagem, binaria, aberta_lista):

    aberta = np.array(aberta_lista, dtype='uint8')  

    # === 5. Mostra resultados ===
    cv2.imshow("Original", imagem)
    cv2.imshow("Binária", binaria)
    cv2.imshow("aberta (manual)", aberta)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # === 6. Salva o resultado ===
    cv2.imwrite("imagem_aberta_manual.jpg",aberta)
    print("Imagem aberta salva como 'imagem_aberta_manual.jpg'")

def printer_fechamento(imagem, binaria, fechamento_lista):

    fechamento = np.array(fechamento_lista, dtype='uint8')  

    # === 5. Mostra resultados ===
    cv2.imshow("Original", imagem)
    cv2.imshow("Binária", binaria)
    cv2.imshow("fechamento (manual)", fechamento)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # === 6. Salva o resultado ===
    cv2.imwrite("imagem_fechamento_manual.jpg", fechamento)
    print("Imagem fechamento salva como 'imagem_fechamento_manual.jpg'")
