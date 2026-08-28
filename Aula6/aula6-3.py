from PIL import Image
import colorsys
imagem_chroma = "CG/Aula6/chroma.jpeg"
imagem_fundo = "CG/Aula6/fundo.jpeg"
imagem_saida = "CG/Aula6/resultado.png"
# Faixa do verde que será removida
# Hue do colorsys vai de 0.0 até 1.0
H_MIN = 0.25
H_MAX = 0.45
# Saturação e brilho mínimos
SAT_MIN = 0.25
VAL_MIN = 0.20
chroma = Image.open(imagem_chroma).convert("RGBA")
fundo = Image.open(imagem_fundo).convert("RGBA")
pixels = chroma.load()
for y in range(chroma.height):
    for x in range(chroma.width):
        r, g, b, a = pixels[x, y]
        # RGB (0-255) -> RGB (0-1)
        r_n = r / 255
        g_n = g / 255
        b_n = b / 255
        # RGB -> HSV
        h, s, v = colorsys.rgb_to_hsv(r_n, g_n, b_n)
        # Verifica se o pixel é verde
        if (
            H_MIN <= h <= H_MAX
            and s >= SAT_MIN
            and v >= VAL_MIN
        ):
            # Torna o pixel transparente
            pixels[x, y] = (r, g, b, 0)
fundo = fundo.resize(chroma.size)
resultado = Image.alpha_composite(fundo, chroma)
resultado.save(imagem_saida)
print("Imagem criada:", imagem_saida)