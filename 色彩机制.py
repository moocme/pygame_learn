import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('pygame color')
color = pygame.Color('#323232ff')
N = 10


# print(dir(color))
def set_color(c, n):
    c += n
    return 0 if c < 0 else (255 if c > 255 else c)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_r) and (event.mod & pygame.KMOD_SHIFT):
                color.r = set_color(color.r, N)
            elif (event.key == pygame.K_g) and (event.mod & pygame.KMOD_SHIFT):
                color.g = set_color(color.g, N)
            elif (event.key == pygame.K_b) and (event.mod & pygame.KMOD_SHIFT):
                color.b = set_color(color.b, N)
            elif (event.key == pygame.K_r) and (event.key & pygame.K_RCTRL):
                color.r = set_color(color.r, -N)
            elif (event.key == pygame.K_g) and (event.mod & pygame.KMOD_CTRL):
                color.g = set_color(color.g, -N)
            elif (event.key == pygame.K_b) and (event.mod & pygame.KMOD_CTRL):
                color.b = set_color(color.b, -N)
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    screen.fill(color)
    pygame.display.update()
