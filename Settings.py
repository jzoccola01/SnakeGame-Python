import sys

import pygame

# Settings:
cell_number = 40
cell_size = 20
width, height = cell_number * cell_size, cell_number * cell_size
screen = pygame.display.set_mode((width, height))


def get_cell_number() -> int:
    return cell_number


def get_cell_size() -> int:
    return cell_size


def set_cell_size(size) -> int:
    return size


def set_cell_number(num) -> int:
    return num


def set_screen_size(width, height):
    return pygame.display.set_mode((width, height))


def get_screen():
    return screen


def get_clock():
    return pygame.time.Clock()


# TODO: Make this function display a game over screen instead of just quitting the game
def game_over():
    # Pause the game and display game over screen (eventually)
    pygame.quit()
    sys.exit()
