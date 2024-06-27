import pygame

# Для автоматической инициализации всех модулей Pygame пишем
pygame.init()

# Создаём окно с определёнными размерами, с заголовком:
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Тестовый проект")

# создаем изображение и рамку для него
image = pygame.image.load("pic-01.png")
image_rect = image.get_rect()

# скорость движения
speed = 5

# Для создания игрового цикла создаём переменную и задаём цикл:
run = True
while run:
    for event in pygame.event.get():
        # 🧠Этот блок сделает так, чтобы при нажатии на крестик в окне игры программа завершалась, а не зависала.
        if event.type == pygame.QUIT:
            run = False

    # работа с клавишами
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        image_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        image_rect.x += speed
    if keys[pygame.K_UP]:
        image_rect.y -= speed
    if keys[pygame.K_DOWN]:
        image_rect.y += speed

    # Заполняем цвет фоном — внутри блока while run пишем:
    screen.fill((0, 0, 0))

    # Отображаем нашу картинку поверх основной заливки
    screen.blit(image, image_rect)

    # Чтобы обновлять содержимое экрана, внутри блока while run пишем:
    pygame.display.flip

# В конце программы используем команду выхода:
pygame.quit()
