import sys
import pygame
import pygame.sprite

moves = [0, 0]
SPEED = 3
flag = 0
turn = False

pygame.init()
bg = pygame.image.load('images/rycb.jpg')
bg_rect = bg.get_rect()
dragon = pygame.image.load('images/long.png')
dragon_rect = dragon.get_rect()
screen = pygame.display.set_mode((bg_rect.width, bg_rect.bottom))
pygame.display.set_caption('背景图片')

# 声音模块
pygame.mixer.init()
pygame.mixer.music.load('sounds/theicegiants.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(loops=-1)

sound = pygame.mixer.Sound('sounds/epic.mp3')
sound.set_volume(0.2)


running = True
while running:
    if flag == 10:
        dragon = pygame.image.load('images/long_next.png')
    if flag == 20:
        dragon = pygame.image.load('images/long.png')
        flag = 0
    flag += 1
    if turn:
        loong = pygame.transform.flip(dragon, True, False)
    else:
        loong = dragon

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sound.play(loops=-1)
            if event.key == pygame.K_RIGHT:
                moves[0] += SPEED
                turn = False
            if event.key == pygame.K_LEFT:
                moves[0] -= SPEED
                turn = True
            if event.key == pygame.K_UP:
                moves[1] -= SPEED
            if event.key == pygame.K_DOWN:
                moves[1] += SPEED
            if event.key == pygame.K_q:
                running = False
        elif event.type == pygame.KEYUP:
            sound.stop()
            moves = [0, 0]
        elif event.type == pygame.QUIT:
            running = False
    # screen.fill('#808080ff')
    screen.blit(bg, bg_rect)
    dragon_rect = dragon_rect.move(moves)
    screen.blit(loong, dragon_rect)
    pygame.display.update()
    pygame.time.Clock().tick(60)
pygame.quit()
sys.exit()
