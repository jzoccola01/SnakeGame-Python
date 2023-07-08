import pygame

# Settings:
cell_number = 20
cell_size = 30
screen_width, screen_height = cell_number * cell_size, cell_number * cell_size
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


def set_cell_size(size) -> int:
    return size


def set_cell_number(num) -> int:
    return num


def set_screen_size(width, height):
    return pygame.display.set_mode((width, height))

