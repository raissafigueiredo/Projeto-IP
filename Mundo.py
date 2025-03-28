import pygame
class Mundo():
    def __init__(self):
        self.plataformas = []

        self.bg_img = pygame.image.load('Cenário.jpeg')
        
        self.escada = pygame.image.load('Escada.png')
        self.escada_rect = self.escada.get_rect()
        self.escada_rect.x = 0
        self.escada_rect.y = 326
        tupla_escada = (self.escada, self.escada_rect)
        self.plataformas.append(tupla_escada)

        self.plataforma = pygame.image.load('Plataforma.jpeg')
        self.plataforma_rect = self.plataforma.get_rect()
        self.plataforma_rect.x = 0
        self.plataforma_rect.y = 350
        tupla_plataforma = (self.plataforma, self.plataforma_rect)
        self.plataformas.append(tupla_plataforma)

        self.plataforma1 = pygame.image.load('Plataforma.jpeg')
        self.plataforma1_rect = self.plataforma.get_rect()
        self.plataforma1_rect.x = 176
        self.plataforma1_rect.y = 650
        tupla_plataforma1 = (self.plataforma1, self.plataforma1_rect)
        self.plataformas.append(tupla_plataforma1)

        self.chao = pygame.image.load('Chão.jpeg')
        self.chao_rect = self.chao.get_rect()
        self.chao_rect.x = 0
        self.chao_rect.y = 50
        tupla_chao = (self.chao, self.chao_rect)
        self.plataformas.append(tupla_chao)

    def draw(self):
        self.tela.blit(self.bg_img, (0,0))
        self.tela.blit(self.escada, self.escada_rect)
        self.tela.blit(self.plataforma, self.plataforma_rect)
        self.tela.blit(self.chao, self.chao_rect)