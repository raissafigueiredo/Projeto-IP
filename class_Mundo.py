import pygame

from class_Screen import Screen

tela = Screen()

cenario_path = 'Sources/Cenário.jpeg'
escada_path = 'Sources/Escada.jpeg'
plataf_path = 'Sources/Plataforma.jpeg'
chao_path = 'Sources/Chão.jpeg'

class Mundo():
    def __init__(self):
        self.plataformas = []


        self.bg_img = pygame.image.load(cenario_path)
        self.bg_img = pygame.transform.scale(self.bg_img, (700, 450))

        self.escada = pygame.image.load(escada_path)
        self.escada = pygame.transform.scale(self.escada, (87.5, 25))
        self.escada_rect = self.escada.get_rect()
        self.escada_rect.x = 0
        self.escada_rect.y = 250
        tupla_escada = (self.escada, self.escada_rect)
        self.plataformas.append(tupla_escada)

        self.plataforma = pygame.image.load(plataf_path)
        self.plataforma = pygame.transform.scale(self.plataforma, (612.5, 25))
        self.plataforma_rect = self.plataforma.get_rect()
        self.plataforma_rect.x = 0
        self.plataforma_rect.y = 274
        tupla_plataforma = (self.plataforma, self.plataforma_rect)
        self.plataformas.append(tupla_plataforma)

        self.plataforma1 = pygame.image.load(plataf_path)
        self.plataforma1 = pygame.transform.scale(self.plataforma1, (612.5, 25))
        self.plataforma1_rect = self.plataforma.get_rect()
        self.plataforma1_rect.x = 90
        self.plataforma1_rect.y = 123.5
        tupla_plataforma1 = (self.plataforma1, self.plataforma1_rect)
        self.plataformas.append(tupla_plataforma1)

        self.chao = pygame.image.load(chao_path)
        self.chao = pygame.transform.scale(self.chao, (700, 22.5))
        self.chao_rect = self.chao.get_rect()
        self.chao_rect.x = 0
        self.chao_rect.y = 427.5
        tupla_chao = (self.chao, self.chao_rect)
        self.plataformas.append(tupla_chao)

    def draw(self):

        tela.tela.blit(self.bg_img, (0,0))
        tela.tela.blit(self.escada, self.escada_rect)
        tela.tela.blit(self.plataforma, self.plataforma_rect)
        tela.tela.blit(self.plataforma1, self.plataforma1_rect)
        tela.tela.blit(self.chao, self.chao_rect)