import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def main():
    tela = np.zeros((300,300,3),dtype=np.uint8)
    # Primitiva de Linha cv2.line(imagem,ponto inicial,ponto final,RGB,espessura)
    cv2.line(tela,(50,50),(250,50),(0,255,0),3) 
    # Primitiva de Círculo cv2.circle(imagem,centro,raio,RGB,espessura(-1 preenche tudo))
    cv2.circle(tela,(150,150),60,(255,0,0),-1)
    # Primitiva de Polígono (Triangulo) cv2.fillPoly(imagem,coordenadas,RGB,espessura)
    pontos_triangulo = np.array([[150,200],[100,280],[200,280]],np.int32)
    # O OpenCV precisa que o array de pontos tenha o formato (número_pontos,1,2)
    pontos_triangulo = pontos_triangulo.reshape((-1,1,2))
    cv2.fillPoly(tela,[pontos_triangulo],(0,255,255))
    plt.imshow(tela)
    plt.title("Desenho de Primitivas")
    plt.show()

if __name__ == "__main__":
    main()