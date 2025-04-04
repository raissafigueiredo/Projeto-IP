import pygame
from objetos import *
from globais import *
from mapa import level
pygame.init()

tile_size = 25
mapa = level()


class Mundo():

    def __init__(self, mapa):
        self.background = pygame.transform.scale(background_img, (LARGURA, ALTURA))
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
                    livro = pygame.transform.scale(livro_img, (TAM_OBSTACULOS))
                    livro_rect = livro.get_rect()
                    livro_rect.x = cont_cols * tile_size +12.3
                    livro_rect.y = cont_linhas * tile_size+12.3
                    tile = (TAM_OBSTACULOS)
                    self.plataformas.append((livro, livro_rect))
                if tile == 3: # Adiciona água da esquerda
                    agua_esq = Objetos(agua_esq_img, cont_cols * tile_size+12.3, cont_linhas * tile_size+12.3, TAM_OBSTACULOS)
                    self.obstaculos.add(agua_esq)
                if tile == 7: # Adiciona água da direita
                    agua_dir = Objetos(agua_dir_img, cont_cols * tile_size+12.3, cont_linhas * tile_size+12.3, TAM_OBSTACULOS)
                    self.obstaculos.add(agua_dir)
                if tile == 4: # Adiciona uma moeda
                    moeda = Objetos(moeda_img, cont_cols * tile_size, cont_linhas * tile_size, TAM_COLECIONAVEIS)
                    self.moedas.add(moeda)
                if tile == 5: # Adiciona um café
                    cafe = Objetos(cafe_img, cont_cols * tile_size, cont_linhas * tile_size, TAM_COLECIONAVEIS)
                    self.cafes.add(cafe)
                if tile == 6: # Adiciona um crachá
                    cracha = Objetos(cracha_img, cont_cols * tile_size, cont_linhas * tile_size, TAM_COLECIONAVEIS)
                    self.crachas.add(cracha)
                cont_cols += 1
            cont_linhas += 1
   
    def draw(self):
        tela.fill(AZUL_CLARO)
        for plat in self.plataformas:
            tela.blit(plat[0], plat[1])
        self.obstaculos.draw(tela)
