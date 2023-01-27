from pygame import *
from project2.test.car2 import *

init()

WIDTH = 800
HEIGHT = 500
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (204, 153, 255)
MINT = (32, 230, 156)

screen = display.set_mode((WIDTH, HEIGHT), vsync=1)
display.set_caption('Game')

FPS = 60
clock = time.Clock()

all_players = sprite.Group()

car = Car(all_players)

while True:
    for ev in event.get():
        if ev.type == QUIT:
            exit()
        elif ev.type == KEYDOWN and ev.key == pygame.constants.K_ESCAPE:
            exit()
    car.wrap_around_screen(WIDTH, HEIGHT)
    all_players.update()
    screen.fill(BLACK)
    all_players.draw(screen)
    display.update()
    clock.tick_busy_loop(FPS)
