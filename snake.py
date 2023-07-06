import pygame
import sys
import random
from pygame.math import Vector2


class FOOD:
    def __init__(self):
        self.x = random.randint(0, cell_number-1)
        self.y = random.randint(0, cell_number-1)
        self.pos = Vector2(self.x, self.y)

    def draw_food(self):
        food_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (200, 0, 0), food_rect)


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rec = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (0, 200, 0), block_rec)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]


pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

food = FOOD()
snake = SNAKE()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    # draw elements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1, 0)


    screen.fill('pink')
    food.draw_food()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)
