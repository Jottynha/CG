import colorsys
from PIL import Image

def criar_imagem_via_hsv(largura, altura, h_graus, s_pct, v_pct, nome_arquivo):
    """
    Cria uma imagem baseada no espaço HSV.
    -> h_graus: Matriz (Hue) de 0 a 360°.
    -> s_pct: Saturação (Saturation) de 0 a 100%.
    -> v_pct: Valor/Brilho (Value) de 0 a 100%.
    """
    # Normalização do domínio físico para o domínio matemático [0.0,1.0]
    h_norm = h_graus / 360.0
    s_norm = s_pct / 100.0
    v_norm = v_pct / 100.0
    # Conversão do espaço cilindrico (HSV) para vetorial (RGB)
    r_float, g_float, b_float = colorsys.hsv_to_rgb(h_norm,s_norm,v_norm)
    # Conversão de ponto flutuantepara inteiro de 8 bits (0-255)
    r = int(r_float*255)
    g = int(g_float*255)
    b = int(b_float*255)
    imagem = Image.new("RGB",(largura,altura),(r,g,b))
    imagem.save(nome_arquivo)
    print(f"[HSV] Imagem salva: {nome_arquivo} | RGB final: ({r}, {g}, {b})")

def criar_imagem_via_hsl(largura, altura, h_graus, s_pct, l_pct, nome_arquivo):
    """
    Cria uma imagem baseada no espaço HSL.
    -> h_graus: Matriz (Hue) de 0 a 360°.
    -> s_pct: Saturação (Saturation) de 0 a 100%.
    -> l_pct: Luminosidade (Lightness) de 0 a 100%.
    """
    # Normalização do domínio físico para o domínio matemático [0.0,1.0]
    h_norm = h_graus / 360.0
    s_norm = s_pct / 100.0
    l_norm = l_pct / 100.0
    # Conversão do espaço cilindrico (HSL) para vetorial (RGB)
    r_float, g_float, b_float = colorsys.hls_to_rgb(h_norm,l_norm,s_norm)
    # Conversão de ponto flutuantepara inteiro de 8 bits (0-255)
    r = int(r_float*255)
    g = int(g_float*255)
    b = int(b_float*255)
    imagem = Image.new("RGB",(largura,altura),(r,g,b))
    imagem.save(nome_arquivo)
    print(f"[HSL] Imagem salva: {nome_arquivo} | RGB final: ({r}, {g}, {b})")

if __name__ == "__main__":
    LARGURA, ALTURA = 400,400
    # Ciano Vibrante em HSV - H = 180 (Ciano); S = 100% (Puro); V = 100% (Brilho Máximo)
    criar_imagem_via_hsv(LARGURA,ALTURA, 180, 100, 100, "ciano_hsv.png")
    # Ciano Vibrante em HSL [Para obter a cor pura, a Luminosidade (Lightness) deve ser 50%]
    criar_imagem_via_hsl(LARGURA,ALTURA, 180, 100, 50, "ciano_hsl.png")
    # Efeito Desbotado ("Pastel") usando HSL, aumentando a luminosidade 80%.
    criar_imagem_via_hsl(LARGURA,ALTURA, 180, 100, 80, "ciano_pastel_hsl.png")
    
