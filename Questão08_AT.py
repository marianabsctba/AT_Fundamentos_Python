#8) Usando a biblioteca ‘pygame’, escreva um programa que desenha um botão (círculo) com o texto “clique” sobre ele na parte superior da tela. 
#Quando o botão for clicado, ele deve chamar uma função que desenha um retângulo em uma posição aleatória na tela. 
#Caso um retângulo apareça na mesma posição que um já existente, ambos devem ser eliminados.

import pygame, random, math, sys
from pygame.locals import *

W = 800
H = 600

BLACK = 0, 0, 0
WHITE = 255, 255, 255
HOVER_COLOR = 50, 70, 90

RECT_LIST = []

pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Questão 08 - AT - Fund. Python - Mariana B. Sukevicz")
pygame.font.init()
clock = pygame.time.Clock()

running = True

CLOCK_TICK = 100

RAD = 100
RX = W // 2
RY = RAD
A = (RX, RY)

class Rectangle():
    def __init__(self):
        self.W = 60
        self.H = 30
        self.x = random.randint(0, W - self.W)
        self.y = random.randint(20, H - self.H)
        self.s_a = pygame.Rect(self.x, self.y, self.W, self.H)
        self.color = (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))

    def drawRectangle(self, screen):
        pygame.draw.rect(screen, self.color, self.s_a)
        

def drawCircle(RAD, RX, RY):
    pygame.draw.circle(screen, HOVER_COLOR, (RX, RY), RAD)
    font = pygame.font.SysFont('Times New Roman', 20)
    text = font.render("CLIQUE AQUI!", 1, WHITE)
    show_text = (RX - (RAD // 2), RY - 25)
    screen.blit(text, show_text)


while running:
    show = True
    screen.fill(WHITE)
    
    for c in RECT_LIST:
        c.drawRectangle(screen)    
    for event in pygame.event.get():       
        if event.type == pygame.QUIT:
            running = False        
       
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            click = pygame.mouse.get_pos()
            collision_p = math.hypot(click[0] - RX, click[1] - RY)
            if collision_p <= RAD:
                r = Rectangle()
                r.drawRectangle(screen)              
                for r_r in RECT_LIST:
                    if r_r.s_a.colliderect(r.s_a):
                        RECT_LIST.remove(r_r)
                        show = False
                if show:
                    RECT_LIST.append(r)    

    circle = drawCircle(RAD, RX, RY)
    pygame.display.update()

    clock.tick(CLOCK_TICK)

pygame.display.quit()
pygame.quit()
sys.exit()

if __name__ == '__main__':
    main()  
