import sys
import pygame
import pygame.freetype

pygame.init()
screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption('文字绘制')
screen.fill('#808080ff')

fo_1 = pygame.freetype.Font('fonts//Alter-Bridge-2.ttf')
fo_2 = pygame.freetype.Font('fonts//Drifttype-0-2.ttf')
fo_rect = fo_1.render_to(screen, (50, 50), 'pygame', fgcolor='#bbbbbbff', bgcolor=None, rotation=45, size=120)
fo_2_sr = fo_2.render('python', fgcolor='#ccccccff', bgcolor=None, rotation=0, size=120)

quit_t = True
while quit_t:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_t = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit_t = False
                break
    screen.blit(fo_2_sr[0], (150, 225))
    pygame.display.update()
pygame.quit()
sys.exit()
