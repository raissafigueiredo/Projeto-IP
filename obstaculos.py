import pygame
from pygame.locals import *
from screen import Screen
from mundo import Mundo
from player import Player

jogador = Player(50, 383)
tela = Screen()



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
        if (self == "livros_um" or self == "placa_um") and jogador.rect.bottom < 390:
          print("cima")
          colisao = "à cima do obstaculo"

        #Para o obstáculo que está no nível do meio
        elif self == "livros_dois" and jogador.rect.bottom < 249:
          print("cima")
          colisao = "à cima do obstaculo"
        
        #Para o obstáculo mais à cima
        elif self == "placa_dois" and jogador.rect.bottom < 90:
          print("cima")
          colisao = "à cima do obstaculo"




    return colisao
