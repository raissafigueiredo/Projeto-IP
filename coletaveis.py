import pygame
from screen import Screen

moeda_path = 'Sources/moedas.png'
cafe_path = 'Sources/coffee_espresso.png'
cracha_path = 'Sources/cracha.png'
tela = Screen()


class Moeda(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(moeda_path)
        self.image = pygame.transform.scale(img, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y          


class Cracha(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(cracha_path)
        self.image = pygame.transform.scale(img, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
           

class Cafe(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(cafe_path)
        self.image = pygame.transform.scale(img, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
           