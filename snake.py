import pygame
import sys

pygame.init()
# screen display
screen = pygame.display.set_mode((400, 500))

while True:
    # draw elements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
