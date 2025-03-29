import pygame

class Screen():
  def __init__(self):
    self.largura_tela = 700
    self.altura_tela = 450
    self.tela = pygame.display.set_mode((self.largura_tela, self.altura_tela))
    