import pygame, random, math

w = 800
h = 600

BLACK = 0, 0, 0
WHITE = 255, 255, 255
HOVER_COLOR = 50, 70, 90

square_list = []

pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.font.init()
clock = pygame.time.Clock()

running = True

CLOCK_TICK = 20

rad = 100
rx = w // 2
ry = rad
a = (rx, ry)

class Square():
    def __init__(self):
        self.w = 60
        self.h = 30
        self.x = random.randint(0, w - self.w)
        self.y = random.randint(20, h - self.h)
        self.s_a = pygame.Rect(self.x, self.y, self.w, self.h)
        self.color = (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))

    def drawSquare(self, screen):
        pygame.draw.rect(screen, self.color, self.s_a)
        

def drawCircle(rad, rx, ry):
    pygame.draw.circle(screen, HOVER_COLOR, (rx, ry), rad)
    font = pygame.font.SysFont('Times New Roman', 20)
    text = font.render("CLIQUE AQUI!", 1, WHITE)
    show_text = (rx - (rad // 2), ry - 5)
    screen.blit(text, show_text)
    
    
while running:
    show = True
    screen.fill(WHITE)
    
    for q in square_list:
        q.drawSquare(screen)
    for event in pygame.event.get():       
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            click = pygame.mouse.get_pos()
            collision_p = math.hypot(click[0] - rx, click[1] - ry)
            if collision_p <= rad:
                s = Square()
                s.drawSquare(screen)
                for s_s in square_list:
                    if s_s.s_a.colliderect(s.s_a):
                        square_list.remove(s_s)
                        show = False
                if show:
                    square_list.append(s)

    circle = drawCircle(rad, rx, ry)
    pygame.display.update()

    clock.tick(CLOCK_TICK)

pygame.display.quit()
pygame.quit()
