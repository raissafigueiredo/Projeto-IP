import pygame
from Player_class import Player
from Screen_class import Screen

tela = Screen()

class Obstaculos:

  def __init__(self):
    self.obstaculo = pygame.draw.react(tela.tela, (255,0,0), (400,400, 40, 40))