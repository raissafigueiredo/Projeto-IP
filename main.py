import pygame
from pygame.locals import *
from mundo import Mundo
from coletaveis import *
from player import Player
from obstaculos import Obstaculos

pygame.init()

relogio = pygame.time.Clock()
livro_path = "Sources/livros.png"
placa_path = "Sources/fonte.png"


# Configura a janela
icone_path = 'Sources/player.png'
icone = pygame.image.load(icone_path)
pygame.display.set_icon(icone)
pygame.display.set_caption('Água e fogo no CIn, sem água e sem fogo')
tela = pygame.display.set_mode((700, 450))


running = True
mundo = Mundo()
jogador = Player(50, 385)


# Inicializa as variáveis dos coletáveis
qtd_moedas = 0
grupo_moedas = mundo.moedas
cracha = mundo.crachas
cafe = mundo.cafes
cafe_coletado = False
cracha_coletado = False

while running:

    relogio.tick(40)
    mundo.draw()
    grupo_moedas.draw(tela)
    cracha.draw(tela)
    cafe.draw(tela)

    livros_um = Obstaculos((360, 385), (40, 40), livro_path)
    placa_um = Obstaculos((540, 385), (40, 40), placa_path)
    livros_dois = Obstaculos((415, 234), (40, 40), livro_path)
    placa_dois = Obstaculos((410, 83), (40, 40), placa_path)

    colisao_livro_um = livros_um.colisao()
    colisao_placa_um = placa_um.colisao()
    colisao_livro_dois = livros_dois.colisao()
    colisao_placa_dois = placa_dois.colisao()
    jogador.update(0,0, colisao_livro_um, colisao_placa_um, colisao_livro_dois, colisao_placa_dois)


    # checa se alguma moeda foi coletada
    if pygame.sprite.spritecollide(jogador, grupo_moedas, True):
        qtd_moedas += 1
        print(qtd_moedas)

    # checa o crachá foi coletado
    if pygame.sprite.spritecollide(jogador, cracha, True):
        cracha_coletado = True
        print(cracha_coletado)

    # checa o café foi coletado
    if pygame.sprite.spritecollide(jogador, cafe, True):
        cafe_coletado = True
        print(cafe_coletado)

    # fechar jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()