import pygame
from objetos import *
from obstaculos import *
from mapa import level
pygame.init()

LARGURA = 1025
ALTURA = 600
tile_size = 25
mapa = level()

class Mundo():

    def __init__(self, mapa):
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        self.background = pygame.transform.scale(background_img, (1025, 600))
        self.plataformas = []
        self.moedas = pygame.sprite.Group()
        self.cafes = pygame.sprite.Group()
        self.crachas = pygame.sprite.Group()
        self.obstaculos = pygame.sprite.Group()

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
                if tile == 2: # Adiciona uma pilha de livros
                    livros = Objetos('livros', cont_cols * tile_size, cont_linhas * tile_size)
                    self.obstaculos.add(livros)
                if tile == 3: # Adiciona uma fonte
                    fonte = Objetos('fonte', cont_cols * tile_size, cont_linhas * tile_size)
                    self.obstaculos.add(fonte)
                if tile == 4: # Adiciona uma moeda
                    moeda = Objetos('moeda', cont_cols * tile_size, cont_linhas * tile_size)
                    self.moedas.add(moeda)
                if tile == 5: # Adiciona um café
                    cafe = Objetos('café', cont_cols * tile_size, cont_linhas * tile_size)
                    self.cafes.add(cafe)
                if tile == 6: # Adiciona um crachá
                    cracha = Objetos('crachá', cont_cols * tile_size, cont_linhas * tile_size)
                    self.crachas.add(cracha)
                cont_cols += 1
            cont_linhas += 1
   
    def draw(self):
        tela.fill((250, 250, 250))
        for plat in self.plataformas:
            tela.blit(plat[0], plat[1])
        self.obstaculos.draw(tela)