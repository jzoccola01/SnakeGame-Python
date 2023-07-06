import pygame

cell_number = 40
cell_size = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()


def get_cell_number() -> int:
    return cell_number


def get_cell_size() -> int:
    return cell_size


def set_cell_size(size) -> int:
    return size


def set_cell_number(num) -> int:
    return num


def create_screen():
    return screen


def get_clock():
    return clock
