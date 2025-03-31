import pygame
from pygame.locals import *
from mundo import Mundo
from coletaveis import *
from player import Player

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




class Obstaculos:

  def __init__(self, posicao, tamanho, img_path):
    self.posicao = posicao
    self.tamanho = tamanho


    self.img_path = img_path
    self.img_arq = pygame.image.load(self.img_path)
    self.img_arq_final = pygame.transform.scale(self.img_arq, (40,40))
    self.obstaculo = self.img_arq_final.get_rect(topleft = (self.posicao))
    tela.blit(self.img_arq_final, self.obstaculo)

  
  def colisao(self, livros_um, placa_um, livros_dois, placa_dois):
    colisao = None

    #Transformando os métodos em variáveis
    var_livros_um = livros_um
    var_placa_um = placa_um
    var_livros_dois = livros_dois
    var_placa_dois = placa_dois

    if self.obstaculo.colliderect(jogador.rect):

      # Colisão lateral esquerda do obstáculo
      if self.obstaculo.left < jogador.rect.right and self.obstaculo.right > jogador.rect.right:
        print("esquerda")
        colisao = "à esquerda do obstaculo"

      # Colisão lateral direita do obstáculo
      elif self.obstaculo.right > jogador.rect.left:
        print("direita")
        colisao = "à direita do obstaculo"

      # Colisão superior ao obstáculo
      if self.obstaculo.top < jogador.rect.bottom  and self.obstaculo.top > jogador.rect.top:
        
        #Para os dois primeiros obstáculos, que estão no mesmo nível
        if (self == var_livros_um or self == var_placa_um) and jogador.rect.bottom < 390:
          print("cima")
          colisao = "à cima do obstaculo"

        #Para o obstáculo que está no nível do meio
        elif self == var_livros_dois and jogador.rect.bottom < 249:
          print("cima")
          colisao = "à cima do obstaculo"
        
        #Para o obstáculo mais à cima
        elif self == var_placa_dois and jogador.rect.bottom < 100:
          print("cima")
          colisao = "à cima do obstaculo"

    return colisao





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

    #Testando a colisão com cada obstáculo
    colisao_livro_um = livros_um.colisao(livros_um, placa_um, livros_dois, placa_dois)
    colisao_placa_um = placa_um.colisao(livros_um, placa_um, livros_dois, placa_dois)
    colisao_livro_dois = livros_dois.colisao(livros_um, placa_um, livros_dois, placa_dois)
    colisao_placa_dois = placa_dois.colisao(livros_um, placa_um, livros_dois, placa_dois)


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