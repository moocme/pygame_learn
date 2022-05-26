import sys
import pygame
from math import pi
# from math import radians


def iradians(x):
    return x * pi / 180


pygame.init()
screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption('图形绘制')
screen.fill(('#3030aaff'))
t_rect = pygame.draw.rect(screen, '#55aa55ff', (1200, 600, 160, 90), 30)
t_polygon = pygame.draw.polygon(screen, '#aa5555ff', [(150, 50), (245, 119),
                                                      (209, 231), (91, 231),
                                                      (55, 119)], 10)
t_circle = pygame.draw.circle(screen, '#aaaa5580', (600, 400), 100, 80)
t_ellipse = pygame.draw.ellipse(screen, '#55aaaaff', (120, 500, 400, 300), 20)
# t_arc = pygame.draw.arc(screen, '#bbbbbbff', (900, 50, 400, 400), 0, 0.5 * pi, 5)
# t_arc = pygame.draw.arc(screen, '#bbbbbbff', (900, 50, 400, 400), radians(45)radians(135), 5)
t_arc = pygame.draw.arc(screen, '#ff0000ff', (900, 50, 400, 400), iradians(15), iradians(165), 3)
t_line = pygame.draw.line(screen, '#aaaaaaff', (0, 750), (1600, 750), 2)
t_lines = pygame.draw.lines(screen, '#bbbbbbff', True, [(300, 300), (800, 100), (900, 700)], 4)
t_aaline = pygame.draw.aaline(screen, '#ccccccff', (100, 800), (1500, 100), 1)
t_aalines = pygame.draw.aalines(screen, '#ddddddff', True, [(800, 300), (1200, 800), (1400, 700)], 1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    pygame.display.update()
