# Rasterizaçao / Vetorização
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("Iniciando laboratório de Rasterização...")
    # Definindo resolução (15x15 pixels)
    largura, altura = 15, 15
    # Criando buffer de pixels, preenchido com zeros (define cor preta)
    framebuffer = np.zeros((altura, largura))
    # Pontos iniciais e finais geométricos
    x0, y0 = 2, 2
    x1, y1 = 12, 9
    # Simulação simplificada do processo proposto por Bresenham
    passos = max(abs(x1 - x0), abs(y1 - y0))
    inc_x = (x1 - x0) / passos
    inc_y = (y1 - y0) / passos
    x_atual, y_atual = x0, y0
    for i in range(passos+1):
        pixel_x =  int(round(x_atual))
        pixel_y =  int(round(y_atual))
        # Pinta pixel na memória (atribuindo valor 1 para cor clara)
        framebuffer[pixel_y,pixel_x] = 1.0
        # Avança no vetor
        x_atual += inc_x
        y_atual += inc_y
    # Criando duas imagens para comparação
    fig, (ax1,ax2) = plt.subplots(1,2,figsize=(12,6))
    fig.patch.set_facecolor('#1e1e1e') 
    ax1.set_facecolor('black')
    ax1.set_title("Vetorização (Matemática Contínua)",color='white', fontsize=14)
    ax1.set_xlim(0,largura)
    ax1.set_ylim(0,altura)
    ax1.plot([x0,x1],[y0,y1],color='red',linewidth=2,label='Vetor ideal')
    ax1.grid(True,color='white',alpha=0.2)
    ax1.legend()
    ax1.tick_params(colors='white') 
    ax2.set_title("Rasterização (Matemática Discreta/Pixels)",color='white', fontsize=14)
    ax2.imshow(framebuffer, cmap='gray', origin='lower',extent=[0, largura, 0, altura]) # O cmap='gray' converte os 0s e 1s da matriz calculada
    ax2.plot([x0,x1],[y0,y1],color='red',linewidth=2,linestyle='--',alpha=0.5)
    ax2.grid(True,color='white',alpha=0.2)
    ax2.tick_params(colors='white')
    plt.tight_layout()
    plt.show()

main()