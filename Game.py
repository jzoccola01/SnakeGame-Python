import sys

import pygame
from pygame.math import Vector2

import Settings
import gameObjects

# CONSTANTS:
SCREEN_UPDATE = pygame.USEREVENT

pygame.time.set_timer(SCREEN_UPDATE, 150)
pygame.display.set_caption("Snake Game by Jonny and Zach")


def display_game_over():
    pygame.init()
    font = pygame.font.Font(None, 75)  # Define the font and size

    text = font.render("Game Over", True, (255, 0, 0))  # Render the text
    text_rect = text.get_rect(center=(400, 200))  # Position the text at the center of the screen

    text_play_again = font.render("Press Enter to Play Again", True, (255, 255, 255))  # Render the text
    text_play_again_rect = text_play_again.get_rect(center=(400, 300))  # Position the text at the center of the screen

    text_quit = font.render("Press Escape to Quit", True, (255, 255, 255))  # Render the text
    text_quit_rect = text_quit.get_rect(center=(400, 400))  # Position the text at the center of the screen

    Settings.screen.fill((0, 0, 0))  # Fill the screen with black color
    Settings.screen.blit(text, text_rect)  # Blit the text onto the screen
    Settings.screen.blit(text_play_again, text_play_again_rect)  # Blit the text onto the screen
    Settings.screen.blit(text_quit, text_quit_rect)  # Blit the text onto the screen

    pygame.display.flip()  # Update the screen

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Play Again on Enter key press
                    run_game()
                    return
                elif event.key == pygame.K_ESCAPE:  # Quit on Escape key press
                    quit_game()
                    return


def quit_game():
    pygame.quit()
    sys.exit()


# This function displays the current score of the game:
def print_score(score):
    pygame.display.set_caption("Snake Game by Jonny and Zach | Score: " + str(score))


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
                snake.check_collision()

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

        Settings.screen.fill('black')
        food.draw_food()
        snake.draw_snake()
        pygame.display.update()
        Settings.clock.tick(60)


if __name__ == "__main__":
    run_game()
