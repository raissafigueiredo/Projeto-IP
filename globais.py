import pygame
from funcoes import load_imagem

# Define constantes que vão ser usadas em outras classes

LARGURA = 1025
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
TAM_COLECIONAVEIS = (25,25)
TAM_OBSTACULOS = (50,50)


# Assets
cafe_img = load_imagem('cafe.png')
background_img = load_imagem('Cenário.jpeg')
cracha_img = load_imagem('cracha.png')
piso_img = load_imagem('piso.png')
#fonte_img = load_imagem('fonte.png')
livro_1_img = load_imagem('livros_1.png')
livro_2_img = load_imagem('livros_2.png')
moeda_img = load_imagem('moedas.png')
player_img = load_imagem('personagem_andar_1.png')