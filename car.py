from scores import *
vec = pygame.math.Vector2


class Car(pygame.sprite.Sprite):
    def __init__(self, group):
        pygame.sprite.Sprite.__init__(self)
        self.max_speed = 5
        """5"""
        self.position = vec(220, 500)
        self.speed = vec(0, 0)
        self.score = 0
        self.image = pygame.image.load('images/car.png').convert()
        self.image = pygame.transform.scale(self.image, (10, 20)).convert_alpha()
        self.image.set_colorkey((255, 255, 255))
        self.original_image = self.image
        self.front = vec(0, 1)
        self.acceleration = vec(0, -0.15)
        self.rect = self.image.get_rect()
        self.angle = 0
        self.angle_speed = 0
        self.add(group)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.angle_speed = -3
            self.rotate()
            """3"""
        if keys[pygame.K_d]:
            self.angle_speed = 3
            self.rotate()
        if keys[pygame.K_w]:
            self.speed += self.acceleration
        if keys[pygame.K_s]:
            self.speed -= self.acceleration
        if not keys[pygame.K_w] and not keys[pygame.K_s]:
            speed = self.speed.length() - 0.25
            if speed <= 0:
                self.speed = vec(0, 0)
            else:
                self.speed.scale_to_length(speed)

        if self.speed.length() > self.max_speed:
            self.speed.scale_to_length(self.max_speed)
        self.position += self.speed
        self.rect.center = self.position

    def rotate(self):
        self.acceleration.rotate_ip(self.angle_speed)
        self.angle += self.angle_speed
        if self.angle > 360:
            self.angle -= 360
        elif self.angle < 0:
            self.angle += 360
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.image.set_colorkey((255, 255, 255))

    def collide(self, group, start_group, middle_group):
        wall = pygame.sprite.spritecollideany(self, group, collided=pygame.sprite.collide_mask)
        if wall is not None:
            try:
                start_group.sprites()[0].kill()
            except IndexError:
                pass
            try:
                middle_group.sprites()[0].kill()
            except IndexError:
                pass
            self.position = vec(220, 500)
            self.image = self.original_image
            self.speed.scale_to_length(0)
            self.angle = 0
            self.acceleration = vec(0, -0.1)
            self.speed.rotate_ip(self.speed.angle_to(self.front))
            create_middle((775, 500), middle_group)

    def collect_score(self, start_group, middle_group):
        start = pygame.sprite.spritecollideany(self, start_group, collided=pygame.sprite.collide_mask)
        middle = pygame.sprite.spritecollideany(self, middle_group, collided=pygame.sprite.collide_mask)
        if start is not None:
            self.score += 1
            start_group.sprites()[0].kill()
            create_middle((775, 500), middle_group)
        elif middle is not None:
            middle_group.sprites()[0].kill()
            create_start((170, 500), start_group)
