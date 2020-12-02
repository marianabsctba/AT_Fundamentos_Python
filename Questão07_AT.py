#7) Usando a biblioteca ‘pygame’, escreva um programa que desenha na tela em posição aleatória um quadrado amarelo de tamanho 50 (cinquenta), 
#toda vez que a tecla espaço for pressionada ou o botão direito for clicado.

import pygame, random
from pygame.locals import *

square_l = []


width_s = 800
weight_s = 600


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Questão 07 - AT - Fund. Python - Mariana B. Sukevicz")
running = True

yellow = 255, 255, 0
black = 0, 0, 0


class Square:
    def update(self):
        self.height = 50
        self.width = 50
        self.x = random.randint(0, width_s - self.width)
        self.y = random.randint(0, weight_s - self.height)
        self.square = pygame.Rect(self.x, self.y, self.height, self.width)

    def draw(self): 
        pygame.draw.rect(screen, yellow, self.square)

square = Square()
d_square = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:   
            square = Square()
            square.update()
            square_l.append(square)
            d_square = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                square = Square()
                square.update()
                square_l.append(square)
                d_square = True
       
    screen.fill((black))
    if d_square:           
        for square in square_l:
            square.draw()

    pygame.display.flip()


pygame.quit()
