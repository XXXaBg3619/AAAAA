import sys, pygame, random, time
from pygame.locals import *

#初始化Pygame庫
pygame.init()

#初始化一個遊戲介面視窗
display = pygame.display.set_mode((640, 480))

#設定遊戲視窗的標題
pygame.display.set_caption("THE SNAKE")

#定義一個變數來控制遊戲速度
fps = pygame.time.Clock()

#初始化遊戲介面內使用的字型
basicfont = pygame.font.SysFont("SIMYOU.TTF", 80)

#定義顏色變數
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
grey = pygame.Color(150, 150, 150)



#繪製貪吃蛇
def draw_snake(snake_body):
    for i in snake_body:
        pygame.draw.rect(display, white, rect(i[0], i[1], 20, 20))

#繪製食物的位置
def draw_food(food_pos):
    pygame.draw.rect(display, red, Rect(food_pos[0], food_pos[1], 20, 20))

#印出當前得分
def draw_score(score):

    #設定分數顯示顏色
    score_surf = basicfont.render("%s" %(score), True, grey)

    #設定分數位置
    score_rect = score_surf.get_rect()
    score_rect.midtop = (320, 240)

    #繫結以上設定到控制程式碼
    display.blit(score_surf, score_rect)


#遊戲結束並退出
def gameover():

    #設定Gameover的顯示顏色
    gameover_surf = basicfont.render("GAMEOVER!", True, grey)

    #設定Gameover位置
    gameover_rect = gameover_surf.get_rect()
    gameover_rect.midtop(320, 10)

    #細節以上設定到控制程式碼
    display.blit(gameover_surf, gameover_rect)


    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


"""運行程式"""

#檢測按鍵等Pygame事件
for event in pygame.event.get():
    if event.type == quit:
        
        #接收到退出事件後退出程式
        pygame.quit()
        sys.exit()

    #判斷鍵盤事件時，用方向鍵或wsad來表示上下左右
    elif event.type == KEYDOWN:
        if (event.key == K_UP or event.key == K_s) and direction != DOWN:
            direction = UP
        if (event.key == K_DOWN or event.key == K_s) and direction != UP:
            direction = Down
        if (event.key == K_LEFT or event.key == K_a) and direction != UP:
            direction = LEFT
        if (event.key == K_RIGHT or event.key == K_d) and direction != UP:
            direction = RIGHT

        #根據鍵盤的輸入，改變蛇的頭部，進行轉彎操作
        if direction == UP:
            snake_head[0] -= 20
        if direction == DOWN:
            snake_head[0] += 20
        if direction == LEFT:
            snake_head[1] -= 20
        if direction == RIGHT:
            snake_head[1] += 20

        #將蛇的頭部當前的位置加入到蛇身的列表中
        snake_body.insert(0, list(snake_head))

        #判斷是否吃到食物
        if snake_head[0] == food_pos[0] and snake_head[1] == food_pos[1]:
            food_flag = 0
        else:
            snake_body.pop()

        #生成新的食物
        if food_flag == 0:
            
            #隨機生成x, y
            x = random.randrange(1, 32)
            y = random.randrange(1, 24)
            food_pos = [int( x * 20), int(y * 20)]
            food_flag = 1


        display.fill(black)
        draw_snake(snake_body)
        draw_food(food_pos)
        draw_score(len(snake_body) - 3)

        #重新整理
        pygame.display.flip()

        #控制遊戲速度
        fps.tick(7)


        """遊戲結束的判斷"""
        #碰到邊界
        if snake_head[0] < 0 or snake_head[0] > 620:
            gameover()
        if snake_head[1] < 0 or snake_head[1] > 460:
            gameover()

        #碰到自己
        for i in snake_body[1:]:
            if snake_head[0] == i[0] and snake_head[1] == i[1]:
                gameover()
        

