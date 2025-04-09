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
perdeu = False
ganhou = False

#função para reiniciar
def reiniciar_jogo():
    global mundo, jogador, grupo_obstaculos, grupo_moedas, cracha, cafe, catraca
    global qtd_moedas, qtd_cracha, qtd_cafe, cafe_coletado, cracha_coletado, pulo_cafe
    global perdeu, ganhou, counter, text
    
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
    qtd_cafe = 0
    cafe_coletado = False
    cracha_coletado = False
    pulo_cafe = False
    perdeu = False
    ganhou = False
    
    # Reinicia o temporizador
    counter, text = 10, '10'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)

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
inicio = True

#variáveis do temporizador do café
estado_cafe = False
counter, text = 10, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)


while running:
    if inicio == True:
        tela.blit(instrucoes_img, (0,0))
        key = pygame.key.get_pressed()
        if key[pygame.K_s]:
            inicio = False


    if perdeu == False and inicio == False:
        relogio.tick(42)
        mundo.draw()
        grupo_moedas.draw(tela)
        cracha.draw(tela)
        cafe.draw(tela)

        jogador.update(mundo, pulo_cafe)
        
        #checa se o jogador tocou na água:
        if pygame.sprite.spritecollide(jogador, grupo_obstaculos, False):
            perdeu = True
            print('perdeu mane')
            jogador.rect.x = 75
            jogador.rect.y = 515

        #checa se o jogador chegou até a catraca:
        if pygame.sprite.spritecollide(jogador, catraca, False):
            if cracha_coletado:
                ganhou =  True
                print('ganhou ebarr!')
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
            cafe_coletado = True
            pulo_cafe = True
            qtd_cafe += 1

            counter = 10
            text = str(counter).rjust(3)
            pygame.time.set_timer(pygame.USEREVENT, 1000)  # Reinicia o timer

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

        # se a pessoa quiser reiniciar a qualquer momento
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:

            reiniciar_jogo()

    if ganhou == True:
        tela.blit(win_img, (0,0))
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:

            reiniciar_jogo()
            ganhou = False


    if perdeu == True :
        tela.blit(game_over_img, (0,0))
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:

            reiniciar_jogo()
            perdeu = False
        
    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        tela.blit(jogador.imagem_player, jogador.rect)

    



pygame.quit()
