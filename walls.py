import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, screen, size, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/walls.png")
        self.image = pygame.transform.scale(self.image, size)
        self.image.set_colorkey((152, 152, 152))
        self.screen = screen
        self.rect = self.image.get_rect()
        self.add(group)

    def update(self):
        self.screen.blit(self.image, (0, 0))


class BackGround(pygame.sprite.Sprite):
    def __init__(self, screen, size, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/walls.png")
        self.image = pygame.transform.scale(self.image, size)
        self.screen = screen
        self.rect = self.image.get_rect()
        self.add(group)

    def update(self):
        self.screen.blit(self.image, (0, 0))


def create_environment(screen, size, group_wall, group_background):
    Wall(screen, size, group_wall)
    BackGround(screen, size, group_background)
    pass
