#7) Usando a biblioteca ‘pygame’, escreva um programa que desenha na tela em posição aleatória um quadrado amarelo de tamanho 50 (cinquenta), 
#toda vez que a tecla espaço for pressionada ou o botão direito for clicado.

import pygame, random
from pygame.locals import *

SQUARE_L = []

WIDTH_S = 800
HEIGHT_S = 600


pygame.init()
SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Questão 07 - AT - Fund. Python - Mariana B. Sukevicz")
running = True

YELLOW = 255, 255, 0
BLACK = 0, 0, 0


class Square:
    def update(self):
        self.height = 50
        self.width = 50
        self.x = random.randint(0, WIDTH_S - self.width)
        self.y = random.randint(0, HEIGHT_S - self.height)
        self.square = pygame.Rect(self.x, self.y, self.height, self.width)

    def draw(self): 
        pygame.draw.rect(SCREEN, YELLOW, self.square, 5)

square = Square()
d_square = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:   
            square = Square()
            square.update()
            SQUARE_L.append(square)
            d_square = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                square = Square()
                square.update()
                SQUARE_L.append(square)
                d_square = True
       
    SCREEN.fill((BLACK))
    if d_square:           
        for square in SQUARE_L:
            square.draw()

    pygame.display.update()


pygame.display.quit()
pygame.quit()
