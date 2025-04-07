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
grupo_obstaculos = mundo.obstaculos
grupo_moedas = mundo.moedas
cracha = mundo.crachas
catraca = mundo.catracas
cafe = mundo.cafes
cafe_coletado = False
cracha_coletado = False
pulo_cafe = False

#variáveis do temporizador do café
estado_cafe = False
counter, text = 10, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

# Condições do jogo
perdeu = False
ganhou = False

while running:
    if perdeu == False:
        relogio.tick(42)
        mundo.draw()
        grupo_moedas.draw(tela)
        cracha.draw(tela)
        cafe.draw(tela)

        jogador.update(mundo,pulo_cafe)
        
        #checa se o jogador tocou na água:
        if pygame.sprite.spritecollide(jogador, grupo_obstaculos, False):
            perdeu = True
            print('perdeu mane')
            jogador.rect.x = 75
            jogador.rect.y = 515
            
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
            cafe_coletado = True
            qtd_cafe += 1

            #faz a parte do segundo cafe funcionar
            if qtd_cafe > qtd_antiga:
                pulo_cafe = True

            qtd_antiga = qtd_cafe

            #pulo do café
            if pulo_cafe == True:

                for e in pygame.event.get():
                    if e.type == pygame.USEREVENT: 
                        counter -= 1
                        text = str(counter).rjust(3) if counter > 0 else 'boom!'

                        if text == 'boom!':
                            pulo_cafe = False 
                            counter, text = 10, '10'.rjust(3)
                            pygame.time.set_timer(pygame.USEREVENT, 1000)
                    
                    relogio.tick(60)
                draw_texto(f'Tempo: {text}',fonte_1,PRETO,10,70,tela)

        # exibir contagem de itens
        draw_texto(f'Moedas: {qtd_moedas}', fonte_1, PRETO, 10, 10, tela)
        draw_texto(f'Crachá: {qtd_cracha}', fonte_1, PRETO, 10, 30, tela)
        draw_texto(f'Cafés: {qtd_cafe}', fonte_1, PRETO, 10, 50, tela)

        pygame.display.update()

    elif perdeu == True:
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:
            perdeu = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        tela.blit(jogador.imagem_player, jogador.rect)


pygame.quit()
