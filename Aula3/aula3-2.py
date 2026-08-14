# Circulo rasterizado
from PIL import Image
def circulo_padrao():
    print("Iniciando rasterização do círculo...")
    # Definindo a resolução (300x300)
    largura_tela, altura_tela = 300, 300
    img = Image.new('RGB', (largura_tela, altura_tela), "white")
    # propriedades matemáticas do círculo
    centro_x, centro_y = 150, 150 
    raio = 50
    raio_quadrado = raio**2
    # Definindo onde o círculo pode existir
    x_min = centro_x - raio
    x_max = centro_x + raio
    y_min = centro_y - raio
    y_max = centro_y + raio
    # Simulando rasterização
    for x in range(x_min,x_max+1):
        for y in range(y_min,y_max+1):
            distancia_quadrada = (x - centro_x)**2 + (y - centro_y)**2 # Retira a potência para transformar em um quadrado
            # se a distância até o centro for menor/igual ao raio -> o pixel pertence ao circulo (pinta de vermelho)
            if distancia_quadrada <= raio_quadrado:
                img.putpixel((x,y),(255,0,0))
    img.save("circulo_rasterizado.png")
    print("Círculo salvo como 'circulo_rasterizado.png'")
    img.show()

def renderizar_circulo(fator_qualidade):
    """
    A resolução padrão será: 300x300 e raio 50
    Se fator -> 0.1, então a resolução torna-se 30x30
    Se fator -> 1.0, então a resolução torna-se 300x300
    Se fator -> 4.0, então a resolução torna-se 1200x1200
    """
    print(f"Renderizando círculo com fator de qualidade {fator_qualidade}")
    largura_base, altura_base = 300, 300
    raio_base = 50
    largura_tela = int(largura_base * fator_qualidade)
    altura_tela = int(altura_base * fator_qualidade)
    raio = int(raio_base * fator_qualidade)
    centro_x = int(largura_tela / 2)
    centro_y = int(altura_tela / 2)
    raio_quadrado = raio**2
    img = Image.new('RGB', (largura_tela, altura_tela), "white")
    x_min, x_max = centro_x - raio, centro_x + raio
    y_min, y_max = centro_y - raio, centro_y + raio
    for x in range(x_min,x_max+1):
            for y in range(y_min,y_max+1):
                distancia_quadrada = (x - centro_x)**2 + (y - centro_y)**2 # Retira a potência para transformar em um quadrado
                # se a distância até o centro for menor/igual ao raio -> o pixel pertence ao circulo (pinta de vermelho)
                if distancia_quadrada <= raio_quadrado:
                    img.putpixel((x,y),(255,0,0))
    return img

def circulo_vetorial():
    print("Iniciando a síntese do círculo vetorial...")
    largura_tela, altura_tela = 300, 300
    centro_x, centro_y = 150, 150
    raio = 50
    cor_preenchimento = "red"
    # Formulação (XML/SVG) ao inves de varrer uma grade
    codigo_vetorial_svg = f"""
    <svg width="{largura_tela}" height="{altura_tela}" xmlns="http://www.w3.org/2000/svg">
    <rect width="100%" height="100%" fill="white"/>
    <circle cx="{centro_x}" cy="{centro_y}" r="{raio}" fill="{cor_preenchimento}"/>
    </svg>
    """
    nome_arquivo = 'circulo_vetorial.svg'
    with open(nome_arquivo,'w') as arquivo:
        arquivo.write(codigo_vetorial_svg)
    print(f"Círculo salvo como '{nome_arquivo}'")
    import webbrowser
    webbrowser.open(f"file://{nome_arquivo}")

circulo_vetorial()