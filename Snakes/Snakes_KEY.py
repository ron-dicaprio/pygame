#-*- encoding:utf-8 -*-
import pygame, sys,os,random
from collections import deque

# screen窗口居中
os.environ['SDL_VIDEO_CENTERED'] = '1'  

# color_list R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0) 
BGCOLOR  = ( 40,  40,  60)
DARK     = (200, 200, 200)

FPS = 20

SCREEN_WIDTH = 600      # 屏幕宽度
SCREEN_HEIGHT = 480     # 屏幕高度
SIZE = 20               # 小方格大小
LINE_WIDTH = 1          # 网格线宽度

# 游戏区域的坐标范围
SCOPE_X = (0, SCREEN_WIDTH // SIZE - 1)
SCOPE_Y = (2, SCREEN_HEIGHT // SIZE - 1)
#print(SCOPE_X,SCOPE_Y)

FPSCLOCK = pygame.time.Clock()

# 初始化蛇,长度3个单位
def init_snake():
    snake = deque()
    snake.append((2, SCOPE_Y[0]))
    snake.append((1, SCOPE_Y[0]))
    snake.append((0, SCOPE_Y[0]))
    return snake

# 随机掉落食物
def create_food(snake):
    food_x = random.randint(SCOPE_X[0], SCOPE_X[1])
    food_y = random.randint(SCOPE_Y[0], SCOPE_Y[1])
    # while解决掉食物可能多次掉落在蛇身上的问题
    while (food_x, food_y) in snake:
        food_x = random.randint(SCOPE_X[0], SCOPE_X[1])
        food_y = random.randint(SCOPE_Y[0], SCOPE_Y[1])
    return food_x, food_y

def print_text(screen, font, x, y, text, fcolor=(255, 255, 255)):
    imgText = font.render(text, True, fcolor)
    screen.blit(imgText, (x, y))

def main():
    # 时钟同步
    global FPSCLOCK, screen
    pygame.init()
    pygame.mouse.set_visible(0)
    # 背景音乐并设置音量50%
    pygame.mixer.music.load('files/ZB_BGM1.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.80)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snakes')
    pos = (1, 0)
    font1 = pygame.font.SysFont('SimHei', 24)  # 得分的字体
    font2 = pygame.font.Font(None, 72)         # GAME OVER 的字体
    fwidth, fheight = font2.size('GAME OVER')

    # 初始化snake函数
    snake = init_snake()

    # 食物
    food = create_food(snake)

    # 初始化分数
    score=0

    # 填充背景色
    screen.fill(BGCOLOR)
    
    game_over = False


    while True: 
        for event in pygame.event.get(): 
            # if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # 防止出现后退现象
                    if pos[0] != -1:
                        pos=(1, 0)
                        next_s = (snake[0][0] + pos[0], snake[0][1] + pos[1])
                        # 咬到自己，游戏结束
                        if next_s in snake:
                            game_over=True
                        if next_s == food:
                            score+=1
                            snake.appendleft(next_s)
                            food = create_food(snake)
                            pygame.display.update() 
                        else:
                            # 判断触碰便捷的情况
                            if SCOPE_X[0] <= next_s[0] <= SCOPE_X[1] and SCOPE_Y[0] <= next_s[1] <= SCOPE_Y[1] and game_over == False:
                                snake.appendleft(next_s)
                                # pop()函数snake清除队列中最后一位
                                snake.pop()
                                pygame.display.update()
                            else:
                                game_over=True
                    else:
                        pass
                if event.key == pygame.K_LEFT:
                    if pos[0] != 1:
                        pos=(-1, 0)
                        next_s = (snake[0][0] + pos[0], snake[0][1] + pos[1])
                        # 咬到自己，游戏结束
                        if next_s in snake:
                            game_over=True
                        if next_s == food:
                            score+=1
                            snake.appendleft(next_s)
                            food = create_food(snake)
                            pygame.display.update() 
                        else:
                            if SCOPE_X[0] <= next_s[0] <= SCOPE_X[1] and SCOPE_Y[0] <= next_s[1] <= SCOPE_Y[1] and game_over == False:
                                snake.appendleft(next_s)
                                snake.pop()
                                pygame.display.update()
                            else:
                                game_over=True
                    else:
                        pass

                if event.key == pygame.K_UP:
                    if pos[1] != 1:
                        pos=(0, -1)
                        next_s = (snake[0][0] + pos[0], snake[0][1] + pos[1])
                        # 咬到自己，游戏结束
                        if next_s in snake:
                            game_over=True
                        if next_s == food:
                            score+=1
                            snake.appendleft(next_s)
                            food = create_food(snake)
                            pygame.display.update() 
                        else:
                            if SCOPE_X[0] <= next_s[0] <= SCOPE_X[1] and SCOPE_Y[0] <= next_s[1] <= SCOPE_Y[1] and game_over == False:
                                snake.appendleft(next_s)
                                snake.pop()
                                pygame.display.update()
                            else:
                                game_over=True 
                    else:
                        pass                    

                if event.key == pygame.K_DOWN:
                    if pos[1] != -1:
                        pos=(0, 1)
                        next_s = (snake[0][0] + pos[0], snake[0][1] + pos[1])
                        # 咬到自己，游戏结束
                        if next_s in snake:
                            game_over=True
                        if next_s == food:
                            score+=1
                            snake.appendleft(next_s)
                            food = create_food(snake)
                            pygame.display.update()
                        else:
                            # game_over控制游戏结束之后Snake无法再移动
                            if SCOPE_X[0] <= next_s[0] <= SCOPE_X[1] and SCOPE_Y[0] <= next_s[1] <= SCOPE_Y[1] and game_over == False:
                                snake.appendleft(next_s)
                                snake.pop()
                                pygame.display.update()
                            else:
                                game_over=True    
                    else:
                        pass
        # 填充背景色
        screen.fill(BGCOLOR)

        # 画网格线 竖线
        for x in range(SIZE, SCREEN_WIDTH, SIZE):
            pygame.draw.line(screen, BLACK, (x, SCOPE_Y[0] * SIZE), (x, SCREEN_HEIGHT), LINE_WIDTH)
        # 画网格线 横线
        for y in range(SCOPE_Y[0] * SIZE, SCREEN_HEIGHT, SIZE):
            pygame.draw.line(screen, BLACK, (0, y), (SCREEN_WIDTH, y), LINE_WIDTH)

        # 画蛇
        for ss in snake:
            pygame.draw.rect(screen, DARK, (ss[0] * SIZE + LINE_WIDTH, ss[1] * SIZE + LINE_WIDTH, SIZE - LINE_WIDTH * 2, SIZE - LINE_WIDTH * 2), 0)

        print_text(screen, font1, 30, 7, f'速度: 手动控制')
        print_text(screen, font1, 450, 7, f'得分:  %s' % (score))

        # 食物会把gameover覆盖
        if not game_over:
            pygame.draw.rect(screen, ORANGE, (food[0] * SIZE, food[1] * SIZE, SIZE, SIZE), 0)

        if game_over:
            print_text(screen, font2, (SCREEN_WIDTH - fwidth) // 2, (SCREEN_HEIGHT - fheight) // 2, 'GAME OVER', RED) 
            # 游戏结束，展示光标
            pygame.mouse.set_visible(1)
            
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()



