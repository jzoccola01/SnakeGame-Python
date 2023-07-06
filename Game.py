import pygame
import sys

from pygame import font
from pygame.math import Vector2
import gameObjects
import Settings

# CONSTANTS:
SCREEN_UPDATE = pygame.USEREVENT

pygame.time.set_timer(SCREEN_UPDATE, 150)
pygame.display.set_caption("Snake Game by Jonny and Zach")


# This function displays the current score of the game: eventually I wanna have it be on the screen
def print_score(score):
    print(score)

# This function runs the gameplay
def run_game():
    # initial settings:
    pygame.init()
    snake = gameObjects.SNAKE()
    food = gameObjects.FOOD()
    score = 0

    while True:
        # draw elements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == SCREEN_UPDATE:
                snake.move_snake()

                # If the snake gets the food
                if snake.body[0] == food.pos:
                    food = gameObjects.FOOD()
                    score += 1
                    print_score(score)
                    snake.add_block()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != Vector2(0, 1):
                    snake.direction = Vector2(0, -1)
                elif event.key == pygame.K_DOWN and snake.direction != Vector2(0, -1):
                    snake.direction = Vector2(0, 1)
                elif event.key == pygame.K_LEFT and snake.direction != Vector2(1, 0):
                    snake.direction = Vector2(-1, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != Vector2(-1, 0):
                    snake.direction = Vector2(1, 0)
                else:
                    continue
            if not event:
                snake = gameObjects.SNAKE()

        Settings.get_screen().fill('black')
        food.draw_food()
        snake.draw_snake()
        pygame.display.update()
        Settings.get_clock().tick(60)


if __name__ == "__main__":
    run_game()
