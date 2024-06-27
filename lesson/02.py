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

image2 = pygame.image.load("")
image_rect2 = image2.get_rect()

# Для создания игрового цикла создаём переменную и задаём цикл:
run = True
while run:
    for event in pygame.event.get():
        # 🧠Этот блок сделает так, чтобы при нажатии на крестик в окне игры программа завершалась, а не зависала.
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect.x = mouseX
            image_rect.y = mouseY

    # Заполняем цвет фоном — внутри блока while run пишем:
    screen.fill((0, 0, 0))

    # Отображаем нашу картинку поверх основной заливки
    screen.blit(image, image_rect)
    screen.blit(image2, image_rect2)

    # Чтобы обновлять содержимое экрана, внутри блока while run пишем:
    pygame.display.flip

# В конце программы используем команду выхода:
pygame.quit()
