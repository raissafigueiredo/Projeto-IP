import pygame
from pygame.locals import *
from jogador import *
pygame.init()


class Jogo:

    def reiniciar(self, mundo, mapa, jogador):

        global perdeu, ganhou
        self.mundo = mundo
        self.jogador =  jogador

        # Reinicia todas as variáveis 
        self.qtd_moedas = 0
        self.qtd_cracha = 0
        self.qtd_cafe = 0
        self.cracha_coletado = False
        self.pulo_cafe = False
        self.counter =  10
        
        # Recria o mundo e todos os objetos
        mundo.reiniciar(mapa)
        jogador.reiniciar(75, 515)
        
        # Atualiza os grupos de sprites
        self.grupo_obstaculos = mundo.obstaculos
        self.grupo_moedas = mundo.moedas
        self.cracha = mundo.crachas
        self.catraca = mundo.catracas
        self.cafe = mundo.cafes


    def jogar(self, mundo, mapa, jogador, tela):

        global perdeu, ganhou
        perdeu =  False
        ganhou = False

        while not perdeu and not ganhou:

            relogio = pygame.time.Clock()
            pygame.time.set_timer(pygame.USEREVENT, 1000)
            
            relogio.tick(42)
            self.mundo.draw()
            self.grupo_moedas.draw(tela)
            self.cracha.draw(tela)
            self.cafe.draw(tela)
            draw_score(tela, self.qtd_moedas, self.qtd_cracha, self.qtd_cafe, self.pulo_cafe, self.counter)

            self.jogador.update(mundo, self.pulo_cafe)

            # checa se o jogador tocou na água:
            if pygame.sprite.spritecollide(self.jogador, self.grupo_obstaculos, False):
                perdeu = True

            # checa se o jogador chegou até a catraca:
            if pygame.sprite.spritecollide(self.jogador, self.catraca, False):
                if self.cracha_coletado:
                    ganhou = True
                else:
                    draw_texto('Você precisa do crachá!',
                            fonte_1, BRANCO, 650, 550, tela)

            # checa se alguma moeda foi coletada
            if pygame.sprite.spritecollide(self.jogador, self.grupo_moedas, True):
                self.qtd_moedas += 1

            # checa se o crachá foi coletado
            if pygame.sprite.spritecollide(self.jogador, self.cracha, True):
                self.cracha_coletado = True
                self.qtd_cracha += 1

            # checa se o café foi coletado
            if pygame.sprite.spritecollide(self.jogador, self.cafe, True):
                self.pulo_cafe = True
                self.qtd_cafe += 1
                self.counter = 10

            # pulo do café
            if self.pulo_cafe == True:
                for e in pygame.event.get():
                    if e.type == pygame.USEREVENT:
                        self.counter -= 1
                        if self.counter == 0:
                            self.pulo_cafe = False

            # se a pessoa quiser reiniciar a qualquer momento
            key = pygame.key.get_pressed()
            if key[pygame.K_r]:
                self.reiniciar(mundo, mapa, jogador)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            pygame.display.update()

    def __init__(self, mundo, mapa, jogador, tela):
        self.reiniciar(mundo, mapa, jogador)
            