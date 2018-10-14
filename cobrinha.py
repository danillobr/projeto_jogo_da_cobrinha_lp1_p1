import os
import sys, traceback
import pygame, random
from pygame.locals import *

def finalizar_jogo(parametro1, parametro2, andar, musicaFim):
    if((parametro1 <= 10) or (parametro1 >= 480) or (parametro2 <= 30) or (parametro2 >= 430)):
        #pygame.mixer.music.load("sons/fim.mp3")
        #pygame.mixer.music.play()
        #del cobrinha[0]
        andar = False
        if musicaFim:
            pygame.mixer.music.load("sons/fim.wav")
            pygame.mixer.music.play()
            musicaFim = False
        #som de derrota e retornar para o menu
        return False    
    return True
def cria_campo():
    contaCampo = 30
    while(1==1):
        if(contaCampo <= 420):
            campo.append((10,contaCampo))
        else:
            break
        contaCampo += 10

    contaCampo = 30
    while(1==1):
        if(contaCampo <= 420):
            campo.append((480,contaCampo))
        else:
            break
        contaCampo += 10

    contaCampo = 10
    while(1==1):
        if(contaCampo <= 480):
            campo.append((contaCampo,430))
        else:
            break
        contaCampo += 10

    contaCampo = 10
    while(1==1):
        if(contaCampo <= 480):
            campo.append((contaCampo,30))
        else:
            break
        contaCampo += 10

def cria_comida():
    x = random.randint(20,470)
    y = random.randint(40,420)
    return (x//10 * 10, y//10 * 10)

def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

PRACIMA = 0
DIREITA = 1
PRABAIXO = 2
ESQUERDA = 3

pontuacao = 0

pygame.init()
pygame.mixer.init()
pygame.font.init()

tela = pygame.display.set_mode((500,450))
pygame.display.set_caption('COBRINHA')

campo = []
campoTotal = pygame.Surface((10,10))
campoTotal.fill((255,255,255))

cobrinha = [(200, 200), (210, 200), (220,200)]
cobrinhaCresce = pygame.Surface((10,10))
cobrinhaCresce.fill((255,0,0))

posicaoComida = cria_comida()
comida = pygame.Surface((10,10))
comida.fill((0,0,255))

#textoPerdeu = pygame.font.Font ("fontes / Minecraft.ttf" ,  26)

texto1 = pygame.font.SysFont("Minecraft", 30)
textoPerdeu = texto1.render("VOCE PERDEU!", True, (0, 128, 0))
texto2 = pygame.font.SysFont("Minecraft", 17)
texto_pontuacao = texto2.render("pontuacao: "+str(pontuacao), True, (0, 128, 0))

pygame.mixer.music.load("sons/somFundo.mp3")
pygame.mixer.music.play()

vou_para = ESQUERDA

musicaFim = True

andar = True

tempo = pygame.time.Clock()

while True:
    tempo.tick(10)
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

    if andar:

        if colisao(cobrinha[0], posicaoComida):
            posicaoComida = cria_comida()
            cobrinha.append((0,0))
            pontuacao += 10
            texto_pontuacao = texto2.render("pontuacao: "+str(pontuacao), True, (0, 128, 0))
            pygame.mixer.music.load("sons/comer.mp3")
            pygame.mixer.music.play()
            pygame.display.update()
            pygame.time.delay(500)
            pygame.mixer.music.load("sons/somFundo.mp3")
            pygame.mixer.music.play()

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
    tela.blit(texto_pontuacao, (180, 10))
    for posicaoCampo in campo:
        tela.blit(campoTotal,posicaoCampo)
    tela.blit(comida, posicaoComida)
    for posicaoCobrinha in cobrinha:
        tela.blit(cobrinhaCresce,posicaoCobrinha)

    try:
        andar = finalizar_jogo(cobrinha[0][0], cobrinha[1][1], andar, musicaFim)
    except IndexError:
        andar = finalizar_jogo(10, 30, False, False)

    musicaFim = andar 
    tamanho = len(cobrinha)

    if(andar == False and tamanho > 0):
        del cobrinha[0]
    elif(tamanho == 0):
        tela.blit(textoPerdeu, (120, 150))
    
    pygame.display.update()