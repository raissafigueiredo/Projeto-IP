#importa o que é necessario
import pygame
import sys


class Jogo:
    def __init__(self):
        #inicia o mod pygame
        pygame.init()
        pygame.display.set_caption('cin game')


        #define o tamanho da tela
        self.tela = pygame.display.set_mode((1300, 700))


        #define  a taxa de atualizacoes por segundo
        self.clk = pygame.time.Clock()


    def loop(self):
        #main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            #Atualiza o display
            pygame.display.flip()


            #Define a taxa de fps
            self.clk.tick(60)


Jogo().loop()