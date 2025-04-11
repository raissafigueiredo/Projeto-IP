import pygame
from pygame.locals import *
from mundo import *
from jogador import *
from globais import *
from telas import *
from maisum import Jogo
pygame.init()


# Configura a janela
icone = jogador_img
pygame.display.set_icon(icone)
pygame.display.set_caption('Água e fogo no CIn, sem água e sem fogo')


relogio = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
running = True
tela_menu = True
tela_instrucoes = False
tela_creditos = False
perdeu = False
ganhou = False

mundo = Mundo(mapa)
jogador = Jogador(75, 515)

jogo = Jogo(mundo, mapa, jogador, tela)


while running:
    if tela_menu == True:
        tela_menu, tela_instrucoes, tela_creditos = menu()

    if tela_creditos == True:
        tela_menu, tela_creditos = creditos()

    if tela_instrucoes == True:
        tela_menu, tela_instrucoes = instrucoes()

    # Lógica de funcionamento do jogo
    if perdeu == False and tela_menu == False and tela_instrucoes == False and tela_creditos == False:
        jogo.jogar(mundo, mapa, jogador, tela)

    if ganhou == True:
        tela.blit(tela_ganhou, (0, 0))
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:
            jogo.reiniciar(mundo, mapa, jogador)

    if perdeu == True:
        tela.blit(tela_perdeu, (0, 0))
        key = pygame.key.get_pressed()

        if key[pygame.K_r]:
            jogo.reiniciar(mundo, mapa, jogador)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
