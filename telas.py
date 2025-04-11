import pygame
import sys
from botão import Botao
from assets import *
from globais import *

tela = pygame.display.set_mode((1025, 600))

def menu():

    inicio = True
    instrucoes_ver = False
    creditos_ver = False

    nome = pygame.transform.scale(nome_jogo, (440, 210))

    tela.blit(tela_menu, (0,0))
    tela.blit(nome, (450,150))
            
    mouse_pos = pygame.mouse.get_pos()

    iniciar_botao = Botao(botao_img, 460, 400, 'Iniciar', (190, 70), 30)
    instrucoes_botao = Botao(botao_img, 670, 400, 'Instruções', (190, 70), 30)
    creditos_botao = Botao(botao_img, 880, 400, 'Créditos', (190, 70), 30)

    for botao in [iniciar_botao, instrucoes_botao, creditos_botao]:
        botao.changecolor(mouse_pos, 30)
        botao.uptade(tela)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if iniciar_botao.check_for_input(mouse_pos):
                inicio = False
            if instrucoes_botao.check_for_input(mouse_pos) == True:
                inicio = instrucoes()
                instrucoes_ver = True

            if creditos_botao.check_for_input(mouse_pos) == True:
                inicio = creditos()
                creditos_ver = True
    
    return inicio, instrucoes_ver, creditos_ver


def instrucoes():

    inicio = False
    instrucao = True

    mouse_pos = pygame.mouse.get_pos()

    tela.fill(PRETO)
    tela.blit(tela_instrucoes, (0,0))

    menu_botao = Botao(botao_img, 950, 47, 'Menu', (96, 33), 30)

    for botao in [menu_botao]:
        botao.changecolor(mouse_pos, 30)
        botao.uptade(tela)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu_botao.check_for_input(mouse_pos):
                inicio = True
                instrucao = False

    return inicio, instrucao


def creditos ():
    
    iniciar = False
    creditos = True
    creditos_mouse_pos = pygame.mouse.get_pos()

    tela.fill(PRETO)
    tela.blit(tela_creditos, (0,0))

    menu_botao = Botao(botao_img, 950, 47, 'Menu', (96, 33), 30)
    menu_botao.changecolor(creditos_mouse_pos, 30)
    menu_botao.uptade(tela)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu_botao.check_for_input(creditos_mouse_pos):
                iniciar = True
                creditos = False

    return iniciar, creditos
