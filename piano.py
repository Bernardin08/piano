import time
import pygame
from pygame.locals import * #está importando coisas necessarias para lidar com gráficos

# Inicialização do Pygame
pygame.init() #inicializa o programa no pygame

# Definindo as dimensões da janela
largura = 800
altura = 200
tamanho_tecla = 60

# Definindo cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Criando a janela
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Piano Simples")

# Carregando sons das teclas

notas = [K_d,K_f,K_g,K_a,K_j,K_h,K_g,K_d,K_a,K_g,K_g,K_f,K_s,K_d,K_a,K_s,K_g,K_d,K_f,K_g,K_a,K_j,K_h,K_a,K_a]
duracoes = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

sons = {
    K_a: pygame.mixer.Sound("piano/do.wav"),
    K_s: pygame.mixer.Sound("piano/re.wav"),
    K_d: pygame.mixer.Sound("piano/mi.wav"),
    K_f: pygame.mixer.Sound("piano/fa.wav"),
    K_g: pygame.mixer.Sound("piano/sol.wav"),
    K_h: pygame.mixer.Sound("piano/la.wav"),
    K_j: pygame.mixer.Sound("piano/si.wav")

}

def tocar_melodia(notas, duracoes):
    for nota, duracao in zip(notas, duracoes):
        sons[nota].play()
        time.sleep(duracao * 0.5)

tocar_melodia(notas, duracoes)


# Loop principal
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            executando = False
        elif evento.type == KEYDOWN:
            if evento.key in sons:
                sons[evento.key].play()

    # Desenhar o piano na tela
    janela.fill(branco)
    for i, (tecla, som) in enumerate(sons.items()):
        pygame.draw.rect(janela, preto if i % 2 == 0 else branco, (i * tamanho_tecla, 0, tamanho_tecla, altura))
    pygame.display.flip()

# Finalizando o Pygame
pygame.quit()

