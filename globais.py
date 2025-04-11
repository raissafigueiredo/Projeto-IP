import pygame
pygame.init()

# Definições da tela
LARGURA = 1025
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Definições dos objetos
TAM_COLECIONAVEIS = (30, 30)
TAM_AGUA = (50, 25)
TAM_OBSTACULOS = (25, 25)

# Fontes
fonte_1 = pygame.font.SysFont('Consolas', 20)
fonte_cracha = pygame.font.SysFont('Consolas', 10)
fonte_score = pygame.font.SysFont('Consolas', 17)

# Cores
BRANCO = (250, 250, 250)
PRETO = (0, 0, 0)
VERMELHO = (180, 45, 20)


# Funções
##########################################################

def load_imagem(path):
    img = pygame.image.load('Sources/' + path).convert()
    img.set_colorkey((0, 0, 0))
    return img


def draw_texto(texto, fonte, cor, x, y, tela):
    img = fonte.render(texto, True, cor)
    tela.blit(img, (x, y))


def draw_score(tela, qtd_moeda, qtd_cracha, qtd_cafe, cafe_c, cont):
    from objetos import Objetos

    rect = pygame.Rect(0, 0, 240, 40)
    pygame.draw.rect(tela, (BRANCO), rect)
    dummies = pygame.sprite.Group()

    objs = {'moedas':  [20, 20],
            'cracha':  [80, 20], 
            'cafe':    [140, 20], 
            'relogio': [200, 20]}
    
    for obj in objs:
        img = pygame.image.load(f'Sources/{obj}.png')
        objeto = Objetos(img, objs[obj][0], objs[obj][1], (21, 21))
        if obj != 'relogio' or cafe_c == True:
            dummies.add(objeto)

    dummies.draw(tela)
    draw_texto(f'x{qtd_moeda}', fonte_score, PRETO, 36, 14, tela)
    draw_texto(f'x{qtd_cracha}', fonte_score, PRETO, 96, 14, tela)
    draw_texto(f'x{qtd_cafe}', fonte_score, PRETO, 156, 14, tela)
    if cafe_c:
        draw_texto(f'{cont}', fonte_score, PRETO, 216, 14, tela)


#função para reiniciar
def reiniciar_jogo(mundo, mapa, jogador):
    global grupo_obstaculos, grupo_moedas, cracha, cafe, catraca
    global qtd_moedas, qtd_cracha, cracha_coletado, pulo_cafe
    global perdeu, ganhou, counter

    # Reinicia todas as variáveis 
    qtd_moedas = 0
    qtd_cracha = 0
    cracha_coletado = False
    pulo_cafe = False
    perdeu = False
    ganhou = False
    counter = 10   
    
    # Recria o mundo e todos os objetos
    mundo.reiniciar(mapa)
    jogador.reiniciar(75, 515)
    
    # Atualiza os grupos de sprites
    grupo_obstaculos = mundo.obstaculos
    grupo_moedas = mundo.moedas
    cracha = mundo.crachas
    catraca = mundo.catracas
    cafe = mundo.cafes 