import pygame
import picture

class Button(picture.Picture):

    def __init__(self, path, pos = (0, 0)):
        super().__init__(path, pos)
        self.hit_snd = pygame.mixer.Sound("res/sounds/swooshing.ogg")
    
    def clicked(self, pos):
        x, y = pos;
        if x > self.rect.left and x < self.rect.right and y > self.rect.top and y < self.rect.bottom:
            self.hit_snd.play()
            return True
        else:
            return False