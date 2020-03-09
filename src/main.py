import pygame
import sys

import bird
import land
import pipe
import score
import button
import picture

WHITE = pygame.Color(255, 255, 255)
FPS = 250

pygame.mixer.pre_init(22050, -16, 2, 32)
pygame.mixer.init()
pygame.init()

pygame.display.set_caption("Flappy Bird")
pygame.display.set_icon(pygame.image.load("res/icon.png"))
screen = pygame.display.set_mode((288, 512), pygame.DOUBLEBUF)
fps = pygame.time.Clock()

die_snd = pygame.mixer.Sound("res/sounds/die.ogg")
fall_snd = pygame.mixer.Sound("res/sounds/fall.ogg")

bird = bird.Bird("res/bird.png")
land = land.Land("res/land.png")

background = picture.Picture("res/bk.png")
button = button.Button("res/button.png", (86, 330))
logo = picture.Picture("res/logo.png", (55, 140))

bird.set_pos((144, 225))
group = pygame.sprite.Group(background, button, logo, land, bird)

begin = False
while not begin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and button.clicked(pygame.mouse.get_pos()):
            begin = True
    
    bird.wave(32, 220, 230)
    land.circulate(120)

    group.update(screen)
    pygame.display.flip()
    fps.tick(FPS)

while True:
    bird.set_pos((88, 255))
    my_score = score.Score((144, 90))
    tap = picture.Picture("res/tap.png", (87, 220))
    ready = picture.Picture("res/ready.png", (46, 140))

    group = pygame.sprite.Group(background, ready, tap, land, bird, my_score)

    pygame.event.clear()
    begin = False
    while not begin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                begin = True
        
        bird.wave(32, 250, 260)
        land.circulate(120)

        group.update(screen)
        pygame.display.flip()
        fps.tick(FPS)
    
    bird.set_pos((88, 255))
    bird.jump("play sound")
    
    pipe1 = pipe.Pipe("res/pipe.png", 288.0)
    pipe2 = pipe.Pipe("res/pipe.png", 458.0)

    group = pygame.sprite.Group(background, pipe1, pipe2, land, bird, my_score)
    
    pygame.event.clear()
    while not pygame.sprite.collide_mask(bird, land) and not pygame.sprite.collide_mask(bird, pipe1) and not pygame.sprite.collide_mask(bird, pipe2):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                bird.jump("play sound")

        bird.fall()
        land.circulate(120)
        pipe1.circulate(land)
        pipe2.circulate(land)
        my_score.add([pipe1, pipe2])

        group.update(screen)
        pygame.display.flip()
        fps.tick(FPS)
    
    die_snd.play()

    screen.fill(WHITE)
    pygame.display.flip()

    pygame.time.delay(156)

    group.remove(my_score)

    if not bird.out():
        bird.jump()
        fall_snd.play()

        while not bird.out():
            bird.fall()
            group.update(screen)
            pygame.display.flip()
            fps.tick(FPS)
    
    my_font = pygame.font.Font(None, 26)

    game_over = picture.Picture("res/over.png", (42, 140))
    score_board = picture.Picture("res/score_board.png", (25, 200))

    group.add(game_over, score_board, button)

    for i in range(0, my_score.val + 1):
        image = my_font.render(str(i), True, WHITE)
        rect = image.get_rect()
        rect.centerx, rect.centery = (218, 290)
        group.update(screen)
        screen.blit(image, rect)
        pygame.display.flip()
        pygame.time.delay(int(512 / (my_score.val + 1)))

    pygame.event.clear()
    begin = False
    while not begin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and button.clicked(pygame.mouse.get_pos()):
                begin = True
        fps.tick(FPS)