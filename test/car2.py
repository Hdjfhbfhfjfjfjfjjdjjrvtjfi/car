import pygame

vec = pygame.math.Vector2


class Car(pygame.sprite.Sprite):
    def __init__(self, group):
        pygame.sprite.Sprite.__init__(self)
        self.max_speed = 2
        self.position = vec(100, 100)
        self.speed = vec(0, 0)
        self.image = pygame.image.load('../images/car.png').convert()
        self.image = pygame.transform.scale(self.image, (20, 39)).convert_alpha()
        self.images = []
        for i in range(0, 361):
            image = pygame.transform.rotate(self.image, i)
            image.set_colorkey((255, 255, 255))
            self.images.append(image)
        self.image.set_colorkey((255, 255, 255))
        self.original_image = self.image
        self.original_vector = vec(0, -1)
        self.front = vec(0, -1)
        self.acceleration = 0.1
        self.rect = self.image.get_rect()
        self.angle = 0
        self.angle_speed = 0
        self.add(group)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.speed.scale_to_length(self.speed.length() + self.acceleration)
        self.position += self.speed
        self.rect.center = self.position

    def collide(self, group):
        wall = pygame.sprite.spritecollideany(self, group, collided=pygame.sprite.collide_mask)
        if wall is not None:
            self.position = vec(220, 500)
            self.image = self.original_image
            self.speed.scale_to_length(0)
            self.angle = 0
            self.acceleration = vec(0, -0.1)
            self.speed.rotate_ip(self.speed.angle_to(self.front))

    def wrap_around_screen(self, width, height):
        if self.position.x > width:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = width
        if self.position.y <= 0:
            self.position.y = height
        if self.position.y > height:
            self.position.y = 0
