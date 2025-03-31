import pygame
from pygame.locals import *
from mundo import Mundo
from coletaveis import *
from player import Player
pygame.init()

# Configura a janela
icone_path = 'Sources/player.png'
icone = pygame.image.load(icone_path)
pygame.display.set_icon(icone)
pygame.display.set_caption('Água e fogo no CIn, sem água e sem fogo')

tela = pygame.display.set_mode((700, 450))
jogador = Player(100, 100)
mundo = Mundo()

relogio = pygame.time.Clock()
running = True

# Inicializa as variáveis dos coletáveis
qtd_moedas = 0
grupo_moedas = mundo.moedas
cracha = mundo.crachas
cafe = mundo.cafes
cafe_coletado = False
cracha_coletado = False

while running:

    relogio.tick(40)
    mundo.draw()
    jogador.update()
    grupo_moedas.draw(tela)
    cracha.draw(tela)
    cafe.draw(tela)

    # checa se alguma moeda foi coletada
    if pygame.sprite.spritecollide(jogador, grupo_moedas, True):
        qtd_moedas += 1
        print(qtd_moedas)

    # checa o crachá foi coletado
    if pygame.sprite.spritecollide(jogador, cracha, True):
        cracha_coletado = True
        print(cracha_coletado)

    # checa o café foi coletado
    if pygame.sprite.spritecollide(jogador, cafe, True):
        cafe_coletado = True
        print(cafe_coletado)

    # fechar jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()