from globais import *
from botão import *

def menu():

    inicio = True

    instrucoes_ver = False
    creditos_ver = False

    tela.blit(tela_menu, (0,0))
            
    MOUSE_MENU_POS = pygame.mouse.get_pos()

    iniciar_botao = Botao(botao_img, 900, 400, 'Iniciar', (100, 60), 30)

    instrucoes_botao = Botao(botao_img, 700, 400, 'Instruções', (100, 60), 30)

    creditos_botao = Botao(botao_img, 500, 400, 'Créditos', (100, 60), 30)

    draw_texto(f'MENU', fonte_1, PRETO, 10, 10, tela)

    for botao in [iniciar_botao, instrucoes_botao, creditos_botao]:
        botao.changecolor(MOUSE_MENU_POS, 30)
        botao.uptade(tela)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if iniciar_botao.check_for_input(MOUSE_MENU_POS):
                inicio = False
            if instrucoes_botao.check_for_input(MOUSE_MENU_POS) == True:
                inicio = instrucoes()
                instrucoes_ver = True

            if creditos_botao.check_for_input(MOUSE_MENU_POS) == True:
                inicio = creditos()
                creditos_ver = True
    
    return inicio, instrucoes_ver, creditos_ver

def instrucoes():
    instrucoes_mouse_pos = pygame.mouse.get_pos()

    MOUSE_MENU_POS = pygame.mouse.get_pos()

    tela.fill(PRETO)
    tela.blit(tela_instrucoes, (0,0))

    menu_botao = Botao(botao_img, 200, 100, 'Menu', (96, 33), 30)

    for botao in [menu_botao]:
        botao.changecolor(MOUSE_MENU_POS, 30)
        botao.uptade(tela)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu_botao.check_for_input(MOUSE_MENU_POS):
                inicio = True
                menu()
    return False

def creditos ():
    creditos = True
    while creditos == True:
        iniciar = False
        creditos_mouse_pos = pygame.mouse.get_pos()

        tela.fill(PRETO)
        tela.blit(tela_creditos, (0,0))

        menu_botao = Botao(botao_img, 600, 300, 'Menu', (96, 33), 30)

        menu_botao.changecolor(creditos_mouse_pos, 30)
        menu_botao.uptade(tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_botao.check_for_input(creditos_mouse_pos):
                    #iniciar = True
                    creditos = False
    return True
