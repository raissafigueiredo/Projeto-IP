import pygame
import sys
from pygame.locals import *
from mundo import *
from player import *
from botão import Botao
from globais import *
from telas import *

pygame.init()


# Configura a janela
icone = player_img
pygame.display.set_icon(icone)
pygame.display.set_caption('Água e fogo no CIn, sem água e sem fogo')


relogio = pygame.time.Clock()
running = True
mundo = Mundo(mapa)
jogador = Player(75, 515)
perdeu = False
ganhou = False

#função para reiniciar
def reiniciar_jogo():
    global mundo, jogador, grupo_obstaculos, grupo_moedas, cracha, cafe, catraca
    global qtd_moedas, qtd_cracha, cracha_coletado, pulo_cafe
    global perdeu, ganhou, counter
    
    # Recria o mundo e todos os objetos
    mundo = Mundo(mapa)
    jogador = Player(75, 515)
    
    # Atualiza os grupos de sprites
    grupo_obstaculos = mundo.obstaculos
    grupo_moedas = mundo.moedas
    cracha = mundo.crachas
    catraca = mundo.catracas
    cafe = mundo.cafes
    
    # Reinicia todas as variáveis 
    qtd_moedas = 0
    qtd_cracha = 0
    cracha_coletado = False
    pulo_cafe = False
    perdeu = False
    ganhou = False
    
    # Reinicia o temporizador
    counter = 10
    pygame.time.set_timer(pygame.USEREVENT, 1000)


# Inicializa as variáveis dos coletáveis
qtd_moedas = 0
qtd_cracha = 0
grupo_obstaculos = mundo.obstaculos
grupo_moedas = mundo.moedas
cracha = mundo.crachas
catraca = mundo.catracas
cafe = mundo.cafes
cracha_coletado = False
pulo_cafe = False
inicio = True

#variáveis do temporizador do café
estado_cafe = False
counter = 10
pygame.time.set_timer(pygame.USEREVENT, 1000)

instrucoes_ver = False
creditos_ver = False

while running:
    if inicio == True:
        inicio, instrucoes_ver, creditos_ver = menu()
    
    if creditos_ver == True:
        inicio, creditos_ver = creditos()

    if instrucoes_ver == True:
        inicio, instrucoes_ver = instrucoes()


    # Lógica de funcionamento do jogo            
    if perdeu == False and inicio == False and instrucoes_ver == False and creditos_ver == False:
        relogio.tick(42)
        mundo.draw()
        grupo_moedas.draw(tela)
        cracha.draw(tela)
        cafe.draw(tela)
        draw_score(tela, qtd_moedas, qtd_cracha, pulo_cafe, counter)

        jogador.update(mundo, pulo_cafe)
        
        #checa se o jogador tocou na água:
        if pygame.sprite.spritecollide(jogador, grupo_obstaculos, False):
            perdeu = True
            jogador.rect.x = 75
            jogador.rect.y = 515

        #checa se o jogador chegou até a catraca:
        if pygame.sprite.spritecollide(jogador, catraca, False):
            if cracha_coletado:
                ganhou =  True
                jogador.rect.x = 75
                jogador.rect.y = 515
            else:
                draw_texto('Você precisa do crachá!', fonte_1, BRANCO, 650, 550, tela)

            
        # checa se alguma moeda foi coletada
        if pygame.sprite.spritecollide(jogador, grupo_moedas, True):
            qtd_moedas += 1

        # checa se o crachá foi coletado
        if pygame.sprite.spritecollide(jogador, cracha, True):
            cracha_coletado = True
            qtd_cracha += 1

        # checa se o café foi coletado
        if pygame.sprite.spritecollide(jogador, cafe, True):
            qtd_antiga = 0
            pulo_cafe = True
            counter = 10
            pygame.time.set_timer(pygame.USEREVENT, 1000)  # Reinicia o timer

        #pulo do café
        if pulo_cafe == True:
            for e in pygame.event.get():
                if e.type == pygame.USEREVENT: 
                    counter -= 1
                    if counter == 0:
                        pulo_cafe = False
                

        # se a pessoa quiser reiniciar a qualquer momento
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:

            reiniciar_jogo()

    if ganhou == True:
        tela.blit(tela_ganhou, (0,0))
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:

            reiniciar_jogo()
            ganhou = False


    if perdeu == True :
        tela.blit(tela_perdeu, (0,0))
        key = pygame.key.get_pressed()

        if key[pygame.K_r]:
            reiniciar_jogo()
            perdeu = False
        
    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
