import pygame
import sys
from pygame.locals import *
from mundo import *
from player import *
from funcoes import draw_texto

pygame.init()

relogio = pygame.time.Clock()
fonte = pygame.font.SysFont("comic sans", 15, True, False)

running = True
mundo = Mundo(mapa)
jogador = Player(75, 515)

# Configura a janela
icone = player_img
pygame.display.set_icon(icone)
pygame.display.set_caption('Água e fogo no CIn, sem água e sem fogo')


# Inicializa as variáveis dos coletáveis
qtd_moedas = 0
qtd_cracha = 0
qtd_cafe = 0
grupo_moedas = mundo.moedas
cracha = mundo.crachas
cafe = mundo.cafes
cafe_coletado = False
cracha_coletado = False
pulo_cafe = False

while running:

    relogio.tick(42)
    mundo.draw()
    grupo_moedas.draw(tela)
    cracha.draw(tela)
    cafe.draw(tela)

    jogador.update(mundo,pulo_cafe)

    # checa se alguma moeda foi coletada
    if pygame.sprite.spritecollide(jogador, grupo_moedas, True):
        qtd_moedas += 1

    # checa se o crachá foi coletado
    if pygame.sprite.spritecollide(jogador, cracha, True):
        cracha_coletado = True
        qtd_cracha += 1

    # checa se o café foi coletado
    if pygame.sprite.spritecollide(jogador, cafe, True):
        cafe_coletado = True
        pulo_cafe = True
        qtd_cafe += 1


    # exibir contagem de itens
    draw_texto(f'Moedas: {qtd_moedas}', fonte_1, PRETO, 10, 10, tela)
    draw_texto(f'Crachá: {qtd_cracha}', fonte_1, PRETO, 10, 30, tela)
    draw_texto(f'Cafés: {qtd_cafe}', fonte_1, PRETO, 10, 50, tela)


    # fechar jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

pygame.quit()
