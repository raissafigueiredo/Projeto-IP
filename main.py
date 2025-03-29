#Looping separado
import pygame
from pygame.locals import *
from Player_class import Player
from Obstaculos_class import Obstaculos
from Looping_class import Looping

pygame.init()
icone_path = 'Sources/player.png'
icone = pygame.image.load(icone_path)
pygame.display.set_icon(icone)
pygame.display.set_caption('Água e fogo no CIn, sem água e sem fogo')

iniciar = Looping()
iniciar.f_looping()