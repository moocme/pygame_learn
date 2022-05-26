import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('pygame')

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            print('MouseMotion:', event.pos, event.rel, event.buttons)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('MouseButtonDown:', event.pos, event.button)
        elif event.type == pygame.MOUSEBUTTONUP:
            print('MouseButtonUp:', event.pos, event.button)
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((128, 168, 128))
    pygame.display.flip()
