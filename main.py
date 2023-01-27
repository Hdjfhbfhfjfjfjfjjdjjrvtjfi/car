import pygame as pg
from car import Car
from scores import *
from walls import *

pg.init()

WIDTH = 1680
HEIGHT = 1050
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pg.display.set_mode((WIDTH, HEIGHT), vsync=1)
pg.display.set_caption('Game')

FPS = 60
clock = pg.time.Clock()

all_players = pg.sprite.Group()
start_group = pg.sprite.Group()
middle_group = pg.sprite.Group()
walls_group = pg.sprite.Group()
background_group = pg.sprite.Group()

car = Car(all_players)
font = pg.font.SysFont("arial", 40)

create_environment(screen, (WIDTH, HEIGHT), walls_group, background_group)
create_middle((775, 500), middle_group)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.KEYDOWN and event.key == pygame.constants.K_ESCAPE:
            exit()

    all_players.update()
    car.collect_score(start_group, middle_group)
    car.collide(walls_group, start_group, middle_group)
    screen.fill(BLACK)
    walls_group.update()
    middle_group.draw(screen)
    start_group.draw(screen)
    background_group.update()
    all_players.draw(screen)
    text = font.render(f"Кругов: {car.score}", False, BLACK, WHITE)
    text.set_colorkey(WHITE)
    screen.blit(text, (1500, 20))
    pg.display.update()
    clock.tick_busy_loop(FPS)
