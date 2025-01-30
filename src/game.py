import pygame
import random

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
GRAVITY = 0.5
JUMP_STRENGTH = -10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cow Platformer")

# Load assets
cow_img = pygame.image.load("cow.jpg")
cow_img = pygame.transform.scale(cow_img, (50, 50))

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = cow_img
        self.rect = self.image.get_rect(midbottom=(WIDTH//2, HEIGHT-50))
        self.vel_y = 0
        self.on_ground = False

    def jump(self):
        if self.on_ground:
            self.vel_y = JUMP_STRENGTH
            self.on_ground = False

    def update(self):
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.vel_y = 0
            self.on_ground = True

# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(topleft=(x, y))

# Create player and platforms
player = Player()
platforms = pygame.sprite.Group()
platforms.add(Platform(300, 500, 200, 20))
platforms.add(Platform(100, 400, 200, 20))
platforms.add(Platform(500, 300, 200, 20))

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(platforms)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.jump()
    
    player.update()
    all_sprites.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
