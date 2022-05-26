# Unit PYG05: Pygame Wall Ball Game Version 11
import sys
import pygame
import pygame.freetype

size = width, height = 600, 400
speed = [1, 1]
COLOR = '#ccccccff'
BG_COLOR = '#808080ff'
pos = [230, 160]
fps = 300

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame")
f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc", 36)
f1surf, f1rect = f1.render("玛卡巴卡", fgcolor=COLOR, size=50)
fclock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if pos[0] < 0 or pos[0] + f1rect.width > width:
        speed[0] = -speed[0]
    if pos[1] < 0 or pos[1] + f1rect.height > height:
        speed[1] = -speed[1]
    pos[0] = pos[0] + speed[0]
    pos[1] = pos[1] + speed[1]

    screen.fill(BG_COLOR)
    # f1surf, f1rect = f1.render("玛卡巴卡", fgcolor=COLOR, size=50)
    screen.blit(f1surf, (pos[0], pos[1]))
    pygame.display.update()
    fclock.tick(fps)
