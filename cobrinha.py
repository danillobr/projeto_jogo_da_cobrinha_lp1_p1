import pygame, random
from pygame.locals import *

def cria_campo_esquerdo():
    contaCampo = 30
    while(1==1):
        if(contaCampo <= 420):
            campo_esquerdo.append((10,contaCampo))
        else:
            break
        contaCampo += 10

def cria_campo_direito():
    contaCampo = 30
    while(1==1):
        if(contaCampo <= 420):
            campo_direito.append((480,contaCampo))
        else:
            break
        contaCampo += 10

def cria_campo_abaixo():
    contaCampo = 10
    while(1==1):
        if(contaCampo <= 480):
            campo_direito.append((contaCampo,430))
        else:
            break
        contaCampo += 10

def cria_campo_acima():
    contaCampo = 10
    while(1==1):
        if(contaCampo <= 480):
            campo_direito.append((contaCampo,30))
        else:
            break
        contaCampo += 10

def cria_campo():
    cria_campo_esquerdo()
    cria_campo_direito()
    cria_campo_abaixo()
    cria_campo_acima()

def cria_comida():
    x = random.randint(30,470)
    y = random.randint(30,420)
    return (x//10 * 10, y//10 * 10)

def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

PRACIMA = 0
DIREITA = 1
PRABAIXO = 2
ESQUERDA = 3

pygame.init()

tela = pygame.display.set_mode((500,450))
pygame.display.set_caption('COBRINHA')

campo_direito = []
campoTotal_direito = pygame.Surface((10,10))
campoTotal_direito.fill((255,255,255))

campo_esquerdo = []
campoTotal_esquerdo = pygame.Surface((10,10))
campoTotal_esquerdo.fill((255,255,255))

campo_abaixo = []
campoTotal_abaixo = pygame.Surface((10,10))
campoTotal_abaixo.fill((255,255,255))

campo_acima = []
campoTotal_acima = pygame.Surface((10,10))
campoTotal_acima.fill((255,255,255))

cobrinha = [(200, 200), (210, 200), (220,200)]
cobrinhaCresce = pygame.Surface((10,10))
cobrinhaCresce.fill((255,0,0))

posicaoComida = cria_comida()
comida = pygame.Surface((10,10))
comida.fill((0,0,255))

texto = pygame.font.get_default_font()
textoPerdeu = pygame.font.SysFont(texto, 50)

pygame.font.init()

vou_para = ESQUERDA

clock = pygame.time.Clock()

while True:
    clock.tick(10)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()

        if evento.type == KEYDOWN:
            if evento.key == K_UP:
                vou_para = PRACIMA
            if evento.key == K_DOWN:
                vou_para = PRABAIXO
            if evento.key == K_LEFT:
                vou_para = ESQUERDA
            if evento.key == K_RIGHT:
                vou_para = DIREITA

    if colisao(cobrinha[0], posicaoComida):
        posicaoComida = cria_comida()
        cobrinha.append((0,0))

    for i in range(len(cobrinha) - 1, 0, -1):
        cobrinha[i] = (cobrinha[i-1][0], cobrinha[i-1][1])

    if vou_para == PRACIMA:
        cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] - 10)
    if vou_para == PRABAIXO:
        cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] + 10)
    if vou_para == DIREITA:
        cobrinha[0] = (cobrinha[0][0] + 10, cobrinha[0][1])
    if vou_para == ESQUERDA:
        cobrinha[0] = (cobrinha[0][0] - 10, cobrinha[0][1])

    cria_campo()

    tela.fill((0,0,0))
    for posicaoCampo in campo_esquerdo:
        tela.blit(campoTotal_esquerdo,posicaoCampo)
    for posicaoCampo in campo_direito:
        tela.blit(campoTotal_direito,posicaoCampo)
    #text = textoPerdeu.render('Texto Perdeu deu certo!', 1, (255,255,255))
    tela.blit(comida, posicaoComida)
    #tela.blit(text, (150, 150))
    for posicaoCobri in cobrinha:
        tela.blit(cobrinhaCresce,posicaoCobri)

    pygame.display.update()
