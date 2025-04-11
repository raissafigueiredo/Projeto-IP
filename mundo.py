import pygame
from objetos import *
from globais import *
from assets import *
from mapa import level
pygame.init()

tile_size = 25
mapa = level()


class Mundo():

    def reiniciar(self, mapa):
        self.background = pygame.transform.scale(background_img, (LARGURA, ALTURA))
        self.plataformas = []
        self.moedas = pygame.sprite.Group()
        self.cafes = pygame.sprite.Group()
        self.crachas = pygame.sprite.Group()
        self.obstaculos = pygame.sprite.Group()
        self.fundo = pygame.sprite.Group()
        self.catracas = pygame.sprite.Group()

        cont_linhas = 0
        for linha in mapa:
            cont_cols = 0
            for tile in linha:
                if tile == 1:  # Adiciona um bloco de piso
                    img = pygame.transform.scale(
                        piso_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = cont_cols * tile_size
                    img_rect.y = cont_linhas * tile_size
                    tile = (img, img_rect)
                    self.plataformas.append(tile)
                if tile == 2:  # Adiciona uma pilha de livros
                    livro = pygame.transform.scale(livro_img, (TAM_OBSTACULOS))
                    livro_rect = livro.get_rect()
                    livro_rect.x = cont_cols * tile_size + 12.3
                    livro_rect.y = cont_linhas * tile_size
                    self.plataformas.append((livro, livro_rect))
                if tile == 3:  # Adiciona água da esquerda
                    agua = Agua(agua_img, cont_cols * tile_size,
                                cont_linhas * tile_size, TAM_AGUA)
                    self.obstaculos.add(agua)
                if tile == 4:  # Adiciona uma moeda
                    moeda = Objetos(moeda_img, cont_cols * tile_size,
                                    cont_linhas * tile_size, (20, 28))
                    self.moedas.add(moeda)
                if tile == 5:  # Adiciona um café
                    cafe = Objetos(cafe_img, cont_cols * tile_size,
                                   cont_linhas * tile_size, TAM_COLECIONAVEIS)
                    self.cafes.add(cafe)
                if tile == 6:  # Adiciona um crachá
                    cracha = Objetos(cracha_img, cont_cols * tile_size,
                                     cont_linhas * tile_size, TAM_COLECIONAVEIS)
                    self.crachas.add(cracha)
                if tile == 7:  # Adiciona a catraca
                    catraca = Objetos(catraca_img, cont_cols * tile_size,
                                      cont_linhas * tile_size, (40, 50))
                    self.catracas.add(catraca)
                if tile == 8:
                    porta = Objetos(porta_img, cont_cols * tile_size,
                                    cont_linhas * tile_size + 2.2, (62, 95))
                    self.fundo.add(porta)
                if tile == 9:
                    robo_cin = Objetos(robo_cin_img, cont_cols * tile_size,
                                       cont_linhas * tile_size, (130, 90))
                    self.fundo.add(robo_cin)
                if tile == 10:
                    janela = Objetos(janela_img, cont_cols * tile_size,
                                     cont_linhas * tile_size, (86, 52))
                    self.fundo.add(janela)
                if tile == 11:
                    jeep = Objetos(jeep_img, cont_cols * tile_size,
                                   cont_linhas * tile_size, (130, 90))
                    self.fundo.add(jeep)
                if tile == 12:
                    bebedouro = Objetos(bebedouro_img, cont_cols * tile_size,
                                   cont_linhas * tile_size, (26, 100))
                    self.fundo.add(bebedouro)
                if tile == 13:
                    placa = Objetos(placa_img, cont_cols * tile_size,
                                   cont_linhas * tile_size, (75, 53))
                    self.fundo.add(placa)



                cont_cols += 1
            cont_linhas += 1

    def draw(self):
        tela.fill(VERMELHO)
        self.fundo.draw(tela)
        for plat in self.plataformas:
            tela.blit(plat[0], plat[1])
        self.obstaculos.draw(tela)
        self.catracas.draw(tela)

    def __init__(self, mapa):
        self.reiniciar(mapa)
        self.obstaculos.draw(tela)
        self.catracas.draw(tela)

    def __init__(self, mapa):
        self.reiniciar(mapa)
