import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('pygame event')
# bg_color = pygame.Color('#222222')
bg_color = pygame.Color('#202020')

pygame.event.set_blocked(pygame.MOUSEMOTION)
ienent = pygame.event.Event(pygame.USEREVENT, {
    "a1": 666,
    "b2": 777,
    "c3": 888
})
while True:
    # pygame.event.clear(pygame.MOUSEMOTION)
    for event in pygame.event.get([
            pygame.QUIT,
            pygame.KEYDOWN,
            pygame.KEYUP,
            pygame.MOUSEBUTTONDOWN,
            pygame.MOUSEBUTTONUP,
            pygame.MOUSEMOTION,
            pygame.USEREVENT,
    ]):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print('KEYDOWN:', event.unicode, event.key, event.mod)
            print(pygame.event.get_blocked(pygame.MOUSEMOTION))
            pygame.event.post(ienent)
            if event.key == pygame.K_r:
                bg_color.g = bg_color.g + 10
            print(bg_color)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('MOUSEBUTTONDOWN:', event.pos, event.button)
        elif event.type == pygame.MOUSEMOTION:
            print('MOUSEMOTION:', event.pos, event.rel, event.buttons)
        elif event.type == pygame.USEREVENT:
            print('USEREVENT:', event.a1, event.b2, event.c3)

    screen.fill(bg_color)
    pygame.display.update()

# while True:
#     event = pygame.event.poll()
#     if event.type == pygame.QUIT:
#         sys.exit()
#     elif event.type == pygame.MOUSEMOTION:
#         print(event.pos, event.buttons)
#     screen.fill((100, 168, 100))
#     pygame.display.update()
