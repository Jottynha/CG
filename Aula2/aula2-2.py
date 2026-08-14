import matplotlib.pyplot as plt
import time

def main():
    print("=== Simulador de FPS (Frames por Segundo) ===")
    print("Valores: 5 (Travado), 24 (Cinema), 60 (Fluido)")
    try:
        fps_alvo = int(input("Digite o FPS desejado para a simualação: "))
    except ValueError:
        fps_alvo = 30
    delta_time = 1.0/fps_alvo
    plt.ion() # Ativa o modo interativo
    fig, ax = plt.subplots(figsize=(8,4))
    # Criando um plano escuro
    fig.patch.set_facecolor('black') # Fundo da Janela Preto
    ax.set_facecolor('black') # Fundo Preto
    ax.set_title(f"Simulação Gráfica rodando a {fps_alvo} FPS",color='white', fontsize=14)
    ax.grid(True,color='white',linestyle='--',alpha=0.3)
    ax.tick_params(colors='white') # Marcações em Branco
    for spine in ax.spines.values():
        spine.set_color('white') # Bordas em Branco
    ax.set_xlim(0,100)
    ax.set_ylim(0,10)
    objeto, = ax.plot([],[],marker='o',color='red',markersize=20)
    # Aqui começa o laço de renderização do FPS (GAME LOOP)
    posicao_x = 0
    velocidade = 50
    tempo_anterior = time.time()
    while posicao_x <= 100:
        tempo_atual = time.time()
        tempo_decorrido = tempo_atual - tempo_anterior
        tempo_anterior = tempo_atual
        # Atualização fisica -> Posição = Velocidade * Tempo (S = S0 + V*t)
        # Esse ajuste garante que a velocidade real do objeto seja a mesma, independentemente do FPS do monitor
        posicao_x += velocidade * tempo_decorrido
        objeto.set_data([posicao_x],[5])
        # RENDERIZA E PAUSA
        plt.pause(delta_time)
    print("Animação concluída")
    plt.ioff()
    plt.show()

main()