import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math

def desenhar_engrenagem(tela, centro, raio=15, dentes=10,
                        cor=(180, 180, 180), espessura=2):
    cx, cy = centro
    # Corpo da engrenagem
    cv2.circle(tela, (cx, cy), raio, cor, espessura)
    # Dentes radiais
    for i in range(dentes):
        ang = 2 * math.pi * i / dentes
        x_in = int(cx + (raio - 2) * math.cos(ang))
        y_in = int(cy + (raio - 2) * math.sin(ang))
        x_out = int(cx + (raio + 5) * math.cos(ang))
        y_out = int(cy + (raio + 5) * math.sin(ang))
        cv2.line(tela, (x_in, y_in), (x_out, y_out), cor, 3)
    # Furo central
    cv2.circle(tela, (cx, cy), max(3, raio // 4), cor, -1)

def desenhar_garra(tela, ponto, angulo, comprimento=28):
    x, y = ponto
    # A garra acompanha a orientação do último elo.
    ux = math.cos(angulo)
    uy = -math.sin(angulo)
    # Vetor perpendicular para separar as duas pontas.
    px = -uy
    py = ux
    # Base da garra ligeiramente à frente da junta.
    base_x = x + int(ux * 7)
    base_y = y + int(uy * 7)
    # Pontos de abertura das duas garras.
    abertura = 9
    ponta1 = (
        int(base_x + ux * comprimento + px * abertura),
        int(base_y + uy * comprimento + py * abertura)
    )
    ponta2 = (
        int(base_x + ux * comprimento - px * abertura),
        int(base_y + uy * comprimento - py * abertura)
    )
    cv2.line(tela, (x, y), ponta1, (0, 200, 255), 5)
    cv2.line(tela, (x, y), ponta2, (0, 200, 255), 5)
    # Pequenos segmentos voltados para dentro, dando aparência de garra.
    curva = 8
    ponta1_final = (
        int(ponta1[0] - ux * curva + px * 4),
        int(ponta1[1] - uy * curva + py * 4)
    )
    ponta2_final = (
        int(ponta2[0] - ux * curva - px * 4),
        int(ponta2[1] - uy * curva - py * 4)
    )
    cv2.line(tela, ponta1, ponta1_final, (0, 200, 255), 4)
    cv2.line(tela, ponta2, ponta2_final, (0, 200, 255), 4)

def braco_mecanico(x, y, ang_ombro, ang_cotovelo):
    # CONFIGURAÇÕES DO BRAÇO
    largura_tela = 600
    altura_tela = 500
    # Comprimento dos dois elos
    comprimento_elo1 = 120
    comprimento_elo2 = 100
    # CONVERSÃO DOS ÂNGULOS [recebidos em graus]
    ang_ombro_rad = math.radians(ang_ombro) # Conversão radianos
    ang_cotovelo_rad = math.radians(ang_cotovelo)
    tela = np.zeros((altura_tela, largura_tela, 3),dtype=np.uint8)
    # BASE DO ROBÔ [x e y representam o canto superior esquerdo da base]
    cv2.rectangle(tela,(x, y),(x + 50, y + 50),(100, 100, 100),-1)
    # A primeira junta fica no centro da parte superior da base.
    base_x = x + 25
    base_y = y
    # PRIMEIRO ELO
    # Coordenada X da primeira junta: x1 = x0 + comprimento * cos(ângulo)
    x1 = base_x + comprimento_elo1 * math.cos(ang_ombro_rad)
    # Como o eixo Y dos pixels cresce para baixo, precisamos SUBTRAIR o seno. [y1 = y0 - comprimento * sin(ângulo)]
    y1 = base_y - comprimento_elo1 * math.sin(ang_ombro_rad)
    x1 = int(x1)
    y1 = int(y1)
    # SEGUNDO ELO
    # O segundo elo utiliza o ângulo ACUMULADO:
    # ângulo total = ângulo do ombro + ângulo do cotovelo
    angulo_total = ang_ombro_rad + ang_cotovelo_rad
    # Coordenada final do segundo elo
    x2 = x1 + comprimento_elo2 * math.cos(angulo_total)
    y2 = y1 - comprimento_elo2 * math.sin(angulo_total)
    x2 = int(x2)
    y2 = int(y2)
    # DESENHO DOS ELOS
    # Primeiro elo
    cv2.line(tela,(base_x, base_y),(x1, y1),(220, 220, 220),8)
    # Segundo elo
    cv2.line(tela,(x1, y1),(x2, y2),(220, 220, 220),8)
    # DESENHO DAS JUNTAS E ENGRENAGENS
    # Junta da base
    desenhar_engrenagem(tela, (base_x, base_y), raio=15)
    cv2.circle(tela,(base_x, base_y),8,(0, 0, 255),-1)
    # Junta do cotovelo
    desenhar_engrenagem(tela, (x1, y1), raio=15)
    cv2.circle(tela,(x1, y1),8,(0, 0, 255),-1)
    # Última junta / ponta do braço
    cv2.circle(tela,(x2, y2),8,(0, 255, 255),-1)
    # GARRA NA ÚLTIMA JUNTA
    desenhar_garra(tela, (x2, y2), angulo_total)
    texto1 = f"Angulo ombro: {ang_ombro} graus"
    texto2 = f"Angulo cotovelo: {ang_cotovelo} graus"
    cv2.putText(tela,texto1,(10, 25),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255, 255, 255),1)
    cv2.putText(tela,texto2,(10, 50),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255, 255, 255),1)
    tela_rgb = cv2.cvtColor(tela, cv2.COLOR_BGR2RGB)
    plt.imshow(tela_rgb)
    plt.title("Braço Robótico 2D")
    plt.show()
    # Mostra as coordenadas calculadas
    print("=== COORDENADAS ===")
    print(f"Base:({base_x}, {base_y})")
    print(f"Cotovelo:({x1}, {y1})")
    print(f"Ponta:({x2}, {y2})")

if __name__ == "__main__":
    origem = (100, 400)
    ang_ombro = 60
    ang_cotovelo = 30
    braco_mecanico(
        origem[0],
        origem[1],
        ang_ombro,
        ang_cotovelo
    )