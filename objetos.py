import pygame
from globais import *

class Objetos(pygame.sprite.Sprite):

    def __init__(self, img, x, y, tamanho): # tamanho recebido como tupla
        pygame.sprite.Sprite.__init__(self) # inicializa a herança do Sprite
        self.image = pygame.transform.scale(img, tamanho)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

