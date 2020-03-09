import pygame

class Picture(pygame.sprite.Sprite):

    def __init__(self, path, pos = (0, 0)):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = pos
    
    def set_pos(self, pos):
        self.rect.left, self.rect.top = pos
    
    def update(self, screen):
        screen.blit(self.image, self.rect)