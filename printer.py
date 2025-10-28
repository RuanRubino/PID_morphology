from dilatacao import dilatacao_binaria
import cv2
import numpy as np 

def printer_all(imagem, binaria, final_lista, texto):

    final = np.array(final_lista, dtype='uint8')  

    # === 5. Mostra resultados ===
    cv2.imshow("Original", imagem)
    cv2.imshow("Binária", binaria)
    cv2.imshow(texto, final)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # === 6. Salva o resultado ===
    cv2.imwrite(f"imagem_{texto}.jpg", final)
    print("Imagem fechamento salva como 'imagem_fechamento_manual.jpg'")
