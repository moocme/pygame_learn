import sys
import pygame
from random import randrange

# 颜色定义
bg_color = pygame.Color('#6090bbff')
rect_color = pygame.Color('#0095a0ff')
polygon_color = pygame.Color('#209620')
# 图形数据定义
screen_size = 1200, 800
rect_size = 50, 50, 1100, 700

# 时间定义
fps = 1
f_clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('图形绘制')
py_quit = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or py_quit:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                py_quit = True
    screen.fill(bg_color)
    draw_rect = pygame.draw.rect(screen, rect_color, rect_size, randrange(400))
    draw_polygon = pygame.draw.polygon(
        screen, polygon_color, [(randrange(20, 1100), randrange(20, 700)),
                                (randrange(20, 1100), randrange(20, 700)),
                                (randrange(20, 1100), randrange(20, 700)),
                                (randrange(20, 1100), randrange(20, 700)),
                                (randrange(20, 1100), randrange(20, 700)),
                                (randrange(20, 1100), randrange(20, 700)),
                                (randrange(20, 1100), randrange(20, 700))])
    f_clock.tick(fps)
    pygame.display.update()
