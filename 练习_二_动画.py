import sys
import pygame


class Bird:

    def __init__(self):
        pygame.init()
        self.bg_image = pygame.image.load('images/bg.png')
        self.bg_rect = self.bg_image.get_rect()
        self.screen = pygame.display.set_mode((self.bg_rect.width, self.bg_rect.height))
        # TODO
        pygame.display.set_caption('练习二')
        self.running = True

    def gameupdate(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.running = False
            self.screen.blit(self.bg_image, self.bg_rect)
            pygame.display.update()
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    b_game = Bird()
    b_game.gameupdate()
