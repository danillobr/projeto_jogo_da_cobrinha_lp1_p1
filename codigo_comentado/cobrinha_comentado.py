import os
import sys, traceback
import pygame, random
from pygame.locals import *

# 2 - incia o loop infinito do jogo e chama a função inicia_jogo()
# 4 - verifica o valor retornado da função inicia_jogo() e 
def jogo(andar,posicaoComida,vou_para,texto_pontuacao,musicaFim,pontuacao):
    pygame.mixer.music.load("sons/somFundoMenu.mp3")
    pygame.mixer.music.play()
    while True:
        if(inicia_jogo()):
            jogo_rodando(andar,posicaoComida,vou_para,texto_pontuacao,musicaFim,pontuacao)

# 3 - verifica quando o "botão" de play foi pressionado e caso isso ocorra a função retornar um valor True para a função jogo()
def inicia_jogo():
    ok = False
    tempo.tick(10)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()

        if evento.type == MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            
            if((x >= 227) and (x <= 380) and (y >= 230) and (y <= 274)):
                pygame.mixer.music.load("sons/aperta_o_botao_jogar.mp3")
                pygame.mixer.music.play()
                pygame.time.delay(500)
                ok = True

    tela.blit(imagemMenu, (0,0))
    pygame.display.update()

    return ok

# 5 - Cria a cobra e inicia o som do jogo e a gameplay no while.
def jogo_rodando(andar, posicaoComida, vou_para, texto_pontuacao, musicaFim, pontuacao):
    cobrinha = [(200, 200), (210, 200), (220,200)]
    cobrinhaCresce = pygame.Surface((10,10))
    cobrinhaCresce.fill((255,0,0))
    pontuacao = 0
    texto2 = pygame.font.SysFont("Minecraft", 17)
    texto_pontuacao = texto2.render("SCORE: "+str(pontuacao), True, (0, 128, 0))
    
    pygame.mixer.music.load("sons/somFundo.mp3")
    pygame.mixer.music.play()
    
    campo_nao_foi_criado = True
# 1º for é para escoha da direção; 2º movimentação onde os valores dentro da dupla da cobrinha vão se alternando conforme ela se movimenta; 3º mostra o campo; 4º insere a cobrinha no campo.
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

# Este 1º if verifica se ocorre movimentação; 2º if serve para acrescentar "mais tamanho" a cobrinha quando ela entra em contato com a comida; 3º impede que o campo seja criado mais de uma vez.

        if andar:

            if colisaoComida(cobrinha[0], posicaoComida):
                posicaoComida = cria_comida()
                cobrinha.append((0,0))
                pontuacao += 10
                texto_pontuacao = texto2.render("SCORE: "+str(pontuacao), True, (0, 128, 0))
                #pygame.mixer.music.load("sons/comer.mp3")
                #pygame.mixer.music.play()
                #pygame.display.update()
                #pygame.time.delay(500)
                #pygame.mixer.music.load("sons/somFundo.mp3")
                #pygame.mixer.music.play()

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

        if(campo_nao_foi_criado):
            cria_campo()
            campo_nao_foi_criado = False

        tela.blit(imagemFundo, (0,0))
        tela.blit(texto_pontuacao, (220, 10))
        for posicaoCampo in campo:
            tela.blit(campoTotal,posicaoCampo)
        tela.blit(comida, posicaoComida)
        for posicaoCobrinha in cobrinha:
            tela.blit(cobrinhaCresce,posicaoCobrinha)
# Este try serve para 'destruir' de fato a cobrinha em todas suas partes.
        try:
            andar = finalizar_jogo(cobrinha[0][0], cobrinha[1][1], andar, musicaFim)
        except IndexError:
            andar = finalizar_jogo(10, 30, False, False)

        musicaFim = andar 
        tamanho = len(cobrinha)
# Esse if serve para aniquilar a cobrinha parte por parte até seu final e exibir ela morrendo e agonizando, dps q ela morrer vc pode clicar em qq area da tela com o mouse para jogar novamente.
        if(andar == False and tamanho > 0):
            del cobrinha[0]
        elif(tamanho == 0):
            tela.blit(textoPerdeu, (170, 150))
            for evento in pygame.event.get():
                if evento.type == MOUSEBUTTONDOWN:
                    jogo(andar,posicaoComida,vou_para,texto_pontuacao,musicaFim,pontuacao)

        pygame.display.update()

def finalizar_jogo(parametro1, parametro2, andar, musicaFim):
    if((parametro1 <= 10) or (parametro1 >= 480) or (parametro2 <= 30) or (parametro2 >= 430)):
        if musicaFim:
            pygame.mixer.music.load("sons/fim.wav")
            pygame.mixer.music.play()
            musicaFim = False
        return False  
    return True

def cria_campo():
    contaCampo = 30
    while(True):
        if(contaCampo <= 420):
            campo.append((10,contaCampo))
        else:
            break
        contaCampo += 10

    contaCampo = 30
    while(True):
        if(contaCampo <= 420):
            campo.append((480,contaCampo))
        else:
            break
        contaCampo += 10

    contaCampo = 10
    while(True):
        if(contaCampo <= 480):
            campo.append((contaCampo,430))
        else:
            break
        contaCampo += 10

    contaCampo = 10
    while(True):
        if(contaCampo <= 480):
            campo.append((contaCampo,30))
        else:
            break
        contaCampo += 10

def cria_comida():
    x = random.randint(20,470)
    y = random.randint(40,420)
    return (x//10 * 10, y//10 * 10)

def colisaoComida(c1, c2):
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
pygame.display.set_caption('SNAKE')

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
textoPerdeu = texto1.render("YOU LOSE!", True, (0, 128, 0))
texto2 = pygame.font.SysFont("Minecraft", 17)
texto_pontuacao = texto2.render("SCORE: "+str(pontuacao), True, (0, 128, 0))
texto3 = pygame.font.SysFont("Minecraft", 30)
textoInicial = texto3.render("PLAY!", True, (0, 128, 0))

vou_para = ESQUERDA

musicaFim = True

andar = True

tempo = pygame.time.Clock()

imagemFundo = pygame.image.load("imagens/fundo.png")
imagemMenu = pygame.image.load("imagens/menu.png")

# 1 - chama a função jogo() e passa os parametros: andar,posicaoComida,vou_para,texto_pontuacao,musicaFim,pontuacao
jogo(andar,posicaoComida,vou_para,texto_pontuacao,musicaFim,pontuacao)
