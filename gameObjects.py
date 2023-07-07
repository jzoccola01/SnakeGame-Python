import random

import pygame
from pygame.math import Vector2

import Settings


class SNAKE:
    def __init__(self):
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for block in self.body:
            x_pos = block.x * Settings.get_cell_size()
            y_pos = block.y * Settings.cell_size
            block_rec = pygame.Rect(x_pos, y_pos, Settings.get_cell_size(), Settings.get_cell_size())
            pygame.draw.rect(Settings.get_screen(), (0, 200, 0), block_rec)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def add_block(self):
        tail = self.body[-1]
        new_tail = tail + self.direction
        self.body.append(new_tail)

    def check_collision(self):
        if self.body[0].x < 0 or self.body[0].x >= Settings.get_cell_number() or self.body[
                0].y >= Settings.get_cell_number() or self.body[0].y < 0:
            Settings.game_over()

        # Check if the snake hits itself:
        for block in self.body[1:]:
            if block == self.body[0]:
                Settings.game_over()


class FOOD:
    def __init__(self):
        self.x = random.randint(0, Settings.get_cell_size() - 1)
        self.y = random.randint(0, Settings.get_cell_size() - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_food(self):
        food_rect = pygame.Rect(
            self.pos.x * Settings.get_cell_size(),
            self.pos.y * Settings.get_cell_size(),
            Settings.get_cell_size(),
            Settings.get_cell_size())

        pygame.draw.rect(Settings.get_screen(), (200, 0, 0), food_rect)
