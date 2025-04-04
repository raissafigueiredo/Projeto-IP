import pygame
from funcoes import load_imagem

# Definições da tela
LARGURA = 1025
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Definições dos objetos
TAM_COLECIONAVEIS = (25,25)
TAM_OBSTACULOS = (25,25)

# Fontes
fonte_1 = pygame.font.SysFont('Consolas', 20)

# Cores
BRANCO = (250, 250, 250)
PRETO = (0,0,0)
AZUL_CLARO = (117, 179, 250)
VERMELHO = (180, 0,0)

# Assets
cafe_img = load_imagem('cafe.png')
background_img = load_imagem('Cenário.jpeg')
cracha_img = load_imagem('cracha.png')
piso_img = load_imagem('piso.png')
agua_esq_img = load_imagem('agua_esq.png')
agua_dir_img = load_imagem('agua_dir.png')
livro_img = load_imagem('livros.png')
moeda_img = load_imagem('moedas.png')
player_img = load_imagem('personagem_andar_1.png')