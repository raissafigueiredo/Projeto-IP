import pygame
from Mundo_class import Mundo
from Player_class import Player

player = Player(100, 100)
relogio = pygame.time.Clock()

class Looping():

  def __init__(self):

    self.run = True
    self.mundo = Mundo()

  def f_looping(self):

    while self.run:

      relogio.tick(40)
      self.mundo.draw()
      player.update()

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              self.run = False

      pygame.display.update()

    pygame.quit()