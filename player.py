from mundo import *
import pygame

# Classe player
class Player():
    def __init__(self, x, y):
        # Imagem do player
        self.imagem_player = pygame.image.load('Sources/personagem_andar_0.png')
        self.rect = self.imagem_player.get_rect()

        # Criação da lista com sprites
        self.direcao = 1
        self.sprites_direita = []
        self.sprites_esquerda = []
        
        for num in range(4):
            img_right = pygame.image.load(f'Sources/personagem_andar_{num}.png')
            self.sprites_direita.append(pygame.transform.scale(img_right, (30, 60)))
            img_left = pygame.transform.flip(img_right, True, False)
            self.sprites_esquerda.append(pygame.transform.scale(img_left, (30, 60)))

        self.index = 0

        # Coordenadas iniciais do player
        self.rect.x = x
        self.rect.y = y
        
        # Propriedades de movimento
        self.gravity = 0
        self.speed_x = 5
        self.speed_y = 0
        self.no_chao = False  

        # Medidas da imagem
        self.width = self.imagem_player.get_width()
        self.height = self.imagem_player.get_height()

    def update(self, mundo, estado_cafe):
        # Importa lista de plataformas
        plataformas = mundo.plataformas

        # Checa se as teclas estão pressionadas
        key = pygame.key.get_pressed()
                
        if key[pygame.K_a]:
            self.direcao = 0
            self.rect.x -= self.speed_x
            self.index += 0.2
            if self.index >= len(self.sprites_esquerda):
                self.index = 1
            self.imagem_player = self.sprites_esquerda[int(self.index)]

        if key[pygame.K_d]:
            self.direcao = 1
            self.rect.x += self.speed_x
            self.index += 0.2
            if self.index >= len(self.sprites_direita):
                self.index = 1
            self.imagem_player = self.sprites_direita[int(self.index)]

        if not key[pygame.K_a] and not key[pygame.K_d]:
            self.index = 0
            self.imagem_player = self.sprites_direita[self.index] if self.direcao == 1 else self.sprites_esquerda[self.index]

        # Aplica gravidade
        self.gravity += 1
        if self.gravity > 15:
            self.gravity = 15

        # Configura o botao do pulo
        if key[pygame.K_w] and self.no_chao:
            self.gravity = -13
            self.no_chao = False 

            if estado_cafe == True:
                self.gravity = -17

        #Rects para verificar colisão com plataformas e obstáculos
        rect_foot = pygame.Rect(self.rect.x+10, self.rect.y + 60, self.width-20, 1)
        rect_head = pygame.Rect(self.rect.x+10, self.rect.y, self.width-20, 1)
        rect_left = pygame.Rect(self.rect.x, self.rect.y+8, 1, self.height-13)
        rect_right = pygame.Rect(self.rect.x+29, self.rect.y+8, 1, self.height-13)


        pygame.draw.rect(tela, (0, 0, 0), rect_foot)
        pygame.draw.rect(tela, (255, 0, 0), rect_head)
        pygame.draw.rect(tela, (0, 255, 0), rect_left)
        pygame.draw.rect(tela, (0, 0, 255), rect_right)



        # Verifica colisoes com plataformas
        self.no_chao = False
        for plataforma_ in plataformas: #Falta adicionar obstaculos a essa lista

            #Colisão no pé da personagem
            if plataforma_[1].colliderect(rect_foot.x, rect_foot.y, rect_foot.width, rect_foot.height):

                if self.gravity > 0:  # Falling
                    self.rect.bottom = plataforma_[1].top
                    self.gravity = 0
                    self.no_chao = True  
            
            #Colisão na cabeça da personagem
            if plataforma_[1].colliderect(rect_head.x, rect_head.y, rect_head.width, rect_head.height):
                if self.gravity < 0:  
                    self.rect.top = plataforma_[1].bottom
                    self.gravity = 0  


            #Se a colisão ocorrer à esquerda do personagem
            if plataforma_[1].colliderect(rect_left.x, rect_left.y, rect_left.width, rect_left.height):
                
                print("esquerda")
                self.rect.left = plataforma_[1].right

            #Se a colisão ocorrer à direita do personagem
            if plataforma_[1].colliderect(rect_right.x, rect_right.y, rect_right.width, rect_right.height):

                print("direita")
                self.rect.right = plataforma_[1].left

        # Aplica gravidade a velocidade
        if not self.no_chao:
            self.rect.y += self.gravity

        # Limita o movimento do boneco
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 1025:
            self.rect.right = 1025
        if self.rect.top < 0:
            self.rect.top = 0
            self.gravity = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600
            self.no_chao = True 

        # Atualiza a tela
        tela.blit(self.imagem_player, self.rect)