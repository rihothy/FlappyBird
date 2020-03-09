import pygame

class Land(pygame.sprite.Sprite):

    def __init__(self, path):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.y = 400
        self.t = pygame.time.Clock()
        self.x = 0.0
        self.step = 0.0

    def circulate(self, v):
        self.step = self.t.tick() / 1000 * v
        self.x -= self.step
        if self.x < -24:
            self.x = 0.0
        self.rect.x = self.x

    def update(self, screen):
        screen.blit(self.image, self.rect)