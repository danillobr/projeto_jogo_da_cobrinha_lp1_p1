import pygame, random
from pygame.locals import *

def cria_comida():
    x = random.randint(0,490)
    y = random.randint(0,440)
    return (x//10 * 10, y//10 * 10)

def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

PRACIMA = 0
DIREITA = 1
PRABAIXO = 2
ESQUERDA = 3

pygame.init()

tela = pygame.display.set_mode((500,450))
pygame.display.set_caption('Cobrinha')

bg = pygame.image.load("bg.jgp")

cobrinha = [(200, 200), (210, 200), (220,200)]
cobrinha_skin = pygame.Surface((10,10))
cobrinha_skin.fill((255,0,0))

posicaoComida = cria_comida()
comida = pygame.Surface((10,10))
comida.fill((0,0,255))

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

    tela.fill((0,0,0))
    tela.blit(comida, posicaoComida)
    for pos in cobrinha:
        tela.blit(cobrinha_skin,pos)

    pygame.display.update()
