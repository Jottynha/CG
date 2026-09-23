import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# ============================================================
# TRANSFORMAÇÕES GRÁFICAS
# Desafio do Engenheiro de Satélites Espaciais
#
# Conceitos utilizados:
#   - Translação
#   - Rotação
#   - Escala
#   - Matrizes homogêneas
#   - Composição TRS
#
# SRO = Sistema de Referência do Objeto
# SRU = Sistema de Referência Universal
#
# Com vetores-coluna:
#
#       P' = T @ R @ S @ P
#
# Portanto:
#       1. Escala
#       2. Rotação
#       3. Translação
# ============================================================


# ============================================================
# PASTA DE SAÍDA
# ============================================================
#
# Os arquivos serão salvos na mesma pasta deste programa.
# Assim não dependemos de /mnt/data.
#

PASTA_SAIDA = Path(__file__).resolve().parent


# ============================================================
# MATRIZ DE TRANSLAÇÃO
# ============================================================

def matriz_translacao(tx, ty):
    """
    Cria uma matriz homogênea 3x3 de translação.

             | 1  0  tx |
        T =  | 0  1  ty |
             | 0  0   1 |
    """

    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ], dtype=float)


# ============================================================
# MATRIZ DE ROTAÇÃO
# ============================================================

def matriz_rotacao(angulo_graus):
    """
    Cria uma matriz homogênea 3x3 de rotação.

             | cosθ  -senθ  0 |
        R =  | senθ   cosθ  0 |
             |  0      0    1 |
    """

    theta = np.radians(angulo_graus)

    cos_theta = np.cos(theta)
    sen_theta = np.sin(theta)

    return np.array([
        [cos_theta, -sen_theta, 0],
        [sen_theta,  cos_theta, 0],
        [0,          0,         1]
    ], dtype=float)


# ============================================================
# MATRIZ DE ESCALA
# ============================================================

def matriz_escala(sx, sy):
    """
    Cria uma matriz homogênea 3x3 de escala.

             | sx  0   0 |
        S =  | 0   sy  0 |
             | 0   0   1 |
    """

    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ], dtype=float)


# ============================================================
# COMPOSIÇÃO TRS
# ============================================================

def matriz_trs(tx=0, ty=0, angulo=0, sx=1, sy=1):
    """
    Cria a matriz de transformação composta.

    P' = T @ R @ S @ P

    Como estamos utilizando vetores-coluna, a ordem
    efetiva das transformações é:

        1. Escala
        2. Rotação
        3. Translação
    """

    T = matriz_translacao(tx, ty)
    R = matriz_rotacao(angulo)
    S = matriz_escala(sx, sy)

    return T @ R @ S


# ============================================================
# APLICAÇÃO DA MATRIZ AOS PONTOS
# ============================================================

def transformar(pontos, matriz):
    """
    Aplica uma matriz 3x3 aos pontos 2D.

    Os pontos são representados como:

        | x1  x2  x3 |
        | y1  y2  y3 |

    Eles são convertidos para coordenadas homogêneas:

        | x1  x2  x3 |
        | y1  y2  y3 |
        |  1   1   1 |

    Depois:

        P' = M @ P
    """

    pontos_homogeneos = np.vstack([
        pontos,
        np.ones(pontos.shape[1])
    ])

    resultado = matriz @ pontos_homogeneos

    return resultado[:2, :]


# ============================================================
# FECHAR POLÍGONO
# ============================================================

def fechar(pontos):
    """
    Adiciona o primeiro ponto novamente no final
    para fechar o desenho do objeto.
    """

    return np.column_stack([
        pontos,
        pontos[:, 0]
    ])


# ============================================================
# DESENHAR OBJETO
# ============================================================

def desenhar_objeto(ax, pontos, nome, alpha=0.25):
    """
    Desenha o polígono utilizando Matplotlib.
    """

    pontos_fechados = fechar(pontos)

    ax.fill(
        pontos_fechados[0],
        pontos_fechados[1],
        alpha=alpha,
        label=nome
    )

    ax.plot(
        pontos_fechados[0],
        pontos_fechados[1],
        linewidth=2
    )


# ============================================================
# CONFIGURAR EIXOS
# ============================================================

def configurar_eixos(ax, titulo, limite):
    """
    Configura os eixos cartesianos e destaca a origem.
    """

    # Eixo X
    ax.axhline(0, linewidth=1)

    # Eixo Y
    ax.axvline(0, linewidth=1)

    # Marca a origem
    ax.scatter(
        [0],
        [0],
        s=45,
        zorder=5
    )

    ax.annotate(
        "Origem (0,0)",
        xy=(0, 0),
        xytext=(0.25, 0.35),
        fontsize=9
    )

    ax.set_title(titulo)

    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")

    ax.set_xlim(-limite, limite)
    ax.set_ylim(-limite, limite)

    # Mantém a mesma proporção nos dois eixos
    ax.set_aspect(
        "equal",
        adjustable="box"
    )

    ax.grid(
        True,
        linestyle=":",
        alpha=0.5
    )


# ============================================================
# 1. MODELAGEM DOS OBJETOS NO SRO
# ============================================================
#
# Os objetos fornecidos no slide são:
#
# Corpo:
#   p1(-1,-1)
#   p2( 1,-1)
#   p3( 1, 1)
#   p4(-1, 1)
#
# Painéis solares:
#   p1(-1,-1)
#   p2( 1,-1)
#   p3( 1, 1)
#   p4(-1, 1)
#
# Antena:
#   p1(-1,0)
#   p2( 1,0)
#   p3( 0,2)
#
# Todos começam no SRO.
# ============================================================


# ------------------------------------------------------------
# Corpo
# ------------------------------------------------------------

corpo = np.array([
    [-1,  1,  1, -1],
    [-1, -1,  1,  1]
], dtype=float)


# ------------------------------------------------------------
# Painéis solares
#
# Os dois painéis possuem a mesma geometria inicial.
# ------------------------------------------------------------

painel = corpo.copy()


# ------------------------------------------------------------
# Antena
# ------------------------------------------------------------

antena = np.array([
    [-1, 1, 0],
    [0,  0, 2]
], dtype=float)


# ============================================================
# 2. PRIMEIRA IMAGEM — SRO
# ============================================================
#
# Nesta etapa NÃO aplicamos nenhuma transformação.
#
# Portanto, os objetos permanecem em suas posições originais.
# Como os dois painéis possuem a mesma geometria e estão
# inicialmente na origem, eles ficam sobrepostos.
# ============================================================

fig_sro, ax_sro = plt.subplots(
    figsize=(8, 8)
)


# Corpo
desenhar_objeto(
    ax_sro,
    corpo,
    "Corpo"
)


# Painel solar 1
desenhar_objeto(
    ax_sro,
    painel,
    "Painel solar 1"
)


# Painel solar 2
desenhar_objeto(
    ax_sro,
    painel,
    "Painel solar 2"
)


# Antena
desenhar_objeto(
    ax_sro,
    antena,
    "Antena"
)


configurar_eixos(
    ax_sro,
    "1. Objetos no SRO — Sistema de Referência do Objeto",
    limite=4
)


ax_sro.legend()

plt.tight_layout()


# Salva na mesma pasta do programa
arquivo_sro = PASTA_SAIDA / "satelite_sro.png"

fig_sro.savefig(
    arquivo_sro,
    dpi=160,
    bbox_inches="tight"
)


# ============================================================
# 3. MATRIZES TRS
# ============================================================
#
# Agora vamos montar o satélite no SRU.
#
# Cada objeto recebe uma transformação diferente.
# ============================================================


# ------------------------------------------------------------
# CORPO
# ------------------------------------------------------------
#
# O corpo é aumentado para representar o corpo principal.
#
# Escala:
#   Sx = 2
#   Sy = 2
#
# Rotação:
#   0 graus
#
# Translação:
#   (0, 0)
# ------------------------------------------------------------

M_corpo = matriz_trs(
    tx=0,
    ty=0,
    angulo=0,
    sx=2,
    sy=2
)


# ------------------------------------------------------------
# PAINEL ESQUERDO
# ------------------------------------------------------------
#
# Escala:
#   Sx = 3
#   Sy = 0.5
#
# Rotação:
#   +30 graus
#
# Translação:
#   (-4.1, 0)
# ------------------------------------------------------------

M_painel_esquerdo = matriz_trs(
    tx=-4.1,
    ty=0,
    angulo=30,
    sx=3,
    sy=0.5
)


# ------------------------------------------------------------
# PAINEL DIREITO
# ------------------------------------------------------------
#
# Escala:
#   Sx = 3
#   Sy = 0.5
#
# Rotação:
#   -30 graus
#
# Translação:
#   (4.1, 0)
# ------------------------------------------------------------

M_painel_direito = matriz_trs(
    tx=4.1,
    ty=0,
    angulo=-30,
    sx=3,
    sy=0.5
)


# ------------------------------------------------------------
# ANTENA
# ------------------------------------------------------------
#
# Escala:
#   Sx = 0.5
#   Sy = 0.5
#
# Rotação:
#   0 graus
#
# Translação:
#   (0, 2)
# ------------------------------------------------------------

M_antena = matriz_trs(
    tx=0,
    ty=2,
    angulo=0,
    sx=0.5,
    sy=0.5
)


# ============================================================
# 4. APLICAÇÃO DAS TRANSFORMAÇÕES
# ============================================================

corpo_sru = transformar(
    corpo,
    M_corpo
)


painel_esquerdo_sru = transformar(
    painel,
    M_painel_esquerdo
)


painel_direito_sru = transformar(
    painel,
    M_painel_direito
)


antena_sru = transformar(
    antena,
    M_antena
)


# ============================================================
# 5. MOSTRAR AS MATRIZES CALCULADAS
# ============================================================

print()
print("=" * 65)
print("ATIVIDADE — TRANSFORMAÇÕES TRS")
print("=" * 65)


print()
print("MATRIZ DO CORPO:")
print(
    np.round(
        M_corpo,
        4
    )
)


print()
print("MATRIZ DO PAINEL ESQUERDO:")
print(
    np.round(
        M_painel_esquerdo,
        4
    )
)


print()
print("MATRIZ DO PAINEL DIREITO:")
print(
    np.round(
        M_painel_direito,
        4
    )
)


print()
print("MATRIZ DA ANTENA:")
print(
    np.round(
        M_antena,
        4
    )
)


# ============================================================
# 6. MOSTRAR OS VÉRTICES NO SRU
# ============================================================

print()
print("=" * 65)
print("VÉRTICES APÓS AS TRANSFORMAÇÕES — SRU")
print("=" * 65)


print()
print("CORPO:")
print(
    np.round(
        corpo_sru.T,
        3
    )
)


print()
print("PAINEL ESQUERDO:")
print(
    np.round(
        painel_esquerdo_sru.T,
        3
    )
)


print()
print("PAINEL DIREITO:")
print(
    np.round(
        painel_direito_sru.T,
        3
    )
)


print()
print("ANTENA:")
print(
    np.round(
        antena_sru.T,
        3
    )
)


# ============================================================
# 7. SEGUNDA IMAGEM — SRU
# ============================================================
#
# Agora mostramos o resultado final depois das transformações.
# ============================================================

fig_sru, ax_sru = plt.subplots(
    figsize=(10, 7)
)


# Corpo
desenhar_objeto(
    ax_sru,
    corpo_sru,
    "Corpo principal"
)


# Painel esquerdo
desenhar_objeto(
    ax_sru,
    painel_esquerdo_sru,
    "Painel esquerdo"
)


# Painel direito
desenhar_objeto(
    ax_sru,
    painel_direito_sru,
    "Painel direito"
)


# Antena
desenhar_objeto(
    ax_sru,
    antena_sru,
    "Antena"
)


configurar_eixos(
    ax_sru,
    "2. Satélite montado no SRU — após transformações TRS",
    limite=8
)


ax_sru.legend()

plt.tight_layout()


# Salva na mesma pasta do programa
arquivo_sru = PASTA_SAIDA / "satelite_sru.png"

fig_sru.savefig(
    arquivo_sru,
    dpi=160,
    bbox_inches="tight"
)


# ============================================================
# 8. MOSTRAR AS DUAS IMAGENS
# ============================================================

plt.show()


# ============================================================
# 9. INFORMAÇÃO FINAL
# ============================================================

print()
print("=" * 65)
print("ARQUIVOS GERADOS")
print("=" * 65)

print()
print(f"SRO: {arquivo_sro}")

print()
print(f"SRU: {arquivo_sru}")

print()
print("Programa executado com sucesso!")
