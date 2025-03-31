import pygame
from colecionaveis import *
from obstaculos import *
from mapa import level
pygame.init()

LARGURA = 1000
ALTURA = 700
tile_size = 25
mapa = level()

class Mundo():

    def __init__(self, mapa):
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        self.background = pygame.transform.scale(background_img, (1000, 700))
        self.plataformas = []
        self.moedas = pygame.sprite.Group()
        self.cafes = pygame.sprite.Group()
        self.crachas = pygame.sprite.Group()

        cont_linhas = 0
        for linha in mapa:
            cont_cols = 0
            for tile in linha:
                if tile == 1: # Adiciona um bloco de piso
                    img = pygame.transform.scale(piso_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = cont_cols * tile_size
                    img_rect.y = cont_linhas * tile_size
                    tile = (img, img_rect)
                    self.plataformas.append(tile)
                cont_cols += 1
            cont_linhas += 1
   
    def draw(self):
        tela.blit(self.background, (0,0))
        for plat in self.plataformas:
            tela.blit(plat[0], plat[1])