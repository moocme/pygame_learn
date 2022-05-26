# Unit PYG02: Pygame Wall Ball Game version 2  节奏型
import sys
import pygame

pygame.init()
size = width, height = 600, 400
speed = [1, 1]
COLOR = 58, 120, 58
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame壁球")
ball = pygame.image.load("images/ball.gif")
ball_rect = ball.get_rect()
fps = 300
f_clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ball_rect = ball_rect.move(speed[0], speed[1])
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(COLOR)
    screen.blit(ball, ball_rect)
    pygame.display.update()
    f_clock.tick(fps)
