import pygame
from pygame.locals import *
from Player_class import Player
from Screen_class import Screen
from Mundo_class import Mundo

pygame.init()
relogio = pygame.time.Clock()
icone_path = "Sources/player.png"
livro_path = "Sources/livros.png"
placa_path = "Sources/fonte.png"
icone = pygame.image.load(icone_path)
pygame.display.set_icon(icone)
tela = Screen()
player = Player(50, 385)
pygame.display.set_caption('Água e fogo no cin, sem água e fogo')


class Obstaculos:

  def __init__(self, posicao, tamanho, img_path):
    self.posicao = posicao
    self.tamanho = tamanho
    self.obstaculo = pygame.draw.rect(tela.tela, (178, 19, 18), (self.posicao, self.tamanho))


    self.img_path = img_path
    self.img_arq = pygame.image.load(self.img_path)
    self.img_arq_final = pygame.transform.scale(self.img_arq, (40,40))
    self.obstaculo = self.img_arq_final.get_rect(topleft = (self.posicao))
    tela.tela.blit(self.img_arq_final, self.obstaculo)

  
  def colisao(self):
    colisao = None

    if self.obstaculo.colliderect(player.rect):
      
      if self.obstaculo.left < player.rect.right and self.obstaculo.right > player.rect.right:
        print ("esquerda")
        colisao = "à esquerda do obstaculo"

      elif self.obstaculo.right > player.rect.left:
        print("direita")
        colisao = "à direita do obstaculo"

      elif self.obstaculo.top > player.rect.bottom:
        print("cima")
        colisao = "à cima do obstaculo"
    return colisao



livros_um = Obstaculos((360, 385), (40, 40), livro_path)
placa_um = Obstaculos((540, 385), (40, 40,), placa_path)
livros_dois = Obstaculos((450, 250), (40, 40), livro_path)
placa_dois = Obstaculos((420, 180), (40, 40), placa_path)


run = True
mundo = Mundo()

while run:

  relogio.tick(40)
  mundo.draw()
  
  contador = 0
  
  livros_um.__init__((360, 385), (40, 40), livro_path)
  placa_um.__init__((540, 385), (40, 40), placa_path)
  livros_dois.__init__((450, 234), (40, 40), livro_path)
  placa_dois.__init__((410, 83), (40, 40), placa_path)

  colisao_livro_um = livros_um.colisao()
  colisao_placa_um = placa_um.colisao()
  colisao_livro_dois = livros_dois.colisao()
  colisao_placa_dois = placa_dois.colisao()
  player.update(0,0, colisao_livro_um, colisao_placa_um, colisao_livro_dois, colisao_placa_dois)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()