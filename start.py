import pygame
import random
from gtts import gTTS
import os

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Arabic Letters")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Clock
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Snake setup
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = "RIGHT"
change_to = direction

# Food
arabic_letters = ["أ", "ب", "ت", "ث", "ج", "ح", "خ"]
food_letter = random.choice(arabic_letters)
food_pos = [random.randrange(1, (WIDTH // 10)) * 10,
            random.randrange(1, (HEIGHT // 10)) * 10]
food_spawn = True

# Game over
def game_over():
    pygame.quit()
    quit()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            elif event.key == pygame.K_DOWN:
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT:
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    # Change direction
    if change_to == "UP" and not direction == "DOWN":
        direction = "UP"
    if change_to == "DOWN" and not direction == "UP":
        direction = "DOWN"
    if change_to == "LEFT" and not direction == "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and not direction == "LEFT":
        direction = "RIGHT"

    # Move the snake
    if direction == "UP":
        snake_pos[1] -= 10
    if direction == "DOWN":
        snake_pos[1] += 10
    if direction == "LEFT":
        snake_pos[0] -= 10
    if direction == "RIGHT":
        snake_pos[0] += 10

    # Snake body growing
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawn = False
        # Play sound for eaten letter
        tts = gTTS(food_letter, lang='ar')
        tts.save("letter.mp3")
        os.system("mpg123 letter.mp3")
        food_letter = random.choice(arabic_letters)
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH // 10)) * 10,
                    random.randrange(1, (HEIGHT // 10)) * 10]
        food_spawn = True

    # Game over conditions
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH - 10 or \
            snake_pos[1] < 0 or snake_pos[1] > HEIGHT - 10:
        game_over()

    # Drawing
    screen.fill(WHITE)
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Draw food letter
    text_surface = font.render(food_letter, True, BLACK)
    screen.blit(text_surface, (food_pos[0], food_pos[1]))

    pygame.display.flip()
    clock.tick(15)
