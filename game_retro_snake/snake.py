#根据b站up主 @Tonymot 的63行代码实现俄罗斯方块思路修改而来的50+行实现贪吃蛇

import pygame,sys, random

time, game_over, direction, direction_swap, snake_body, wall, bean = 0, False, 1, 1, [[10,12],[10,13]], [25,20], [10, 10]

def move(n):
    global direction, game_over, direction_swap, bean
    if 2 >= n >= -2 and direction != n and direction != -n:
        direction_swap = n
    if 10 == n:
        direction = direction_swap
        x, y = (direction % 2) * direction, int(direction / 2)
        if 0 <= snake_body[-1][0]+x < wall[0] and wall[1] >= snake_body[-1][1] + y > 0:
            if [snake_body[-1][0]+x, snake_body[-1][1]+y] in snake_body:
                game_over = True
            snake_body.append([snake_body[-1][0]+x, snake_body[-1][1]+y])
            if snake_body[-1][0] != bean[0] or snake_body[-1][1] != bean[1]:
                snake_body.pop(0)
            else:
                while bean in snake_body:
                    bean = [int(random.random()*1000 % wall[0]), int(random.random()*1000 % wall[1] + 1)]
        else:
            game_over = True
        for row in range(25):
            for col in range(1, 21):
                if [row, col] in snake_body:
                    pygame.draw.rect(screen, (0, 0, 255), (row*20, 400-col*20, 20, 20))
        pygame.draw.rect(screen, (255, 0, 0), (bean[0]*20, 400-bean[1]*20, 19, 19))

pygame.init()
screen = pygame.display.set_mode((500,400))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            move(-1)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            move(1)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            move(2)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            move(-2)
    if time >= 10:
        screen.fill((255, 255, 255))
        move(10)
        time = 0
    else:time += 1
    if game_over:sys.exit()
    pygame.time.Clock().tick(180)
    pygame.display.flip()