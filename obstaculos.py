import pygame
from player import Player
jogador = Player(50, 385)


tela = pygame.display.set_mode((700, 450))



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
      print("444")

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
