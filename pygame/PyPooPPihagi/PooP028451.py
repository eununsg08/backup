import pygame
from random import *
##############################################
# 기본 초기화 (반드시 해야 하는 것들)

pygame.init()  # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로
screen_height = 640  # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Ju Game")  # 게임 이름

# FPS
clock = pygame.time.Clock()
##############################################


# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경 만들기
background = pygame.image.load("D:\code\pygame\PyPooPPihagi\배경사진.png")

# 캐릭터
character = pygame.image.load("D:\code\pygame\PyPooPPihagi\캐릭터.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

character_x_pos = (screen_width / 2) - (character_width/2)
character_y_pos = (screen_height) - (character_height)

# 똥
enemy_1 = pygame.image.load("D:\code\pygame\PyPooPPihagi\똥.png")

enemy_1_size = enemy_1.get_rect().size
enemy_1_width = enemy_1_size[0]
enemy_1_height = enemy_1_size[1]

enemy_1_x_pos = randint(0, (screen_width) - (character_width))
enemy_1_y_pos = 0
#enemy_1_speed = randint(10, 20)
enemy_1_speed = int(10)

enemy_2 = pygame.image.load("D:\code\pygame\PyPooPPihagi\똥.png")

enemy_2_size = enemy_2.get_rect().size
enemy_2_width = enemy_2_size[0]
enemy_2_height = enemy_2_size[1]

enemy_2_x_pos = randint(0, (screen_width) - (character_width))
enemy_2_y_pos = 0
#enemy_2_speed = randint(10, 20)
enemy_2_speed = int(10)

enemy_3 = pygame.image.load("D:\code\pygame\PyPooPPihagi\똥.png")

enemy_3_size = enemy_3.get_rect().size
enemy_3_width = enemy_3_size[0]
enemy_3_height = enemy_3_size[1]

enemy_3_x_pos = randint(0, (screen_width) - (character_width))
enemy_3_y_pos = 0
#enemy_3_speed = randint(10, 20)
enemy_3_speed = int(10)

enemy_4 = pygame.image.load("D:\code\pygame\PyPooPPihagi\똥.png")

enemy_4_size = enemy_1.get_rect().size
enemy_4_width = enemy_1_size[0]
enemy_4_height = enemy_1_size[1]

enemy_4_x_pos = randint(0, (screen_width) - (character_width))
enemy_4_y_pos = 0
#enemy_1_speed = randint(10, 20)
enemy_4_speed = int(10)

enemy_5 = pygame.image.load("D:\code\pygame\PyPooPPihagi\똥.png")

enemy_5_size = enemy_1.get_rect().size
enemy_5_width = enemy_1_size[0]
enemy_5_height = enemy_1_size[1]

enemy_5_x_pos = randint(0, (screen_width) - (character_width))
enemy_5_y_pos = 0
#enemy_1_speed = randint(10, 20)
enemy_5_speed = int(10)

# 폰트
game_font = pygame.font.Font(None, 40)

# 시작 시간
start_ticks = pygame.time.get_ticks()

# 이동
to_x = 0
to_y = 0

character_speed = 1.1

running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등 )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
            if event.key == pygame.K_UP:
                to_y = 0
            if event.key == pygame.K_DOWN:
                to_y = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 타이머 집어넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    timer = game_font.render(str(int(elapsed_time)), True, (255, 255, 255))

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_1_y_pos += enemy_1_speed

    if enemy_1_y_pos > screen_height:
        enemy_1_y_pos = 0
        enemy_1_x_pos = randint(0, (screen_width) - (character_width))

    enemy_2_y_pos += enemy_2_speed

    if enemy_2_y_pos > screen_height:
        enemy_2_y_pos = 0
        enemy_2_x_pos = randint(0, (screen_width) - (character_width))

    enemy_3_y_pos += enemy_3_speed

    if enemy_3_y_pos > screen_height:
        enemy_3_y_pos = 0
        enemy_3_x_pos = randint(0, (screen_width) - (character_width))

    enemy_4_y_pos += enemy_4_speed

    if enemy_4_y_pos > screen_height:
        enemy_4_y_pos = 0
        enemy_4_x_pos = randint(0, (screen_width) - (character_width))

        enemy_5_y_pos += enemy_5_speed

    if enemy_5_y_pos > screen_height:
        enemy_5_y_pos = 0
        enemy_5_x_pos = randint(0, (screen_width) - (character_width))

    # 4. 충돌 처리

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_1_rect = enemy_1.get_rect()
    enemy_1_rect.left = enemy_1_x_pos
    enemy_1_rect.top = enemy_1_y_pos

    enemy_2_rect = enemy_2.get_rect()
    enemy_2_rect.left = enemy_2_x_pos
    enemy_2_rect.top = enemy_2_y_pos

    enemy_3_rect = enemy_3.get_rect()
    enemy_3_rect.left = enemy_3_x_pos
    enemy_3_rect.top = enemy_3_y_pos

    if character_rect.colliderect(enemy_1_rect):
        print("충돌 발생")
        running = False
    elif character_rect.colliderect(enemy_2_rect):
        print("충돌 발생")
        running = False
    # elif character_rect.colliderect(enemy_3_rect):
    #     print("충돌 발생")
    #     running = False

    # 5. 화면에 그리기

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy_1, (enemy_1_x_pos, enemy_1_y_pos))
    screen.blit(enemy_2, (enemy_2_x_pos, enemy_2_y_pos))
    screen.blit(enemy_3, (enemy_3_x_pos, enemy_3_y_pos))
    screen.blit(timer, (10, 10))

    # if elapsed_time > 20:
    #     screen.blit(enemy_3, (enemy_3_x_pos, enemy_3_y_pos))

    pygame.display.update()  # 게임화면을 다시 그리기!


pygame.time.delay(2000)
pygame.quit()