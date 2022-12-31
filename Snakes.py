#-*- encoding:utf-8 -*-
import pygame, sys,os,random
from collections import deque

# 窗口居中
os.environ['SDL_VIDEO_CENTERED'] = '1'  

# color      R    G    B
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

FOOD_STYLE_LIST=(10, (255, 100, 100))

# 游戏区域的坐标范围
SCOPE_X = (0, SCREEN_WIDTH // SIZE - 1)
SCOPE_Y = (2, SCREEN_HEIGHT // SIZE - 1)
#print(SCOPE_X,SCOPE_Y)

FPSCLOCK = pygame.time.Clock()

# 初始化蛇,长度3
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
    while (food_x, food_y) in snake:
        # 如果食物出现在蛇身上，则重来
        food_x = random.randint(SCOPE_X[0], SCOPE_X[1])
        food_y = random.randint(SCOPE_Y[0], SCOPE_Y[1])
    return food_x, food_y

def main():
    # 时钟同步
    global FPSCLOCK, screen
    pygame.init()
    # 背景音乐并设置音量50%
    pygame.mixer.music.load('files/ZB_BGM1.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.80)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('snake cakes')
    pos = (1, 0)
    #font1 = pygame.font.SysFont('SimHei', 24)  # 得分的字体
    #font2 = pygame.font.Font(None, 72)         # GAME OVER 的字体
    #fwidth, fheight = font2.size('GAME OVER')

    #slide_text_full=u'  在任何特定的环境里，人们至少还有一种自由，那就是选择自己的态度。一个人只要改变内在的心态，就可以改变外在的生活环境和生存状态。人的一生中，紧要处只有几步，如何使自己的生命更有意义，成为真正幸福的人，对于我们每个人来说，采取积极的生活态度就尤为重要。'
    slide_text_full=u'  江南皮革厂江南皮革厂倒闭了,黄鹤和小姨子跑路了.江南皮革厂江南皮革厂倒闭了,黄鹤和小姨子跑路了.'

    # 初始化snake函数
    snake = init_snake()

    # 食物
    food = create_food(snake)

    # 填充背景色
    screen.fill(BGCOLOR)


    while True: 
        for event in pygame.event.get(): 
            
            # close windows or press ESC
            #if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # 防止出现后退现象
                    if pos[0] != -1:
                        pos=(1, 0)
                        next_s = (snake[0][0] + pos[0], snake[0][1] + pos[1])
                        if next_s == food:
                            snake.appendleft(next_s)
                            food = create_food(snake)
                            #snake.pop()
                            pygame.display.update() 
                        else:
                            snake.appendleft(next_s)
                            snake.pop()
                            pygame.display.update()
                    else:
                        pass
                if event.key == pygame.K_LEFT:
                    if pos[0] != 1:
                        pos=(-1, 0)
                        next_s = (snake[0][0] + pos[0], snake[0][1] + pos[1])
                        if next_s == food:
                            snake.appendleft(next_s)
                            food = create_food(snake)
                            #snake.pop()
                            pygame.display.update() 
                        else:
                            snake.appendleft(next_s)
                            snake.pop()
                            pygame.display.update()
                    else:
                        pass

                if event.key == pygame.K_UP:
                    if pos[1] != 1:
                        pos=(0, -1)
                        next_s = (snake[0][0] + pos[0], snake[0][1] + pos[1])
                        if next_s == food:
                            snake.appendleft(next_s)
                            food = create_food(snake)
                            #snake.pop()
                            pygame.display.update() 
                        else:
                            snake.appendleft(next_s)
                            snake.pop()
                            pygame.display.update()
                    else:
                        pass                    

                if event.key == pygame.K_DOWN:
                    if pos[1] != -1:
                        pos=(0, 1)
                        next_s = (snake[0][0] + pos[0], snake[0][1] + pos[1])
                        if next_s == food:
                            snake.appendleft(next_s)
                            food = create_food(snake)
                            #snake.pop()
                            pygame.display.update()
                            
                        else:
                            snake.appendleft(next_s)
                            snake.pop()
                            pygame.display.update()
                            
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

          
        pygame.draw.rect(screen, FOOD_STYLE_LIST[0], (food[0] * SIZE, food[1] * SIZE, SIZE, SIZE), 0)
        
        game_Fonts=pygame.font.Font('C:\Windows\Fonts\msyh.ttc',30)
        slide_text_full=slide_text_full[1:]+slide_text_full[0]
        slide_text=slide_text_full[0:50]
        text_object=game_Fonts.render(slide_text,True,GREEN,BLUE)
        text_location=text_object.get_rect()
        #screen.blit(text_object,text_location)

        #pygame.time.delay(200)
        #print(snake)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
