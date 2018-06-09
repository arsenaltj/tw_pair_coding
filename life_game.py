# -*- coding:utf8 -*-
import pygame
import sys
import time
import numpy as np
from pygame.locals import *

# 矩阵宽，高
WIDTH = 80
HEIGHT = 40
# 细胞大小，动画帧率
CELL_SIZE = 10
FRAME_RATE = 0.1


class Cell(pygame.sprite.Sprite):
    size = CELL_SIZE

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([self.size, self.size])
        # 填白色
        self.image.fill((255, 255, 255))
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


if __name__ == "__main__":
    screen = pygame.display.set_mode((WIDTH * Cell.size, HEIGHT * Cell.size))
