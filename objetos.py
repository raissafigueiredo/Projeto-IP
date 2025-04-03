import pygame
from globais import *

"""class Objetos(pygame.sprite.Sprite):

    def __init__(self, tipo, x, y, img):
        pygame.sprite.Sprite.__init__(self) # inicializa a herança do Sprite
        self.tipo = tipo

        if tipo == 'moeda':
            self.image = pygame.transform.scale(moeda_img, (50,50))
        if tipo == 'café':
            self.image = pygame.transform.scale(cafe_img, (50,50))
        if tipo == 'crachá':
            self.image = pygame.transform.scale(cracha_img, (50,50))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)   """



class Objetos(pygame.sprite.Sprite):

    def __init__(self, img, x, y, tamanho): # tamanho recebido como tupla
        pygame.sprite.Sprite.__init__(self) # inicializa a herança do Sprite
        self.image = pygame.transform.scale(img, tamanho)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
  