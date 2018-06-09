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
