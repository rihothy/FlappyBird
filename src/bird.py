import pygame

G = 1500

class Bird(pygame.sprite.Sprite):

    def __init__(self, path):
        super().__init__()
        self.master_image = pygame.image.load(path)
        self.image = self.master_image.subsurface((0, 0, 48, 48))
        self.rect = self.image.get_rect()
        self.jump_snd = pygame.mixer.Sound("res/sounds/jump.ogg")
        self.t_fall = pygame.time.Clock()
        self.t_swing = pygame.time.get_ticks()
        self.hight = 0.0
        self.pos = 0
        self.v = 0.0

    def update(self, screen):
        th = -90
        if self.v < 100:
            th = 30
        elif self.v < 300:
            th = (1 - (self.v - 100) / 200) * 30
        elif self.v < 700:
            th = (self.v - 300) / 400 * -90
        
        if pygame.time.get_ticks() - self.t_swing > 72:
            self.t_swing = pygame.time.get_ticks()
            self.pos = (self.pos + 1) % 4
            self.image = self.master_image.subsurface((self.pos * 48, 0, 48, 48))
        
        image = pygame.transform.rotate(self.image, th)
        rect = image.get_rect()
        rect.centerx = self.rect.centerx
        rect.centery = self.rect.centery = self.hight
        screen.blit(image, rect)

    def set_pos(self, pos):
        self.v = 0.0
        self.t_fall.tick()
        self.rect.centerx, self.hight = pos
    
    def fall(self):
        dt = self.t_fall.tick() / 1000
        dv = self.v
        self.v += G * dt
        self.hight += (dv + self.v) / 2 * dt
    
    def wave(self, v, top, buttom):
        if not hasattr(Bird.wave, 'dir'):
            Bird.wave.dir = "up"
        
        self.v = 300
        dt = self.t_fall.tick() / 1000
        self.hight += v * dt * (-1 if Bird.wave.dir == "up" else 1)

        if self.hight > buttom:
            Bird.wave.dir = "up"
            self.hight = buttom
        elif self.hight < top:
            Bird.wave.dir = "down"
            self.hight = top

    def jump(self, cmd = None):
        if self.hight > 0:
            if cmd == "play sound":
                self.jump_snd.play()
            self.v = -400

    def out(self):
        if self.hight >= 386:
            return True
        else:
            return False