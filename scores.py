import pygame


class Start(pygame.sprite.Sprite):
    def __init__(self, coord, group):
        pygame.sprite.Sprite.__init__(self)
        self.position = coord
        self.add(group)
        self.image = pygame.Surface((150, 2))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(coord[0]+75, coord[1]+1))


class Middle(pygame.sprite.Sprite):
    def __init__(self, coord, group):
        pygame.sprite.Sprite.__init__(self)
        self.position = coord
        self.add(group)
        self.image = pygame.Surface((200, 2))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(coord[0] + 75, coord[1] + 1))


def create_start(coord, group):
    Start(coord, group)


def create_middle(coord, group):
    Middle(coord, group)


