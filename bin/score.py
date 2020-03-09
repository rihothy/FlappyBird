import pygame

from bin import pipe

class Score(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.val = 0
        self.enables = [True, True]
        self.font = pygame.font.Font(None, 68)
        self.add_snd = pygame.mixer.Sound("res/sounds/point.ogg")
        self.pos = pos
    
    def update(self, screen):
        image = self.font.render(str(self.val), True, (255, 255, 255))
        rect = image.get_rect()
        rect.centerx, rect.centery = self.pos
        screen.blit(image, rect)

    def add(self, pipes):
        for i, pipe in enumerate(pipes):
            if pipe.rect.centerx > 288:
                self.enables[i] = True
            if self.enables[i] and pipe.rect.centerx < 56:
                self.add_snd.play()
                self.val += 1
                self.enables[i] = False