# Cores
from PIL import Image
def criar_imagem_rgb(largura, altura, cor_rgb, nome_arquivo):
    # Cria uma imagem RGB com uma cor sólida e salva em disco.
    imagem = Image.new('RGB', (largura, altura), cor_rgb) # Aloca a matrizna memória.
    imagem.save(f"{nome_arquivo}.png")
    print(f"[Sucesso] Imagem RGB {nome_arquivo} criada com sucesso.")

def criar_imagem_cmyk(largura, altura, cor_cmyk, nome_arquivo):
    # Cria uma imagem CMYK com uma cor sólida e salva em disco.
    c_int = int(cor_cmyk[0]*2.55)
    m_int = int(cor_cmyk[1]*2.55)
    y_int = int(cor_cmyk[2]*2.55)
    k_int = int(cor_cmyk[3]*2.55)
    cor_cmyk = (c_int,m_int,y_int,k_int)
    imagem = Image.new('CMYK', (largura, altura), cor_cmyk) # Aloca a matrizna memória.
    imagem.save(f"{nome_arquivo}.jpg")
    print(f"[Sucesso] Imagem CMYK {nome_arquivo} criada com sucesso.")

def rgb_para_cmyk(r,g,b):
    # Evitar erro de divisão por zero (preto absoluto)
    if (r==0) and (g==0) and (b==0):
        return 0.0,0.0,0.0,1.0
    # Normalização para espaço float [0.0, 1.0]
    r_prime = r/255.0
    g_prime = g/255.0
    b_prime = b/255.0
    # Cálculo do canal Key (preto)
    k = 1.0 - max(r_prime,g_prime,b_prime)
    # Cálculo dos canais C, M, Y
    c = (1.0 - r_prime - k) / (1.0 - k)
    m = (1.0 - g_prime - k) / (1.0 - k)
    y = (1.0 - b_prime - k) / (1.0 - k)
    c_int = int(c*255)
    m_int = int(m*255)
    y_int = int(y*255)
    k_int = int(k*255)
    return c_int,m_int,y_int,k_int

if __name__ == "__main__":
    # Dimensões
    LARGURA = 400
    ALTURA = 400
    cor_vermelha_rgb = (255,0,0)
    print(f"Cor vermelha em RGB: {cor_vermelha_rgb}")
    criar_imagem_rgb(LARGURA,ALTURA,cor_vermelha_rgb,"cor_rgb")
    cor_vermelha_cmyk = rgb_para_cmyk(cor_vermelha_rgb[0],cor_vermelha_rgb[1],cor_vermelha_rgb[2])
    print(f"Cor vermelha em CMYK: {cor_vermelha_cmyk}")
    criar_imagem_cmyk(LARGURA,ALTURA,cor_vermelha_cmyk,"cor_cmyk_conversao")

