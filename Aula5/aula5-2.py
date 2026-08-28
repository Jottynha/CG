from PIL import Image
import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math

VERDE = (0,255,0)
AMARELO = (255,255,0)
AZUL = (0,0,255)
BRANCO = (255,255,255)
LARGURA = 400
ALTURA = 400

# Bandeira do Brasil
tela = np.zeros((ALTURA, LARGURA, 3), dtype=np.uint8)
# Fundo verde
cv2.rectangle(tela, (0,0), (LARGURA,ALTURA), VERDE, -1)
# Losango amarelo
pontos_losango = np.array([
    [LARGURA//2, 30],
    [370, ALTURA//2],
    [LARGURA//2, 370],
    [30, ALTURA//2]
], np.int32)
cv2.fillPoly(tela, [pontos_losango], AMARELO)
# Círculo azul
centro = (LARGURA//2, ALTURA//2)
cv2.circle(tela, centro, 90, AZUL, -1)
# Estrelas
def estrela(imagem, centro, tamanho, cor):
    pontos = []
    for i in range(10):
        angulo = -math.pi/2 + i * math.pi/5
        if i % 2 == 0:
            raio = tamanho
        else:
            raio = tamanho * 0.4
        x = int(centro[0] + raio * math.cos(angulo))
        y = int(centro[1] + raio * math.sin(angulo))
        pontos.append([x, y])
    pontos = np.array(pontos, np.int32)
    cv2.fillPoly(imagem, [pontos], cor)
estrelas = [
    ((225, 180), 8),
    ((250, 175), 6),
    ((275, 185), 7),
    ((205, 205), 6),
    ((235, 215), 5),
    ((265, 215), 6),
    ((295, 205), 5),
    ((220, 240), 6),
    ((250, 245), 7),
    ((280, 235), 5),
    ((200, 180), 5)
]
for posicao, tamanho in estrelas:
    estrela(tela, posicao, tamanho, BRANCO)
plt.imshow(tela)
plt.title("Bandeira do Brasil")
plt.axis("off")
plt.show()
