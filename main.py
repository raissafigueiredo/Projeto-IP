import pygame
import sys
from pygame.locals import *
from mundo import *
from player import *
from obstaculos import *

pygame.init()

relogio = pygame.time.Clock()
fonte = pygame.font.SysFont("comic sans", 15, True, False)

running = True
mundo = Mundo(mapa)

# Configura a janela
icone_path = 'Sources/player.png'
icone = pygame.image.load(icone_path)
pygame.display.set_icon(icone)
pygame.display.set_caption('Água e fogo no CIn, sem água e sem fogo')
tela = mundo.tela


# Inicializa as variáveis dos coletáveis
qtd_moedas = 0
qtd_cracha = 0
qtd_cafe = 0
grupo_moedas = mundo.moedas
cracha = mundo.crachas
cafe = mundo.cafes
cafe_coletado = False
cracha_coletado = False

while running:

    relogio.tick(42)
    mundo.draw()
    grupo_moedas.draw(tela)
    cracha.draw(tela)
    cafe.draw(tela)

    jogador.update(mundo)

    # checa se alguma moeda foi coletada
    if pygame.sprite.spritecollide(jogador, grupo_moedas, True):
        qtd_moedas += 1
        print(qtd_moedas)

    # checa se o crachá foi coletado
    if pygame.sprite.spritecollide(jogador, cracha, True):
        cracha_coletado = True
        qtd_cracha += 1
        print(cracha_coletado)

    # checa se o café foi coletado
    if pygame.sprite.spritecollide(jogador, cafe, True):
        cafe_coletado = True
        qtd_cafe += 1
        print(cafe_coletado)


    #exibir contagem de itens
    mensagem_moeda = f'Moedas: {qtd_moedas}'
    texto_moeda = fonte.render(mensagem_moeda, False, (255, 255, 255))

    mensagem_cracha = f'Crachá: {qtd_cracha}'
    texto_cracha = fonte.render(mensagem_cracha, False, (255, 255, 255))

    mensagem_cafe = f'Cafés: {qtd_cafe}'
    texto_cafe = fonte.render(mensagem_cafe, False, (255, 255, 255))

    tela.blit(texto_moeda, (10, 10))
    tela.blit(texto_cracha, (10, 30))
    tela.blit(texto_cafe, (10, 50))

    # fechar jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

pygame.quit()
