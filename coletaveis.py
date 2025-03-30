import pygame

moeda_path = 'Sources/coin_spin.gif'

class Moeda(pygame.sprite.Sprite):
    moedas = pygame.sprite.Group()

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(moeda_path)
        self.image = pygame.transform.scale(img, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    
    def update(self, jogador):
        if pygame.sprite.spritecollide(self, jogador, True):
            qtd_moedas += 1
            print(qtd_moedas)
