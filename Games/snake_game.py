import pygame
import random

pygame.init()

# Initialize the screen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Define snake and food properties
snake_block = 10
snake_speed = 30 # Increase this value for a slower snake

snake_x = screen_width / 2
snake_y = screen_height / 2

snake_list = []
snake_length = 1

food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

game_over = False

snake_x_change = 0
snake_y_change = 0

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_block
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_block
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_block
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_block
                snake_x_change = 0

    snake_x += snake_x_change
    snake_y += snake_y_change

    # Snake movement and length management
    snake_head = [snake_x, snake_y]
    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        del snake_list[0]

    # Food generation and snake growth
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
        food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
        snake_length += 1

    # Game over conditions
    if (
        snake_x >= screen_width
        or snake_x < 0
        or snake_y >= screen_height
        or snake_y < 0
    ):
        game_over = True

    for x in snake_list[:-1]:
        if x == snake_head:
            game_over = True

    # Draw the screen
    screen.fill(black)
    for pos in snake_list:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], snake_block, snake_block))
    pygame.draw.rect(screen, red, pygame.Rect(food_x, food_y, snake_block, snake_block))

    pygame.display.update()

    pygame.time.delay(snake_speed)

pygame.quit()
