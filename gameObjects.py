import random
import pygame
import sys
import Setting
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for block in self.body:
            x_pos = block.x * Setting.get_cell_size()
            y_pos = block.y * Setting.cell_size
            block_rec = pygame.Rect(x_pos, y_pos, Setting.get_cell_size(), Setting.get_cell_size())
            pygame.draw.rect(Setting.create_screen(), (0, 200, 0), block_rec)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def check_snake(self):
        if self.body[0].x < 0 or self.body[0].x >= Setting.get_cell_number() \
                or self.body[0].y < 0 or self.body[0].y >= Setting.get_cell_number():
            Setting.game_over()


class FOOD:
    def __init__(self):
        self.x = random.randint(0, Setting.get_cell_size() - 1)
        self.y = random.randint(0, Setting.get_cell_size() - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_food(self):
        food_rect = pygame.Rect(
            self.pos.x * Setting.get_cell_size(),
            self.pos.y * Setting.get_cell_size(),
            Setting.get_cell_size(),
            Setting.get_cell_size())

        pygame.draw.rect(Setting.create_screen(), (200, 0, 0), food_rect)
