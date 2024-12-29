import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Màu sắc
red = (255, 0, 0)       # Màu rắn (snake)
green = (0, 255, 0)     # Màu nền
yellow = (255, 255, 102)  # Màu thức ăn
black = (0, 0, 0)       # Màu chữ

# Kích thước và tốc độ
snake_block = 10
snake_speed = 15

# Đồng hồ để điều chỉnh tốc độ khung hình
clock = pygame.time.Clock()

# Hàm hiển thị thông điệp
def show_message(msg, color, x, y, font_size=50):
    font = pygame.font.SysFont("comicsansms", font_size)
    message = font.render(msg, True, color)
    screen.blit(message, (x, y))

# Hàm hiển thị menu "You Died"
def show_game_over_menu(score):
    screen.fill(black)  # Làm mới màn hình
    show_message("You Died!", red, width // 4, height // 4, 50)
    show_message(f"Your Score: {score}", yellow, width // 4, height // 2, 35)
    show_message("Press C to Play Again or Q to Quit", green, width // 8, height // 1.5, 30)
    pygame.display.update()

# Hàm vẽ rắn
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, red, [x[0], x[1], snake_block, snake_block])  # Màu đỏ cho rắn

# Vòng lặp chính của trò chơi
def gameLoop():
    game_over = False
    game_close = False

    # Vị trí ban đầu của rắn
    x1, y1 = width // 2, height // 2
    x1_change, y1_change = 0, 0
    snake_list = []
    length_of_snake = 1

    # Tọa độ thức ăn
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            # Hiển thị menu "You Died"
            show_game_over_menu(length_of_snake - 1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # Nhấn Q để thoát
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # Nhấn C để chơi lại
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # Kiểm tra va chạm tường
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(green)  # Tô nền màu xanh lá

        # Vẽ thức ăn
        pygame.draw.rect(screen, yellow, [foodx, foody, snake_block, snake_block])

        # Xử lý rắn
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Kiểm tra rắn đụng vào chính nó
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        # Vẽ rắn
        draw_snake(snake_block, snake_list)
        pygame.display.update()

        # Kiểm tra rắn ăn thức ăn
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()

# Bắt đầu trò chơi
gameLoop()
