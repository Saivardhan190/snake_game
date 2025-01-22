import random
import pygame

pygame.init()

width, height = 600, 600
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sai Snake Game")

snake_x, snake_y = width // 2, height // 2
change_x, change_y = 0, 0
food_x, food_y = random.randrange(0, width, 10), random.randrange(0, height, 10)

clock = pygame.time.Clock()
snake_body = [(snake_x, snake_y)]
score = 0
font = pygame.font.SysFont("comicsansms", 20)

# Function to display the snake, food, and score
def display_snake_and_food():
    global snake_x, snake_y, food_x, food_y, score

    snake_x = (snake_x + change_x) % width
    snake_y = (snake_y + change_y) % height

    if (snake_x, snake_y) in snake_body[1:]:
        game_over()
    snake_body.append((snake_x, snake_y))

    if (food_x == snake_x and food_y == snake_y):
        score += 1
        food_x, food_y = random.randrange(0, width, 10), random.randrange(0, height, 10)
    else:
        del snake_body[0]

    game_screen.fill((20, 20, 20))
    pygame.draw.circle(game_screen, (200, 0, 0), (food_x, food_y), 6)
    for (x, y) in snake_body:
        pygame.draw.circle(game_screen, (0, 200, 0), (x, y), 6)

    # Display the score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    game_screen.blit(score_text, (10, 10))

    pygame.display.update()

# Function to display the game over screen
def game_over():
    game_screen.fill((0, 0, 0))
    game_over_text = font.render("GAME OVER", True, (255, 0, 0))
    score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
    game_screen.blit(game_over_text, (width // 2 - 70, height // 2 - 30))
    game_screen.blit(score_text, (width // 2 - 70, height // 2 + 10))
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()
    quit()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and change_x == 0:
                change_x, change_y = -10, 0
            elif event.key == pygame.K_RIGHT and change_x == 0:
                change_x, change_y = 10, 0
            elif event.key == pygame.K_UP and change_y == 0:
                change_x, change_y = 0, -10
            elif event.key == pygame.K_DOWN and change_y == 0:
                change_x, change_y = 0, 10

    display_snake_and_food()
    clock.tick(15)
