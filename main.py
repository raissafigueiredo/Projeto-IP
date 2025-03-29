#Looping separado
import pygame
from pygame.locals import *
from class_Player import Player
from class_Obstaculos import Obstaculos
from class_Looping import Looping

pygame.init()
icone_path = 'Sources/player.png'
icone = pygame.image.load(icone_path)
pygame.display.set_icon(icone)
pygame.display.set_caption('Água e fogo no cin, sem água e fogo')

iniciar = Looping()
iniciar.f_looping()