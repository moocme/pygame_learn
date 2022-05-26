import sys
import pygame
import pygame.sprite

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('pygame sprite')
x, y = 10, 10
LOOP = 28


class Mover(pygame.sprite.Sprite):

    def __init__(self, w, h):
        super(Mover, self).__init__()
        self.image = pygame.Surface((59, 10))
        self.image.fill('#202020ff')
        self.rect = self.image.get_rect(left=w, top=h)

    def update(self):
        self.rect.centerx += 10

    def draw(self, screen):
        screen.blit(self.image, self.rect)


movers = pygame.sprite.Group()
for i in range(LOOP):
    mover = Mover(x, y)
    movers.add(mover)
    y += 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

        elif event.type == pygame.QUIT:
            running = False
    screen.fill('#808080ff')
    movers.update()
    movers.draw(screen)
    pygame.display.update()
    pygame.time.wait(200)
pygame.quit()
sys.exit()
