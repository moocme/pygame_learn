# Unit PYG02: Pygame Wall Ball Game version 1  展示型
import sys
import pygame

pygame.init()
size = width, height = 600, 400
speed = [1, 1]
BLACK = 0, 0, 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame壁球")

ball = pygame.image.load('pygame_learn/images/ball.gif')
ball_rect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ball_rect = ball_rect.move(speed[0], speed[1])
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = - speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = - speed[1]

    screen.fill(BLACK)
    screen.blit(ball, ball_rect)
    pygame.display.update()
