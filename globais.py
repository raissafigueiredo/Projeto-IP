import pygame
from objetos import Objetos
pygame.init()

# Definições da tela
LARGURA = 1025
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Definições dos objetos
TAM_COLECIONAVEIS = (30,30)
TAM_AGUA = (50,25)
TAM_OBSTACULOS = (25,25)

# Fontes
fonte_1 = pygame.font.SysFont('Consolas', 20)
fonte_cracha = pygame.font.SysFont('Consolas', 10)
fonte_score =  pygame.font.SysFont('Consolas', 17)

# Cores
BRANCO = (250, 250, 250)
PRETO = (0,0,0)
AZUL_CLARO = (117, 179, 250)
VERMELHO = (180, 0,0)
VERMELHO_TESTE = (180,45,20)


# Funções
def load_imagem(path):
    img = pygame.image.load('Sources/' + path).convert()
    img.set_colorkey((0,0,0))
    return img

def draw_texto(texto, fonte, cor, x, y, tela):
    img = fonte.render(texto, True, cor)
    tela.blit(img, (x,y))

def draw_score(tela, qtd_moeda, qtd_cracha, cafe_c, cont):
    rect = pygame.Rect(0, 0, 180, 40)
    pygame.draw.rect(tela, (BRANCO), rect)
    dummies = pygame.sprite.Group()
    objs = {'moedas': [20, 20, qtd_moeda],'cracha': [80, 20, qtd_cracha], 'cafe': [140, 20, cafe_c]}
    for obj in objs:
        img = pygame.image.load(f'Sources/{obj}.png')
        objeto = Objetos(img, objs[obj][0], objs[obj][1], (21,21))
        if obj != 'cafe' or cafe_c == True:
            dummies.add(objeto)
    dummies.draw(tela)
    draw_texto(f'x{qtd_moeda}', fonte_score, PRETO, 36, 14, tela)
    draw_texto(f'x{qtd_cracha}', fonte_score, PRETO, 96, 14, tela)
    if cafe_c:
        draw_texto(f'{cont}', fonte_score, PRETO, 156, 14, tela)


'''    
    moeda_img = pygame.image.load('Sources/moedas.png')
    moeda = pygame.transform.scale(moeda_img, (20, 28))
    moeda_rect = moeda.get_rect()
    pygame.draw'''



# Assets
cafe_img = load_imagem('cafe.png')
background_img = load_imagem('Cenário.jpeg')
cracha_img = load_imagem('cracha.png')
piso_img = load_imagem('piso.png')
livro_img = load_imagem('livros.png')
moeda_img = load_imagem('moedas.png')
player_img = load_imagem('personagem_andar_1.png')
catraca_img = load_imagem('catraca.png')
porta_img = load_imagem('porta.png')
robo_cin_img = load_imagem('robo_cin.png')
janela_img = load_imagem('janela.png')
jeep_img = load_imagem('jeep.png')
agua_img = load_imagem('agua_junta.png')
tela_menu = load_imagem('tela_menu.png')
tela_instrucoes = load_imagem('tela_instrucoes.png')
tela_creditos = load_imagem('tela_creditos.png')
tela_perdeu = load_imagem('tela_perdeu.png')
tela_ganhou = load_imagem('tela_ganhou.png')

porta_img = load_imagem('porta.png')
robo_cin_img = load_imagem('robo_cin.png')
janela_img = load_imagem('janela.png')
jeep_img = load_imagem('jeep.png')

botao_img = load_imagem('botao.png')
