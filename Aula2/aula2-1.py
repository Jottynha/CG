import matplotlib.pyplot as plt
import matplotlib.patches as patches

def construir_plano_cartesiano(eixo_x:float,eixo_y:float, title:str):
    fig, ax = plt.subplots(figsize=(7,7))
    fig.patch.set_facecolor('black') # Fundo da Janela Preto
    ax.set_facecolor('black') # Fundo Preto
    ax.set_title("Dispositivo Lógico: Clique 3 vezes",color='white', fontsize=14)
    ax.grid(True,color='white',linestyle='--',alpha=0.3)
    ax.tick_params(colors='white') # Marcações em Branco
    for spine in ax.spines.values():
        spine.set_color('white') # Bordas em Branco    
    ax.set_xlim(0,eixo_x)
    ax.set_ylim(0,eixo_y)
    ax.set_title(title)
    ax.grid(True,linestyle='--',alpha=0.5)
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")

    return fig, ax

def main():
    print("Dispositivos de Entrada...")
    fig,ax = construir_plano_cartesiano(eixo_x=100,eixo_y=100,title="Clique 3 vezes para gerar primitiva gráfica")
    coordenadas_entrada = []
    def ao_clicar(event): # Callback quando o mouse dispara evento
        if event.xdata is None or event.ydata is None: # Ignora click fora da malha
            return
        # Dispositivo de Entrada [Localizador]
        x,y = event.xdata,event.ydata 
        coordenadas_entrada.append([x,y])
        print(f"Entrada do Mouse --> Coordenadas: ({x:.2f},{y:.2f})")
        ax.plot(x,y,"ro") # "ro" -> Ponto Vermelho (Red Circle)
        fig.canvas.draw() # Atualiza o desenho
        if len(coordenadas_entrada) == 3: 
            print("Desenhando a primitiva de Polígono")
            triangulo = patches.Polygon(coordenadas_entrada,closed=True,
                                        fill=True, color='green', alpha=0.6,
                                        edgecolor='red', linewidth=3)
            ax.add_patch(triangulo)
            fig.canvas.draw() # Atualiza o desenho
            coordenadas_entrada.clear()
    fig.canvas.mpl_connect('button_press_event',ao_clicar) # Cria o [Ouvinte] que conecta o mousa à função clicar
    print("Aguardando entraada do usuário na interface gráfica...")
    plt.show()      
main()  