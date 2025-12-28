import pygame
import random

pygame.init()

# Screen size
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game by Chiku 😎")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()
SNAKE_BLOCK = 20
SPEED = 5  # starting speed

# Fonts
font = pygame.font.SysFont("comicsansms", 30)

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(win, GREEN, [x, y, SNAKE_BLOCK, SNAKE_BLOCK])

def draw_food(x, y):
    pygame.draw.rect(win, RED, [x, y, SNAKE_BLOCK, SNAKE_BLOCK])

def message(msg, color):
    text = font.render(msg, True, color)
    win.blit(text, [WIDTH/6, HEIGHT/3])

def gameLoop():
    run = True
    game_over = False

    # Snake starting position
    x = WIDTH//2
    y = HEIGHT//2
    x_change = SNAKE_BLOCK  # automatic start moving right
    y_change = 0

    snake_list = []
    length = 1

    # Food position
    food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 20.0) * 20
    food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 20.0) * 20

    score = 0

    while run:

        while game_over:
            win.fill(BLUE)
            message(f"You Lost! Score: {score}. Press C to play again or Q to quit.", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        run = False
                        game_over = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                # Arrow keys
                if event.key == pygame.K_LEFT and x_change != SNAKE_BLOCK:
                    x_change = -SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change != -SNAKE_BLOCK:
                    x_change = SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_UP and y_change != SNAKE_BLOCK:
                    y_change = -SNAKE_BLOCK
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change != -SNAKE_BLOCK:
                    y_change = SNAKE_BLOCK
                    x_change = 0

        # Move snake
        x += x_change
        y += y_change

        # Wrap-around walls
        x %= WIDTH
        y %= HEIGHT

        win.fill(BLUE)
        draw_food(food_x, food_y)

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length:
            del snake_list[0]

        # Self-collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        draw_snake(snake_list)

        # Food eaten
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 20.0) * 20
            food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 20.0) * 20
            length += 1
            score += 1

        # Draw score
        text = font.render(f"Score: {score}", True, WHITE)
        win.blit(text, [10,10])

        pygame.display.update()
        clock.tick(SPEED)

    pygame.quit()
    quit()

gameLoop()
