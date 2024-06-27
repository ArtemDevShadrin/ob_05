import pygame
import random

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Размер ячейки и сетки
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Направления
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Определение стартовой позиции змеи и скорости
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = RIGHT
snake_speed = 10

# Определение стартовой позиции еды
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Переменные для счетчика еды и флага окончания игры
food_count = 0
game_over = False

# Функция отрисовки змеи и еды
def draw():
    WIN.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(WIN, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(WIN, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()

# Функция обработки событий
def handle_events():
    global snake_direction, game_over
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != DOWN:
                snake_direction = UP
            elif event.key == pygame.K_DOWN and snake_direction != UP:
                snake_direction = DOWN
            elif event.key == pygame.K_LEFT and snake_direction != RIGHT:
                snake_direction = LEFT
            elif event.key == pygame.K_RIGHT and snake_direction != LEFT:
                snake_direction = RIGHT
            elif event.key == pygame.K_SPACE and game_over:
                reset_game()

# Функция обновления змейки
def update_snake():
    global food, food_count, game_over
    head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    if head == food:
        snake.append(snake[-1])
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        food_count += 1
    else:
        snake.pop()
    if head in snake:
        game_over = True
    if head[0] < 0:
        head = (GRID_WIDTH - 1, head[1])
    elif head[0] >= GRID_WIDTH:
        head = (0, head[1])
    if head[1] < 0:
        head = (head[0], GRID_HEIGHT - 1)
    elif head[1] >= GRID_HEIGHT:
        head = (head[0], 0)
    snake.insert(0, head)

# Функция сброса игры
def reset_game():
    global snake, snake_direction, food, food_count, game_over
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    snake_direction = RIGHT
    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    food_count = 0
    game_over = False

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(snake_speed)
    handle_events()
    if not game_over:
        update_snake()
    draw()

    if game_over:
        font = pygame.font.Font(None, 24)
        text = font.render("Игра окончена! Счет: {}. Нажмите Пробел для новой игры.".format(food_count), True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        WIN.blit(text, text_rect)
        pygame.display.update()
