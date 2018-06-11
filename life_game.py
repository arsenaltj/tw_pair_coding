# -*- coding:utf8 -*-
import pygame
import sys
import time
import numpy as np
from pygame.locals import *
# 矩阵宽，高
WIDTH = 160
HEIGHT = 80
# 细胞大小
CELL_SIZE = 10

if len(sys.argv) < 5:
    print '''this game need 3 argv
                1:window width (100)
                2:windows height (50)
                3:cell size (10)
                so we run defualt
                '''
    WIDTH = 160
    HEIGHT = 80
    CELL_SIZE = 10
else:
    WIDTH = int(sys.argv[1])
    HEIGHT = int(sys.argv[2])
    CELL_SIZE = int(sys.argv[3])
# cell颜色
WHITE = (255, 255, 255)
BLUE = (0, 255, 255)
YELLOW = (255, 255, 0)
C1 = (255, 0, 255)
C2 = (255, 0, 0)
C3 = (0, 255, 0)
C4 = (0, 0, 255)
COLOR = WHITE
# 动画帧率
FRAME_RATE = 0.1

# 初始化world和鼠标点击事件
pygame.world = np.zeros((HEIGHT, WIDTH))
pygame.button_down = False

# 控制开始时间
pygame.clock_start = 0


class Cell(pygame.sprite.Sprite):
    size = CELL_SIZE

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([self.size, self.size])
        # 填白色
        self.image.fill(COLOR)
        # 画矩形
        self.rect = self.image.get_rect()
        self.rect.topleft = position


def draw():
    '''画游戏界面'''
    screen.fill((0, 0, 0))
    for sp_col in range(pygame.world.shape[1]):
        for sp_row in range(pygame.world.shape[0]):
            if pygame.world[sp_row][sp_col]:
                new_cell = Cell((sp_col * Cell.size, sp_row * Cell.size))
                screen.blit(new_cell.image, new_cell.rect)


def change_state():
    '''核心逻辑：
            nbrs_count 是计算一个细胞周围细胞的个数
            然后判断，当周围有3个，有两个 以及其他情况下的状态改变
    '''
    nbrs_count = sum(np.roll(np.roll(pygame.world, i, 0), j, 1)
                     for i in (-1, 0, 1) for j in (-1, 0, 1)
                     if (i != 0 or j != 0))
    # for i in (-1, 0 ,1):
    #    for j in (-1, 0 ,1):
    #        if(i != 0 or j != 0):
    #            nbrs_count = sum(np.roll(np.roll(pygame.world, i, 0), j, 1))
    judge_cell_state(nbrs_count)
    # pygame.world = (nbrs_count == 3) | (
    #   (pygame.world == 1) & (nbrs_count == 2)).astype('int')


def judge_cell_state(nbrs_count):
    pygame.world = (nbrs_count == 3) | (
        (pygame.world == 1) & (nbrs_count == 2)).astype('int')

    return pygame.world


def judge_cell_state_exception(nbrs_count):
    if nbrs_count.any() < 0 or nbrs_count.any() > 8:
        raise Exception("nbrs_count should in range(0,8)", nbrs_count)

    pygame.world = (nbrs_count == 3) | (
        (pygame.world == 1) & (nbrs_count == 2)).astype('int')

    return pygame.world


def init():
    '''地图初始化'''
    pygame.world.fill(0)
    draw()
    return 'Stop'


def stop():
    '''停止时的状态'''
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_RETURN:
            return 'Move'
        if event.type == KEYDOWN and event.key == K_r:
            return 'Reset'
        if event.type == MOUSEBUTTONDOWN:
            pygame.button_down = True
            pygame.button_type = event.button
        if event.type == MOUSEBUTTONUP:
            pygame.button_down = False
        if pygame.button_down:
            mouse_control()

    return 'Stop'


def move():
    '''细胞变化时的状态'''
    global FRAME_RATE
    global COLOR
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            return 'Stop'
        if event.type == KEYDOWN and event.key == K_r:
            return 'Reset'
        if event.type == MOUSEBUTTONDOWN:
            pygame.button_down = True
            pygame.button_type = event.button
        if event.type == MOUSEBUTTONUP:
            pygame.button_down = False
        if pygame.button_down:
            mouse_control()
        if event.type == KEYDOWN and event.key == K_q:  # 按键q时帧率变快
            FRAME_RATE = 2 * FRAME_RATE
        if event.type == KEYDOWN and event.key == K_e:  # 按键e时帧率变慢
            FRAME_RATE = FRAME_RATE / 2
        if event.type == KEYDOWN and event.key == K_z:  # 按键z时变蓝色
            COLOR = BLUE
        if event.type == KEYDOWN and event.key == K_x:  # 按键x时变黄色
            COLOR = YELLOW
        if event.type == KEYDOWN and event.key == K_c:  # 按键c时变白色
            COLOR = WHITE
        if event.type == KEYDOWN and event.key == K_v:  # 按键v时变蓝色
            COLOR = C1
        if event.type == KEYDOWN and event.key == K_b:  # 按键b时变黄色
            COLOR = C2
        if event.type == KEYDOWN and event.key == K_n:  # 按键n时变白色
            COLOR = C3
        if event.type == KEYDOWN and event.key == K_m:  # 按键m时变白色
            COLOR = C4
    if time.clock() - pygame.clock_start > FRAME_RATE:
        change_state()
        draw()
        pygame.clock_start = time.clock()

    return 'Move'


def color_change():
    dict_color = {
        K_z: YELLOW
    }


def mouse_control():
    '''鼠标控制细胞的生命'''
    mouse_x, mouse_y = pygame.mouse.get_pos()
    sp_col = mouse_x / Cell.size
    sp_row = mouse_y / Cell.size
    if pygame.button_type == 1:  # 鼠标左键，细胞活
        pygame.world[sp_row][sp_col] = 1
    elif pygame.button_type == 3:  # 鼠标右键，细胞亡
        pygame.world[sp_row][sp_col] = 0
    draw()


if __name__ == '__main__':
    '''main函数
        创建状态机来转换游戏的三种状态
        初始化界面
        开始游戏主循环
    '''
    state_actions = {
        'Reset': init,
        'Stop': stop,
        'Move': move
    }
    state = 'Reset'
    pygame.init()
    icon_res = "./twIcon.png"
    icon = pygame.image.load(icon_res)
    pygame.display.set_icon(icon)
    pygame.display.set_caption('ThoughtWorksPairCodingGame!')
    screen = pygame.display.set_mode((WIDTH * Cell.size, HEIGHT * Cell.size))
    while True:  # 游戏主循环
        state = state_actions[state]()
        pygame.display.update()
