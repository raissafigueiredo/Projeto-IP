import pygame
from mundo import Mundo

tela = pygame.display.set_mode((700, 450))
player_path = 'Sources/player.png'

class Player():
    def __init__(self, x,y):
                img = pygame.image.load(player_path)
                self.image = pygame.transform.scale(img, (60,60))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.vel_y = 0
                self.jumped = False
                self.index = 0
                self.width = self.image.get_width()
                self.height = self.image.get_height()
                self.direction = 0

    def update(self, dx, dy, colisao_livro_um, colisao_placa_um, colisao_livro_dois, colisao_placa_dois):
                plataformas = Mundo().plataformas
                self.dx = dx
                self.dy = dy
                self.colisao_livro_um = colisao_livro_um
                self.colisao_placa_um = colisao_placa_um
                self.colisao_livro_dois = colisao_livro_dois
                self.colisao_placa_dois = colisao_placa_dois
                key = pygame.key.get_pressed()

                walk_cooldown = 5

                if key[pygame.K_SPACE] and self.jumped == False:
                    self.vel_y = -10
                    self.jumped = True

                if key[pygame.K_SPACE] == False:
                    self.jumped = False
                

                
                if key[pygame.K_LEFT]:

                    if self.colisao_livro_um == "à direita do obstaculo" or self.colisao_placa_um == "à direita do obstaculo" or self.colisao_livro_dois == "à direita do obstaculo" or self.colisao_placa_dois == "à direita do obstaculo":
                     pass
                    else:
                     self.dx -= 5




                if key[pygame.K_RIGHT]:
                            
                    if self.colisao_livro_um == "à esquerda do obstaculo" or self.colisao_placa_um == "à esquerda do obstaculo" or self.colisao_livro_dois == "à esquerda do obstaculo" or self.colisao_placa_dois == "à esquerda do obstaculo":
                     pass
                    else:
                        self.dx += 5
                         
                self.vel_y += 1
                
                if self.vel_y > 10:
                    self.vel_y = 10

                
                if colisao_livro_um == "à cima do obstaculo" or colisao_placa_um == "à cima do obstaculo" or colisao_livro_dois == "à cima do obstaculo" or colisao_placa_dois == "à cima do obstaculo":
                    pass
                else:
                    self.dy += self.vel_y

                self.rect.x += self.dx

                if colisao_livro_um == "à cima do obstaculo":
                    pass
                else:
                    self.rect.y += self.dy
            
                for plataforma_ in plataformas:
                    if plataforma_[1].colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                        self.dx = 0

                    if plataforma_[1].colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                        if self.vel_y < 0:
                                self.dy = plataforma_[1].bottom - self.rect.top
                                self.vel_y = 0

                        elif self.vel_y >= 0:
                                self.dy = plataforma_[1].top - self.rect.bottom
                                self.vel_y = 0

                self.rect.x += self.dx
                self.rect.y += self.dy

                if self.rect.bottom > 700: #largura da tela
                        self.rect.bottom = 450 #altura da tela
                        self.dy = 0

                                       
                tela.blit(self.image, self.rect)
