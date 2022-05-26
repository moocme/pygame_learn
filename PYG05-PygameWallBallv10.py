# Unit PYG05: Pygame Wall Ball Game Version 10
import sys
import pygame
import pygame.freetype

size = width, height = 600, 400
speed = [1, 1]
COLOR = '#eeeeeeff'
BG_COLOR = '#707070ff'
pos = [230, 160]
fps = 300

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame")
f1 = pygame.freetype.Font("C://Windows//Fonts//FZSTK.TTF", 36)
f1_rect = f1.render_to(screen, pos, "哈喽凯蒂", fgcolor=COLOR, size=50)
f_clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if f1_rect.left < 0 or f1_rect.right > width:
        # if pos[0] < 0 or pos[0] + f1_rect.width > width:
        speed[0] = -speed[0]
    if pos[1] < 0 or pos[1] + f1_rect.height > height:
        speed[1] = -speed[1]
    pos[0] = pos[0] + speed[0]
    pos[1] = pos[1] + speed[1]

    screen.fill(BG_COLOR)
    f1_rect = f1.render_to(screen, pos, "哈喽凯蒂", fgcolor=COLOR, size=50)
    pygame.display.update()
    f_clock.tick(fps)
