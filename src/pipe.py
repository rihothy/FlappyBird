import pygame
import random

import land

class Pipe(pygame.sprite.Sprite):

    def __init__(self, path, x):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.x = x
        self.rect.y = random.randint(50, 200) - 320

    def circulate(self, land):
        self.x -= land.step
        if self.x < -52:
            self.x = 288.0
            self.rect.y = random.randint(50, 200) - 320
        self.rect.x = self.x

    def update(self, screen):
        screen.blit(self.image, self.rect)