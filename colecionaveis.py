import pygame
from assets import *

moedas = pygame.sprite.Group()
cafes = pygame.sprite.Group()
crachas = pygame.sprite.Group()

class Colecionaveis(pygame.sprite.Sprite):

    def __init__(self, tipo, x, y):
        pygame.sprite.Sprite.__init__(self) # inicializa a herança do Sprite
        self.tipo = tipo

        if tipo == 'moeda':
            self.imagem = pygame.transform.scale(moeda_img, (50,50))
        if tipo == 'café':
            self.imagem = pygame.transform.scale(cafe_img, (50,50))
        if tipo == 'crachá':
            self.imagem = pygame.transform.scale(cracha_img, (50,50))

        self.rect = self.imagem.get_rect()
        self.rect.center = (x, y)        