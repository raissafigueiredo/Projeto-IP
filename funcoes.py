import pygame
from globais import *
pygame.init()

BASE_IMG_PATH = 'Sources/'

class Botao():
    def __init__(self, imagem, fonte, x_pos, y_pos, texto_input):
        self.imagem = imagem
        self.fonte = fonte
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.imagem.get_rect(center=(self.x_pos, self.y_pos)) #centro do botão na pos x e y
        self.texto_input = texto_input
        self.texto = self.fonte.render(self.texto_input, True, "white")
        self.texto_rect = self.texto.get_rect(center = (self.x_pos, self.y_pos)) #texto que vê na tela


    def uptade(self, tela): #uptade method - colocar botões na tela
        tela.blit(self.imagem, self.rect) 
        tela.blit(self.texto, self.texto_rect)

    def check_for_input(self, posicao): #onde o mouse clica
        if posicao[0] in range(self.rect.left, self.rect.right) and posicao[1] in range(self.rect.top, self.rect.bottom): #0=x e 1=y
            print("botao pressionado")

    def changecolor(self, posicao):
        if posicao[0] in range(self.rect.left, self.rect.right) and posicao[1] in range(self.rect.top, self.rect.bottom): #0=x e 1=y
            self.texto = self.fonte.render(self.texto_input, True, "gray")
        else:
            self.texto = self.fonte.render(self.texto_input, True, "white")